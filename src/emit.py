"""Stage 5 — render the published artifacts."""

import hashlib
import json
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

from src.config import VulnClass
from src.extractors.base import Candidate
from src.llm.provider import Verdict
from src.redact import redact

PROVENANCE_FIELDS = (
    "id", "url", "title", "program", "reporter", "severity", "bounty", "disclosed_at",
)

REDACTED_TEXT_FIELDS = ("title", "program", "reporter")


def _safe_text(value):
    """Redact a corpus-derived text field, never dropping the record for it.

    Payload, technique and param drop the record when they cannot be cleared,
    because an unpublishable payload is worthless. A title is different: the
    payload beside it is still valuable, so an uncleanable title is replaced
    rather than taken as a reason to discard the finding.
    """
    if value is None:
        return None
    cleaned = redact(str(value))
    return cleaned if cleaned is not None else "[redacted]"


MAX_SLUG = 80


def _slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", str(value).lower()).strip("-")
    # Program names come from corpus data we do not control. An unbounded slug
    # becomes a filename longer than the filesystem allows, and ENAMETOOLONG
    # kills the whole run rather than skipping one page.
    return slug[:MAX_SLUG].strip("-") or "unknown"


def build_records(
    candidates: list[Candidate],
    verdicts: list[Verdict],
    index: dict[int, dict],
    classes: dict[str, VulnClass],
) -> list[dict]:
    by_key = {v.key: v for v in verdicts}
    records: list[dict] = []
    seen: set[tuple[str, str]] = set()

    for candidate in candidates:
        verdict = by_key.get(candidate.key())
        if verdict is None or not verdict.is_payload:
            continue
        payload = redact(candidate.payload)
        if payload is None:
            continue
        if not _is_substantive(payload):
            continue

        # The model is shown the raw, unredacted payload and context, so its
        # description can quote a secret it was shown. Without this pass a
        # credential reaches the public repo through the technique sentence
        # while the payload field beside it was correctly redacted -- the one
        # route into the published tree that bypasses the payload gate.
        technique = redact(verdict.technique) if verdict.technique else ""
        if technique is None:
            continue
        param = redact(verdict.param) if verdict.param else None
        if verdict.param and param is None:
            continue

        report = index.get(candidate.report_id)
        if report is None:
            continue
        identity = (candidate.cls, payload)
        if identity in seen:
            continue
        seen.add(identity)

        # title, program and reporter are corpus-derived free text and never
        # otherwise see redact(): without this pass they are the one path
        # into the published tree that bypasses the redaction gate the
        # payload/technique/param fields above go through.
        safe_report = dict(report)
        for field in REDACTED_TEXT_FIELDS:
            safe_report[field] = _safe_text(report.get(field))
        # The url is reconstructable from the id, so derive it rather than
        # passing it through redaction -- hackerone.com is not a SAFE_HOST,
        # so redaction would rewrite the host and silently point every
        # provenance link at the wrong domain (or, for a high-entropy url,
        # drop it to "[redacted]" entirely).
        safe_report["url"] = f"https://hackerone.com/reports/{report.get('id')}"

        records.append({
            "id": hashlib.sha1(f"{candidate.cls}\x00{payload}".encode()).hexdigest()[:8],
            "class": candidate.cls,
            "payload": payload,
            "technique": technique,
            "param": param,
            "report": {field: safe_report.get(field) for field in PROVENANCE_FIELDS},
        })
    return records


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _escape_link_text(text: str) -> str:
    """Escape characters that would corrupt a `[text](url)` markdown link."""
    return text.replace("[", "\\[").replace("]", "\\]")


def _fence_for(payload: str) -> str:
    """A fence longer than any backtick run inside the payload.

    CommonMark closes a fence on the first run of at least the opening length,
    so a payload containing ``` escaped its block and the remainder rendered as
    markdown -- its own "## Impact" line became a page heading.
    """
    longest = max((len(run) for run in re.findall(r"`+", payload)), default=0)
    return "`" * max(3, longest + 1)


def _entry_markdown(record: dict) -> str:
    report = record["report"]
    bounty = f" · ${report['bounty']:,}" if report.get("bounty") else ""
    param = f"\n**Parameter:** `{record['param']}`" if record.get("param") else ""
    title = _escape_link_text(report["title"] or "Untitled report")
    reporter = report.get("reporter") or "unknown"
    return (
        f"### `{record['id']}`\n\n"
        f"{_fence_for(record['payload'])}\n{record['payload']}\n"
        f"{_fence_for(record['payload'])}\n"
        f"{param}\n"
        f"— [{title}]({report['url']}) · {report['program']} · "
        f"[{reporter}](https://hackerone.com/{reporter})"
        f"{bounty}\n"
    )


# A payload needs at least one character that could act on a target. Extractors
# pull fragments like "'../'" out of prose, and the model does not reliably
# reject them; a wordlist full of quote marks is worse than one without.
_HAS_SUBSTANCE = re.compile(r"[A-Za-z0-9]")
MIN_PAYLOAD_CHARS = 4


def _is_substantive(payload: str) -> bool:
    stripped = payload.strip().strip("'\"`")
    return len(stripped) >= MIN_PAYLOAD_CHARS and bool(_HAS_SUBSTANCE.search(stripped))


def _is_single_line(payload: str) -> bool:
    return "\n" not in payload and "\r" not in payload


# Grouping on the exact technique sentence produced 741 headings for 803
# payloads -- a flat dump wearing a heading, since the model writes a distinct
# sentence per payload. Keying on the leading significant words clusters real
# variants ("svg onload", "img onerror") while staying specific enough that a
# heading still means something.
_TECHNIQUE_STOPWORDS = frozenset({
    "the", "a", "an", "in", "to", "via", "using", "of", "with", "by", "that",
    "is", "and", "for", "on",
})
_TECHNIQUE_WORDS = 4


def _technique_key(technique: str | None) -> str:
    words = re.findall(r"[a-z]+", (technique or "").lower())
    keep = [w for w in words if w not in _TECHNIQUE_STOPWORDS][:_TECHNIQUE_WORDS]
    return " ".join(keep) or "ungrouped"


def _grouped_markdown(entries: list[dict]) -> str:
    """Render entries grouped under their technique sentence as a subheading.

    Groups are ordered by descending size (the biggest technique cluster
    first), entries within a group by descending bounty. Payloads sharing an
    identical technique sentence cluster together, which is real grouping
    rather than a flat dump with a claim attached to it.
    """
    groups: dict[str, list[dict]] = defaultdict(list)
    for record in entries:
        groups[_technique_key(record["technique"])].append(record)

    ordered = sorted(groups.items(), key=lambda item: (-len(item[1]), item[0]))
    sections = []
    for _, group in ordered:
        # Heading is the group's most common full sentence, so it reads as
        # English rather than as the normalised key it was grouped on.
        technique = Counter(
            r["technique"] for r in group if r["technique"]
        ).most_common(1)
        technique = technique[0][0] if technique else "Ungrouped"
        ranked = sorted(group, key=lambda r: r["report"].get("bounty") or 0, reverse=True)
        body = "\n".join(_entry_markdown(r) for r in ranked)
        sections.append(f"## {technique}\n\n{body}")
    return "\n\n".join(sections)


def emit(records: list[dict], classes: dict[str, VulnClass], out_dir: Path) -> None:
    _write(out_dir / "payloads.json", json.dumps(records, indent=2) + "\n")

    # A multi-line payload legitimately occurs (a fenced code block is
    # captured whole), but both flat formats assume one payload per line --
    # a three-line payload becomes three wordlist entries, and the
    # tab-separated report URL in payloads.txt attaches only to its last
    # line. Excluded here; it still renders correctly in payloads.json and
    # the markdown pages below, which do not assume single-line entries.
    flat = "\n".join(
        f"{r['payload']}\t{r['report']['url']}"
        for r in records if _is_single_line(r["payload"])
    )
    _write(out_dir / "payloads.txt", flat + "\n")

    by_class: dict[str, list[dict]] = defaultdict(list)
    for record in records:
        by_class[record["class"]].append(record)

    for slug, vuln in classes.items():
        entries = by_class.get(slug, [])
        body = _grouped_markdown(entries) if entries else "_No payloads extracted yet._\n"
        _write(
            out_dir / "payloads" / f"{slug}.md",
            f"# {vuln.name}\n\n{len(entries)} payloads from disclosed reports.\n\n{body}",
        )
        words = sorted({r["payload"] for r in entries if _is_single_line(r["payload"])})
        _write(out_dir / "wordlists" / f"{slug}.txt", "\n".join(words) + ("\n" if words else ""))

    by_program: dict[str, list[dict]] = defaultdict(list)
    for record in records:
        by_program[record["report"].get("program") or "Unknown"].append(record)
    for program, entries in by_program.items():
        body = "\n".join(_entry_markdown(r) for r in entries)
        _write(
            out_dir / "by-program" / f"{_slugify(program)}.md",
            f"# {program}\n\n{len(entries)} payloads.\n\n{body}",
        )

    ranked = sorted(records, key=lambda r: r["report"].get("bounty") or 0, reverse=True)[:100]
    _write(
        out_dir / "top-payloads" / "by-bounty.md",
        "# Top payloads by bounty\n\n" + "\n".join(_entry_markdown(r) for r in ranked),
    )

    programs = len(by_program)
    total_bounty = sum(r["report"].get("bounty") or 0 for r in records)
    bounty_count = sum(1 for r in records if r["report"].get("bounty"))
    report_count = len({r["report"]["id"] for r in records})
    stamp = datetime.now(timezone.utc).strftime("%B %d, %Y at %H:%M UTC")
    rows = "\n".join(
        f"| [{classes[s].name}](payloads/{s}.md) | {len(by_class.get(s, []))} |" for s in classes
    )
    readme = f"""# HackerOne Disclosed Reports Payloads

**Real bug bounty payloads extracted from disclosed HackerOne reports — every
one of them worked on a live production target.**

A searchable payload list for XSS, SQL injection, SSRF, path traversal, SSTI,
XXE, open redirect, CSRF, IDOR and RCE, drawn from {report_count:,} disclosed
HackerOne reports. Every payload links back to the report it came from and the
researcher who found it.

## 📊 Statistics

| Metric | Count |
|---|---|
| **Total Payloads** | {len(records):,} |
| **Classes Covered** | {len(classes)} |
| **Programs Represented** | {programs:,} |
| **Bounty Behind Them** | ${total_bounty:,.0f} |

*Last Updated: {stamp}*

## Payloads by vulnerability class

| Class | Payloads |
|---|---|
{rows}

Each page groups payloads by technique variant, so the `svg onload` cases sit
together rather than scattered through a flat list.

## Wordlists for ffuf, Burp Intruder and sqlmap

[`wordlists/`](wordlists/) holds one plain-text file per class — deduplicated
raw payload strings, one per line, no markdown and no commentary. Load them
directly with `ffuf -w`, paste into Burp Intruder, or feed to any fuzzer that
takes a wordlist.

## How this differs from a generic payload list

Collections like PayloadsAllTheThings are curated lists of payloads that
*should* work. Every entry here is one that **did** — it appears in a public
HackerOne report, used against a real production target and accepted as a valid
finding. {bounty_count:,} of them also earned a bounty, totalling
${total_bounty:,.0f}. The report link is on every entry, so you can read the
context a payload was used in rather than guessing at it.

## Browse

| Category | Description |
|---|---|
| [By Program](by-program/) | Payloads that worked, per bug bounty program |
| [Top Payloads](top-payloads/) | Ranked by bounty paid |
| [Wordlists](wordlists/) | Raw strings, one per line, tool-ready |

## Data files

- `payloads.json` — structured record per payload, with full provenance
- `payloads.txt` — flat payload + report URL list (single-line payloads only;
  multi-line payloads are in `payloads.json` and `payloads/` instead)
- `payloads/` — one page per vulnerability class, grouped by technique
- `wordlists/` — deduplicated raw strings for ffuf, Burp Intruder and friends
  (single-line payloads only, so every line loads as one entry)

## How the data is built

Rebuilt daily from the public archive of disclosed HackerOne reports. Payloads
are extracted deterministically, then filtered so that vulnerable source code,
log lines and reference links do not end up in the dataset. Victim hostnames
are normalised — `target.com` is where a payload starts, `evil.com` is where it
sends you — and anything credential-shaped is dropped rather than published.

## Related projects

- [Self-Hosted Bug Bounty & Disclosure Programs](https://github.com/ashikkunjumon/Self-Hosted-Bug-Bounty-Programs)
  — 7,500+ vulnerability disclosure and bug bounty programs, indexed by country
- [Bug Bounty Dorks Automation](https://github.com/ashikkunjumon/Bug-Bounty-Dorks-Automation)
  — search-engine dorks for recon and for finding programs to test
"""

    readme_path = out_dir / "README.md"
    # The timestamp stamped into every render would otherwise make
    # git diff --cached --quiet never true, so "commit only on change" never
    # fires and a day with no newly disclosed reports still produces a
    # commit. Only rewrite the file when something other than the stamp
    # changed; a no-op day leaves it byte-for-byte as it was.
    if readme_path.exists() and _without_stamp(readme_path.read_text(encoding="utf-8")) == _without_stamp(readme):
        return
    _write(readme_path, readme)


def _without_stamp(text: str) -> str:
    return "\n".join(
        line for line in text.splitlines() if not line.startswith("*Last Updated:")
    )
