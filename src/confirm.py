"""Stage 4 — confirm candidates, cached by content hash.

The cache is the reason a 15k-candidate backfill can crash and resume, and
the reason a daily run only pays for genuinely new candidates.
"""

import json
import sys
import threading
import time
from collections.abc import Callable
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from src.extractors.base import Candidate
from src.llm.provider import Verdict

# Smaller batches generate proportionally fewer output tokens and finish well
# inside the timeout; 25-candidate batches straddled it.
BATCH_SIZE = 10

# The endpoint is latency-bound, not throughput-bound: a 64-token request and a
# 25-candidate request both take roughly 40 seconds. Sequential batches used
# well under a tenth of the 40-requests-per-minute budget and put a
# 3,159-candidate backfill at nearly eight hours. Running several in flight
# turns latency into parallelism -- but only up to a point, and the limit is
# not the documented 40 RPM. Measured on a real batch: concurrency 1, 2 and 3
# all succeed (37, 46, 79 verdicts/min), while 6 timed out 84% of batches and
# tripped the failure-rate guard below. The endpoint degrades rather than
# returning 429, so the ceiling has to be found by measurement.
CONCURRENCY = 6

# Under concurrency "consecutive failures" is meaningless -- batches finish out
# of order -- so the guard is a failure RATE instead. A handful of transient
# blips never trips it; a broken provider or an expired key does.
MAX_BATCH_FAILURE_RATE = 0.5
MIN_BATCHES_FOR_RATE = 4
# Free tier is 40 RPM; one batch per 1.6s stays comfortably under it.
SECONDS_BETWEEN_BATCHES = 1.6
# A run that fails this many batches in a row is not hitting transient
# blips -- it is a broken provider, and must not be reported as a clean
# run that simply had nothing new to judge.
MAX_CONSECUTIVE_FAILURES = 5


def load_cache(path: Path) -> dict[str, Verdict]:
    if not path.exists():
        return {}
    cache: dict[str, Verdict] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError:
            continue
        # A line can be valid JSON yet still lack the fields a cache record
        # requires -- tolerate that the same way an unparseable line is
        # tolerated, rather than letting record["key"] abort the whole run.
        key = record.get("key")
        if key is None or "is_payload" not in record:
            continue
        cache[key] = Verdict(
            key=key,
            is_payload=record["is_payload"],
            technique=record.get("technique", ""),
            param=record.get("param"),
        )
    return cache


def append_cache(path: Path, verdicts: list[Verdict]) -> None:
    if not verdicts:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        for verdict in verdicts:
            handle.write(json.dumps({
                "key": verdict.key,
                "is_payload": verdict.is_payload,
                "technique": verdict.technique,
                "param": verdict.param,
            }) + "\n")


def confirm(
    candidates: list[Candidate],
    provider,
    cache_path: Path,
    batch_size: int = BATCH_SIZE,
    sleep: Callable[[float], None] = time.sleep,
    concurrency: int = CONCURRENCY,
) -> list[Verdict]:
    cache = load_cache(cache_path)
    seen: set[str] = set()
    pending: list[Candidate] = []
    for candidate in candidates:
        key = candidate.key()
        if key in cache or key in seen:
            continue
        seen.add(key)
        pending.append(candidate)

    batches = [pending[i:i + batch_size] for i in range(0, len(pending), batch_size)]
    lock = threading.Lock()
    state = {"attempted": 0, "failed": 0}

    def run(index: int, batch: list[Candidate]) -> None:
        # Stagger starts so a burst of threads does not arrive as one spike.
        if index and concurrency > 1:
            sleep(SECONDS_BETWEEN_BATCHES * (index % concurrency) / concurrency)
        try:
            verdicts = provider.judge(batch)
        except Exception as error:
            with lock:
                state["attempted"] += 1
                state["failed"] += 1
            # The exception TYPE is logged, never its message: the OpenAI SDK
            # builds exception messages from the server response body, so an
            # auth failure can carry the submitted API key. This runs in CI on
            # a public repository, where stderr is world-readable.
            print(f"confirm: batch {index} failed ({type(error).__name__})",
                  file=sys.stderr, flush=True)
            return

        with lock:
            state["attempted"] += 1
            if len(verdicts) < len(batch):
                # A partial answer leaves the unanswered keys uncached, so they
                # would be re-sent and re-paid on every future run.
                state["failed"] += 1
            append_cache(cache_path, verdicts)
            for verdict in verdicts:
                cache[verdict.key] = verdict

    with ThreadPoolExecutor(max_workers=max(1, concurrency)) as pool:
        list(pool.map(lambda pair: run(*pair), enumerate(batches)))

    attempted, failed = state["attempted"], state["failed"]
    if attempted and failed == attempted:
        raise RuntimeError(
            f"every one of {attempted} batches failed or returned nothing; "
            f"aborting rather than reporting a silent no-op run"
        )
    if attempted >= MIN_BATCHES_FOR_RATE and failed / attempted > MAX_BATCH_FAILURE_RATE:
        raise RuntimeError(
            f"{failed} of {attempted} batches failed ({failed / attempted:.0%}); "
            f"aborting rather than publishing from a half-judged run"
        )

    result = [cache[c.key()] for c in candidates if c.key() in cache]
    unjudged = len(candidates) - len(result)
    if unjudged:
        print(
            f"confirm: {unjudged} of {len(candidates)} candidates went unjudged "
            f"and will be retried on the next run",
            file=sys.stderr,
        )
    return result
