import json
from pathlib import Path

import pytest

from src.sync import sync_corpus


def make_fetch(index, bodies):
    calls = []

    def fetch(url: str) -> bytes:
        calls.append(url)
        if url.endswith("index.json"):
            return json.dumps(index).encode()
        report_id = int(url.rsplit("/", 1)[-1].removesuffix(".md"))
        return bodies[report_id].encode()

    fetch.calls = calls
    return fetch


def test_fetches_index_and_bodies(tmp_path):
    fetch = make_fetch([{"id": 1}, {"id": 2}], {1: "body one", 2: "body two"})
    result = sync_corpus(tmp_path, fetch=fetch)

    assert result.fetched == 2
    assert (tmp_path / "reports" / "1.md").read_text() == "body one"
    assert json.loads(result.index_path.read_text()) == [{"id": 1}, {"id": 2}]


def test_skips_already_mirrored_reports(tmp_path):
    fetch = make_fetch([{"id": 1}, {"id": 2}], {1: "body one", 2: "body two"})
    sync_corpus(tmp_path, fetch=fetch)

    second = make_fetch([{"id": 1}, {"id": 2}], {1: "body one", 2: "body two"})
    result = sync_corpus(tmp_path, fetch=second)

    assert result.fetched == 0
    assert result.skipped == 2
    assert not [u for u in second.calls if u.endswith(".md")]


def test_limit_caps_new_fetches(tmp_path):
    fetch = make_fetch([{"id": 1}, {"id": 2}, {"id": 3}], {1: "a", 2: "b", 3: "c"})
    result = sync_corpus(tmp_path, fetch=fetch, limit=2)
    assert result.fetched == 2


def test_a_failed_body_fetch_does_not_abort_the_run(tmp_path):
    # A single genuine transient failure out of only two attempts is a 50%
    # failure rate, which the C1 abort guard (rightly) treats as a broken
    # sync rather than noise -- so this needs a corpus large enough that one
    # miss stays under MAX_FAILURE_RATE, same as a realistic daily run.
    def fetch(url: str) -> bytes:
        if url.endswith("index.json"):
            return json.dumps([{"id": i} for i in range(1, 21)]).encode()
        if url.endswith("/1.md"):
            raise OSError("transient")
        return f"body {url}".encode()

    result = sync_corpus(tmp_path, fetch=fetch)
    assert result.fetched == 19
    assert result.failed == 1
    assert not (tmp_path / "reports" / "1.md").exists()
    assert (tmp_path / "reports" / "2.md").exists()


def test_a_high_body_failure_rate_aborts_the_sync(tmp_path):
    def fetch(url: str) -> bytes:
        if url.endswith("index.json"):
            return json.dumps([{"id": i} for i in range(20)]).encode()
        raise OSError("429 throttled")

    with pytest.raises(RuntimeError, match="refusing to continue"):
        sync_corpus(tmp_path, fetch=fetch)


def test_a_few_missing_reports_do_not_abort(tmp_path):
    def fetch(url: str) -> bytes:
        if url.endswith("index.json"):
            return json.dumps([{"id": i} for i in range(20)]).encode()
        if url.endswith("/3.md"):
            raise OSError("gone")
        return b"body"

    result = sync_corpus(tmp_path, fetch=fetch)
    assert result.fetched == 19
    assert result.failed == 1


def test_a_converged_corpus_does_not_abort_on_a_few_permanent_404s(tmp_path):
    # The guard asks "what fraction of the corpus is missing", not "what
    # fraction of this run's attempts missed" -- otherwise a converged corpus
    # aborts forever, because the only fetches left to attempt are the dead ones.
    index = [{"id": i} for i in range(100)]

    def fetch(url: str) -> bytes:
        if url.endswith("index.json"):
            return json.dumps(index).encode()
        # "/3.md"/"/7.md" (with the leading slash) match only the single-digit
        # ids 3 and 7 -- "13.md"/"73.md" etc. end in "3.md" but not "/3.md".
        if url.endswith(("/3.md", "/7.md")):
            raise OSError("404")
        return b"body"

    first = sync_corpus(tmp_path, fetch=fetch)
    assert first.failed == 2
    second = sync_corpus(tmp_path, fetch=fetch)   # must not raise
    assert second.failed == 2
    assert second.skipped == 98


def test_a_small_increment_over_a_mirrored_corpus_does_not_abort(tmp_path):
    index = [{"id": i} for i in range(100)]

    def fetch(url: str) -> bytes:
        if url.endswith("index.json"):
            return json.dumps(index).encode()
        if url.endswith("99.md"):
            raise OSError("404")
        return b"body"

    sync_corpus(tmp_path, fetch=fetch)
    result = sync_corpus(tmp_path, fetch=fetch)   # must not raise
    assert result.failed == 1


def test_a_programming_error_in_the_fetcher_is_not_swallowed(tmp_path):
    # A bug in the fetcher must surface loudly. Silently skipping every
    # report and reporting success is the failure mode this guards.
    def fetch(url: str) -> bytes:
        if url.endswith("index.json"):
            return json.dumps([{"id": 1}]).encode()
        raise TypeError("bug in the fetcher")

    with pytest.raises(TypeError):
        sync_corpus(tmp_path, fetch=fetch)


# --- tarball bootstrap -------------------------------------------------------
#
# A cold start needs ~10k report bodies. One request per report takes over an
# hour and invites the throttling that MAX_FAILURE_RATE then correctly aborts
# on -- so in CI, where the mirror starts empty every run, the per-file path
# would fail every day. The whole corpus is one 12MB download.

import io
import tarfile

from src.sync import BOOTSTRAP_THRESHOLD, TARBALL_URL, bootstrap_corpus


def make_tarball(ids, extra_members=()):
    buf = io.BytesIO()
    with tarfile.open(fileobj=buf, mode="w:gz") as archive:
        for report_id in ids:
            data = f"body {report_id}".encode()
            info = tarfile.TarInfo(f"HackerOne-Disclosed-Reports-main/reports/{report_id}.md")
            info.size = len(data)
            archive.addfile(info, io.BytesIO(data))
        for name, data in extra_members:
            info = tarfile.TarInfo(name)
            info.size = len(data)
            archive.addfile(info, io.BytesIO(data))
    return buf.getvalue()


def test_bootstrap_extracts_report_bodies(tmp_path):
    reports = tmp_path / "reports"
    reports.mkdir()
    written = bootstrap_corpus(reports, fetch=lambda url: make_tarball([1, 2, 3]))
    assert written == 3
    assert (reports / "2.md").read_text() == "body 2"


def test_bootstrap_ignores_members_outside_reports(tmp_path):
    # A crafted member name must not escape the reports directory. The target
    # path is built from the captured id, never from the archive's own path.
    reports = tmp_path / "reports"
    reports.mkdir()
    evil = [
        ("../../../../tmp/pwned.md", b"nope"),
        ("HackerOne-Disclosed-Reports-main/reports/../../pwned.md", b"nope"),
        ("HackerOne-Disclosed-Reports-main/README.md", b"nope"),
    ]
    written = bootstrap_corpus(reports, fetch=lambda url: make_tarball([1], extra_members=evil))
    assert written == 1
    assert sorted(p.name for p in reports.iterdir()) == ["1.md"]
    assert not (tmp_path.parent / "pwned.md").exists()


def test_bootstrap_does_not_overwrite_existing_reports(tmp_path):
    reports = tmp_path / "reports"
    reports.mkdir()
    (reports / "1.md").write_text("already here")
    written = bootstrap_corpus(reports, fetch=lambda url: make_tarball([1, 2]))
    assert written == 1
    assert (reports / "1.md").read_text() == "already here"


def test_a_cold_start_uses_the_tarball_instead_of_per_file_fetches(tmp_path):
    ids = list(range(BOOTSTRAP_THRESHOLD + 10))
    calls = []

    def fetch(url):
        calls.append(url)
        if url.endswith("index.json"):
            return json.dumps([{"id": i} for i in ids]).encode()
        if url == TARBALL_URL:
            return make_tarball(ids)
        raise AssertionError(f"unexpected per-file fetch: {url}")

    result = sync_corpus(tmp_path, fetch=fetch)
    assert result.bootstrapped == len(ids)
    assert result.fetched == 0
    assert calls.count(TARBALL_URL) == 1
    assert not [u for u in calls if u.endswith(".md")]


def test_a_small_gap_does_not_trigger_the_tarball(tmp_path):
    ids = list(range(5))
    calls = []

    def fetch(url):
        calls.append(url)
        if url.endswith("index.json"):
            return json.dumps([{"id": i} for i in ids]).encode()
        if url == TARBALL_URL:
            raise AssertionError("should not bootstrap for a small gap")
        return b"body"

    result = sync_corpus(tmp_path, fetch=fetch)
    assert result.fetched == 5
    assert result.bootstrapped == 0


def test_limit_disables_the_bootstrap(tmp_path):
    # --limit exists to make a cheap smoke run; bootstrapping the whole corpus
    # would defeat it.
    ids = list(range(BOOTSTRAP_THRESHOLD + 10))

    def fetch(url):
        if url.endswith("index.json"):
            return json.dumps([{"id": i} for i in ids]).encode()
        if url == TARBALL_URL:
            raise AssertionError("limit must disable the bootstrap")
        return b"body"

    result = sync_corpus(tmp_path, fetch=fetch, limit=3)
    assert result.fetched == 3
    assert result.bootstrapped == 0


def test_a_failed_tarball_falls_back_to_per_file(tmp_path):
    # The tarball is an optimisation, not a requirement.
    ids = list(range(BOOTSTRAP_THRESHOLD + 5))

    def fetch(url):
        if url.endswith("index.json"):
            return json.dumps([{"id": i} for i in ids]).encode()
        if url == TARBALL_URL:
            raise OSError("tarball unavailable")
        return b"body"

    result = sync_corpus(tmp_path, fetch=fetch)
    assert result.bootstrapped == 0
    assert result.fetched == len(ids)


def test_bootstrapped_reports_are_not_also_counted_as_skipped(tmp_path):
    # The loop sees files the bootstrap just wrote as already present, which
    # would otherwise report the same report twice and double the total.
    ids = list(range(BOOTSTRAP_THRESHOLD + 10))

    def fetch(url):
        if url.endswith("index.json"):
            return json.dumps([{"id": i} for i in ids]).encode()
        if url == TARBALL_URL:
            return make_tarball(ids)
        raise AssertionError("no per-file fetch expected")

    result = sync_corpus(tmp_path, fetch=fetch)
    assert result.bootstrapped == len(ids)
    assert result.skipped == 0
    assert result.bootstrapped + result.fetched + result.skipped == len(ids)
