"""Stage 1 — incremental mirror of the reference report corpus."""

import io
import json
import re
import tarfile
import urllib.request
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path

BASE = "https://raw.githubusercontent.com/ajaysenr/HackerOne-Disclosed-Reports/main"
INDEX_URL = f"{BASE}/index.json"
TARBALL_URL = (
    "https://codeload.github.com/ajaysenr/HackerOne-Disclosed-Reports/tar.gz/refs/heads/main"
)
USER_AGENT = "HackerOne-Disclosed-Reports-Payloads/0.1 (+https://github.com/ashikkunjumon)"

# Above this many missing reports, fetch the whole corpus as one tarball
# instead of one request per report. Measured: 9,946 reports take ~80 minutes
# per-file at ~2/sec, versus ~11 seconds for a 12MB tarball. That matters most
# in CI, where data/corpus is not persisted, so every run is a cold start --
# the per-file path would spend an hour hammering a public endpoint daily and
# trip the throttling that MAX_FAILURE_RATE then correctly aborts on.
BOOTSTRAP_THRESHOLD = 500

# Only files matching this shape are extracted, and the destination is built
# from the captured id rather than the archive's own path, so a crafted member
# name cannot escape the reports directory.
_REPORT_MEMBER = re.compile(r"(?:^|/)reports/(\d+)\.md$")

# urllib.error.HTTPError is an OSError subclass, so a 429/403 rate-limit
# response is otherwise indistinguishable from a report that simply does not
# exist. A throttled run must not look like a clean sync over a small corpus.
MAX_FAILURE_RATE = 0.10

Fetcher = Callable[[str], bytes]


@dataclass(frozen=True)
class SyncResult:
    fetched: int
    skipped: int
    failed: int
    index_path: Path
    bootstrapped: int = 0


def http_fetch(url: str) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=120) as response:
        return response.read()


def bootstrap_corpus(reports_dir: Path, fetch: Fetcher = http_fetch) -> int:
    """Populate the mirror from a single tarball request. Returns files written.

    Existing files are never overwritten, so this composes with the
    incremental per-file path rather than replacing it.
    """
    written = 0
    blob = fetch(TARBALL_URL)
    with tarfile.open(fileobj=io.BytesIO(blob), mode="r:gz") as archive:
        for member in archive:
            if not member.isfile():
                continue
            match = _REPORT_MEMBER.search(member.name)
            if not match:
                continue
            target = reports_dir / f"{match.group(1)}.md"
            if target.exists():
                continue
            handle = archive.extractfile(member)
            if handle is None:
                continue
            target.write_bytes(handle.read())
            written += 1
    return written


def sync_corpus(
    dest: Path,
    fetch: Fetcher = http_fetch,
    limit: int | None = None,
) -> SyncResult:
    reports_dir = dest / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)

    index_bytes = fetch(INDEX_URL)
    index_path = dest / "index.json"
    index_path.write_bytes(index_bytes)
    index = json.loads(index_bytes)

    # A cold start pulls the whole corpus in one request. Skipped when `limit`
    # is set, because --limit exists to make a cheap smoke run and
    # bootstrapping everything would defeat it.
    bootstrapped = 0
    if limit is None:
        missing = sum(
            1 for record in index if not (reports_dir / f"{record['id']}.md").exists()
        )
        if missing > BOOTSTRAP_THRESHOLD:
            try:
                bootstrapped = bootstrap_corpus(reports_dir, fetch)
            except (OSError, tarfile.TarError):
                # The tarball is an optimisation, not a requirement; fall
                # through to the per-file path.
                bootstrapped = 0

    fetched = skipped = failed = 0
    for record in index:
        report_id = record["id"]
        target = reports_dir / f"{report_id}.md"
        if target.exists():
            skipped += 1
            continue
        if limit is not None and fetched >= limit:
            continue
        try:
            body = fetch(f"{BASE}/reports/{report_id}.md")
        except OSError:
            # Network and filesystem errors are transient and retried next run.
            # Programming errors in the fetcher surface loudly instead of being
            # silently swallowed (which would mask bugs in an empty result).
            failed += 1
            continue
        target.write_bytes(body)
        fetched += 1

    # Measured against the whole corpus, not just this run's attempts: once a
    # corpus has converged, the un-mirrored remainder is mostly permanent
    # 404s, so "failed / attempted" collapses to a number near 100% forever.
    # The property being guarded is "how much of the corpus is missing", and
    # that is a fraction of the index, not of what happened to need fetching
    # this run.
    if index and failed / len(index) > MAX_FAILURE_RATE:
        raise RuntimeError(
            f"corpus sync failed {failed} of {len(index)} reports "
            f"({failed / len(index):.0%}); refusing to continue with a partial corpus"
        )

    return SyncResult(
        fetched=fetched,
        # Files the bootstrap just wrote are seen as present by the loop
        # below, which would otherwise report them as both bootstrapped and
        # skipped. `skipped` means "already present before this run".
        skipped=skipped - bootstrapped,
        failed=failed,
        index_path=index_path,
        bootstrapped=bootstrapped,
    )
