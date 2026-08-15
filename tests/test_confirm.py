import json
from pathlib import Path

import pytest

from src.confirm import append_cache, confirm, load_cache
from src.extractors.base import Candidate
from src.llm.provider import Verdict


def make_candidates(n):
    return [Candidate(i, "xss", f"<svg onload={i}>", f"ctx{i}", "xss") for i in range(n)]


class RecordingProvider:
    def __init__(self):
        self.batches = []

    def judge(self, batch):
        self.batches.append(list(batch))
        return [Verdict(c.key(), True, "technique", None) for c in batch]


def test_cache_round_trips(tmp_path):
    path = tmp_path / "verdicts.jsonl"
    append_cache(path, [Verdict("abc", True, "t", "next")])
    cache = load_cache(path)
    assert cache["abc"].technique == "t"
    assert cache["abc"].param == "next"


def test_missing_cache_file_is_empty(tmp_path):
    assert load_cache(tmp_path / "nope.jsonl") == {}


def test_a_valid_json_line_missing_required_fields_is_skipped(tmp_path):
    path = tmp_path / "v.jsonl"
    path.write_text('{"unrelated": true}\n{"key": "abc", "is_payload": true}\n')
    cache = load_cache(path)
    assert "abc" in cache
    assert len(cache) == 1


def test_only_uncached_candidates_reach_the_provider(tmp_path):
    path = tmp_path / "verdicts.jsonl"
    candidates = make_candidates(3)
    append_cache(path, [Verdict(candidates[0].key(), True, "cached", None)])

    provider = RecordingProvider()
    verdicts = confirm(candidates, provider, path, sleep=lambda _: None)

    judged = [c.key() for b in provider.batches for c in b]
    assert candidates[0].key() not in judged
    assert len(verdicts) == 3


def test_a_second_run_costs_nothing(tmp_path):
    path = tmp_path / "verdicts.jsonl"
    candidates = make_candidates(5)
    confirm(candidates, RecordingProvider(), path, sleep=lambda _: None)

    second = RecordingProvider()
    verdicts = confirm(candidates, second, path, sleep=lambda _: None)
    assert second.batches == []
    assert len(verdicts) == 5


def test_candidates_are_batched(tmp_path):
    provider = RecordingProvider()
    confirm(make_candidates(25), provider, tmp_path / "v.jsonl", batch_size=10, sleep=lambda _: None)
    assert [len(b) for b in provider.batches] == [10, 10, 5]


def test_a_failing_batch_does_not_lose_earlier_progress(tmp_path):
    path = tmp_path / "verdicts.jsonl"

    class FlakyProvider:
        def __init__(self):
            self.calls = 0

        def judge(self, batch):
            self.calls += 1
            if self.calls == 2:
                raise RuntimeError("rate limited")
            return [Verdict(c.key(), True, "t", None) for c in batch]

    confirm(make_candidates(25), FlakyProvider(), path, batch_size=10, sleep=lambda _: None)
    # The first and third batches persisted despite the middle one failing.
    assert len(load_cache(path)) == 15


def test_a_persistently_failing_provider_aborts_loudly(tmp_path):
    # A provider that always fails must not look like a clean run over an
    # empty queue -- that is the failure mode that hides a broken backfill.
    class AlwaysFails:
        def judge(self, batch):
            raise RuntimeError("auth rejected")

    with pytest.raises(RuntimeError, match="every one of"):
        confirm(make_candidates(100), AlwaysFails(), tmp_path / "v.jsonl",
                batch_size=10, sleep=lambda _: None)


def test_scattered_failures_do_not_trip_the_abort(tmp_path):
    class Flaky:
        def __init__(self):
            self.calls = 0

        def judge(self, batch):
            self.calls += 1
            if self.calls % 2 == 0:
                raise RuntimeError("transient")
            return [Verdict(c.key(), True, "t", None) for c in batch]

    verdicts = confirm(make_candidates(100), Flaky(), tmp_path / "v.jsonl",
                       batch_size=10, sleep=lambda _: None)
    assert verdicts  # alternating failures must not abort the run


def test_duplicate_candidates_are_judged_once(tmp_path):
    candidate = make_candidates(1)[0]
    provider = RecordingProvider()
    confirm([candidate, candidate, candidate], provider, tmp_path / "v.jsonl",
            sleep=lambda _: None)
    judged = [c.key() for b in provider.batches for c in b]
    assert len(judged) == 1


def test_every_input_candidate_still_gets_a_verdict_back(tmp_path):
    candidate = make_candidates(1)[0]
    verdicts = confirm([candidate, candidate], RecordingProvider(),
                       tmp_path / "v.jsonl", sleep=lambda _: None)
    assert len(verdicts) == 2   # deduped for billing, expanded for the caller


def test_a_small_run_where_every_batch_fails_aborts(tmp_path):
    class AlwaysFails:
        def judge(self, batch):
            raise RuntimeError("auth rejected")

    with pytest.raises(RuntimeError, match="every one of"):
        confirm(make_candidates(30), AlwaysFails(), tmp_path / "v.jsonl",
                batch_size=10, sleep=lambda _: None)


def test_a_provider_returning_no_verdicts_is_treated_as_failure(tmp_path):
    class ReturnsNothing:
        def judge(self, batch):
            return []

    with pytest.raises(RuntimeError):
        confirm(make_candidates(30), ReturnsNothing(), tmp_path / "v.jsonl",
                batch_size=10, sleep=lambda _: None)


def test_a_partial_response_still_caches_what_it_got(tmp_path):
    # A provider that answers only part of EVERY batch is a broken response
    # format, so the run aborts rather than publishing from it -- but whatever
    # did come back must still be persisted, or the next run re-pays for it.
    class Partial:
        def judge(self, batch):
            return [Verdict(c.key(), True, "t", None) for c in batch[:5]]

    path = tmp_path / "v.jsonl"
    with pytest.raises(RuntimeError):
        confirm(make_candidates(10), Partial(), path, batch_size=10, sleep=lambda _: None)
    assert len(load_cache(path)) == 5


def test_an_occasional_partial_response_does_not_abort(tmp_path):
    class MostlyFine:
        def __init__(self):
            self.calls = 0

        def judge(self, batch):
            self.calls += 1
            keep = batch if self.calls != 2 else batch[:2]
            return [Verdict(c.key(), True, "t", None) for c in keep]

    verdicts = confirm(make_candidates(100), MostlyFine(), tmp_path / "v.jsonl",
                       batch_size=10, sleep=lambda _: None)
    assert len(verdicts) >= 90


def test_batch_failure_log_never_echoes_the_exception_message(tmp_path, capsys):
    # The OpenAI SDK builds exception messages from the server response body,
    # so an auth failure can carry the API key. This runs in CI on a public
    # repository. Log the type, never the message.
    secret = "nv" + "api-" + "s3cr3t0000000000000000000000000000000000"

    class LeakyProvider:
        def judge(self, batch):
            raise RuntimeError(f"401 Unauthorized: key {secret} rejected")

    try:
        confirm(make_candidates(10), LeakyProvider(), tmp_path / "v.jsonl",
                batch_size=10, sleep=lambda _: None)
    except RuntimeError:
        pass

    captured = capsys.readouterr()
    assert secret not in captured.err
    assert secret not in captured.out
    assert "RuntimeError" in captured.err


# --- concurrency --------------------------------------------------------------
#
# The endpoint is latency-bound, not throughput-bound: a 64-token request and a
# 25-candidate request both take ~40s. Sequential batches used 0.7 of a 40 RPM
# budget and put the backfill at 7.7 hours.

import threading


def test_batches_run_concurrently(tmp_path):
    seen = []
    barrier = threading.Barrier(3, timeout=5)

    class ConcurrentProvider:
        def judge(self, batch):
            seen.append(threading.current_thread().name)
            barrier.wait()          # deadlocks unless 3 batches are in flight
            return [Verdict(c.key(), True, "t", None) for c in batch]

    confirm(make_candidates(30), ConcurrentProvider(), tmp_path / "v.jsonl",
            batch_size=10, concurrency=3, sleep=lambda _: None)
    assert len(set(seen)) >= 2


def test_concurrent_writes_do_not_corrupt_the_cache(tmp_path):
    class Provider:
        def judge(self, batch):
            return [Verdict(c.key(), True, "technique", None) for c in batch]

    path = tmp_path / "v.jsonl"
    candidates = make_candidates(200)
    confirm(candidates, Provider(), path, batch_size=10, concurrency=8, sleep=lambda _: None)
    cache = load_cache(path)
    assert len(cache) == 200
    for line in path.read_text().splitlines():
        assert json.loads(line)["key"]      # every line is intact JSON


def test_every_candidate_still_gets_a_verdict_under_concurrency(tmp_path):
    class Provider:
        def judge(self, batch):
            return [Verdict(c.key(), True, "t", None) for c in batch]

    verdicts = confirm(make_candidates(55), Provider(), tmp_path / "v.jsonl",
                       batch_size=10, concurrency=4, sleep=lambda _: None)
    assert len(verdicts) == 55


def test_the_all_failed_guard_still_fires_under_concurrency(tmp_path):
    class AlwaysFails:
        def judge(self, batch):
            raise RuntimeError("auth rejected")

    with pytest.raises(RuntimeError):
        confirm(make_candidates(40), AlwaysFails(), tmp_path / "v.jsonl",
                batch_size=10, concurrency=4, sleep=lambda _: None)
