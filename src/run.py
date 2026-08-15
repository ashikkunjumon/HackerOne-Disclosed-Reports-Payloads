"""CLI entry point wiring the five pipeline stages."""

import argparse
import json
import sys
from pathlib import Path

from src.classify import classify_report
from src.config import VulnClass, load_classes
from src.confirm import confirm
from src.emit import build_records, emit
from src.extractors import EXTRACTORS
from src.extractors.base import Candidate
from src.llm.provider import NvidiaProvider
from src.sync import sync_corpus

CORPUS = Path("data/corpus")
VERDICTS = Path("data/verdicts.jsonl")

# A record count more than a small drop below what is already published is
# treated as a collapse rather than a legitimate shrink -- see C1 in the
# final review. A throttled corpus sync or a broken provider must not be
# able to publish an empty or shrunken dataset silently.
SHRINK_FLOOR = 0.90


def _previous_count(out_dir: Path) -> int:
    path = out_dir / "payloads.json"
    if not path.exists():
        return 0
    try:
        return len(json.loads(path.read_text(encoding="utf-8")))
    except (json.JSONDecodeError, OSError):
        return 0


def _write_diagnostics(data_dir: Path, classified: dict, candidates: list[Candidate]) -> None:
    """Write the stage 2/3 artifacts spec S5.2/S6 calls for: a report-id ->
    classes/signal map, so misclassification is debuggable, and one
    candidate per line, so each stage is independently re-runnable from
    disk. These are diagnostic outputs -- a failure to write them must not
    abort the run.
    """
    try:
        data_dir.mkdir(parents=True, exist_ok=True)
        (data_dir / "classified.json").write_text(
            json.dumps(classified, indent=2) + "\n", encoding="utf-8"
        )
        with (data_dir / "candidates.jsonl").open("w", encoding="utf-8") as handle:
            for candidate in candidates:
                handle.write(json.dumps({
                    "report_id": candidate.report_id,
                    "class": candidate.cls,
                    "payload": candidate.payload,
                    "context": candidate.context,
                    "extractor": candidate.extractor,
                }) + "\n")
    except OSError as error:
        print(f"extract_candidates: failed to write diagnostics ({error})", file=sys.stderr)


def extract_candidates(
    index: dict[int, dict],
    corpus: Path,
    classes: dict[str, VulnClass],
    data_dir: Path | None = None,
) -> list[Candidate]:
    candidates: list[Candidate] = []
    classified: dict[str, dict] = {}
    for report_id, record in index.items():
        body_path = corpus / "reports" / f"{report_id}.md"
        if not body_path.exists():
            continue
        body = body_path.read_text(encoding="utf-8", errors="replace")
        classification = classify_report(record, body, classes)
        classified[str(report_id)] = {
            "classes": list(classification.classes),
            "signal": classification.signal,
        }
        for slug in classification.classes:
            extract = EXTRACTORS.get(slug)
            if extract:
                candidates.extend(extract(report_id, body))

    if data_dir is not None:
        _write_diagnostics(data_dir, classified, candidates)
    return candidates


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build the disclosed-payload dataset.")
    parser.add_argument("--out", type=Path, default=Path("."))
    parser.add_argument("--limit", type=int, default=None,
                        help="cap newly fetched reports (useful for a first smoke run)")
    parser.add_argument("--skip-sync", action="store_true")
    parser.add_argument("--dry-run", action="store_true",
                        help="extract and report counts without calling the LLM")
    parser.add_argument("--max-candidates", type=int, default=None,
                        help="cap how many candidates reach the LLM — use this to smoke-test "
                             "the live API without paying for the whole backfill")
    parser.add_argument("--allow-shrink", action="store_true",
                        help="publish even if the new record count collapses relative to "
                             "the already-published payloads.json")
    args = parser.parse_args(argv)

    classes = load_classes()

    if not args.skip_sync:
        result = sync_corpus(CORPUS, limit=args.limit)
        bootstrap_note = (
            f"{result.bootstrapped} from tarball, " if result.bootstrapped else ""
        )
        print(f"sync: {bootstrap_note}{result.fetched} fetched, "
              f"{result.skipped} already present, {result.failed} failed")

    index_records = json.loads((CORPUS / "index.json").read_text(encoding="utf-8"))
    index = {r["id"]: r for r in index_records}

    candidates = extract_candidates(index, CORPUS, classes, data_dir=CORPUS.parent)
    print(f"candidates: {len(candidates)}")

    if args.dry_run:
        return 0

    if args.max_candidates is not None:
        candidates = candidates[:args.max_candidates]
        print(f"capped to {len(candidates)} candidates")

    verdicts = confirm(candidates, NvidiaProvider(), VERDICTS)
    records = build_records(candidates, verdicts, index, classes)
    print(f"payloads: {len(records)}")

    previous = _previous_count(args.out)
    if previous and len(records) < previous * SHRINK_FLOOR and not args.allow_shrink:
        print(
            f"refusing to publish: {len(records)} payloads is a collapse from the "
            f"{previous} already published. Re-run with --allow-shrink if this is "
            f"intended.",
            file=sys.stderr,
        )
        return 1

    emit(records, classes, args.out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
