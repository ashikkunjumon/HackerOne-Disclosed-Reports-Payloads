"""Stage 4 — LLM verdicts over extractor candidates.

NVIDIA's hosted endpoint is OpenAI-compatible, so the official client works
by swapping base_url. The prompt is deliberately narrow: the model filters
and summarises, it never does the recall work.
"""

import json
import os
import re
from dataclasses import dataclass

from src.extractors.base import Candidate

BASE_URL = "https://integrate.api.nvidia.com/v1"
# Chosen by measurement, not by catalogue listing. meta/llama-3.3-70b-instruct
# is listed but does not serve for this account -- it accepts the connection and
# returns nothing until timeout. Of the models that do respond, gpt-oss-20b kept
# every candidate including bare fragments like "../" and reused one technique
# sentence across unrelated payloads; gpt-oss-120b correctly rejected them. That
# discrimination is the whole reason this stage exists.
DEFAULT_MODEL = "openai/gpt-oss-120b"

# The SDK defaults to a 10-minute timeout with retries. An unattended daily run
# must not sit for half an hour on a model that has stopped responding -- which
# is exactly the failure mode observed on llama-3.3-70b.
# A 25-candidate batch generates ~2,500 output tokens and was measured at
# 45-120s. A 90s timeout killed the slow half mid-flight and the run counted
# them as failures, which read as throttling and made concurrency look like
# the culprit. Generous enough that a timeout means genuinely stuck.
REQUEST_TIMEOUT = 300.0
BATCH_SIZE = 10

SYSTEM = """You classify strings taken from public security reports.

For each item decide whether it is a PAYLOAD: a string an attacker supplies
to trigger the vulnerability. It is NOT a payload if it is any of these:
- vulnerable source code, or the patch that fixed it
- a server log line or an HTTP response body
- a plain reference or documentation URL
- prose describing the bug

If it is a payload, describe the technique in one sentence, naming the
mechanism rather than restating the string. If a request parameter carries
the payload, name it.

Reply with ONLY a JSON array, one object per item:
[{"index": 0, "is_payload": true, "technique": "...", "param": "next"}]
Use null for param when there is none. No prose outside the array."""

_FENCE = re.compile(r"```(?:json)?\s*(.*?)```", re.DOTALL)


@dataclass(frozen=True)
class Verdict:
    key: str
    is_payload: bool
    technique: str
    param: str | None


def build_prompt(batch: list[Candidate]) -> str:
    items = [
        {"index": i, "class": c.cls, "string": c.payload, "context": c.context}
        for i, c in enumerate(batch)
    ]
    return json.dumps(items, indent=2)


def parse_verdicts(raw: str | None, batch: list[Candidate]) -> list[Verdict]:
    # The SDK hands back None when a model returns no content -- some models
    # put their output in a separate reasoning field. Treat it as unparseable
    # rather than raising, which the caller would misread as a network failure.
    if not raw:
        return []
    text = raw.strip()
    fenced = _FENCE.search(text)
    if fenced:
        text = fenced.group(1).strip()
    if not text.startswith("["):
        start = text.find("[")
        if start == -1:
            return []
        text = text[start:]

    try:
        parsed = json.loads(text)
    except json.JSONDecodeError:
        return []
    if not isinstance(parsed, list):
        return []

    verdicts: list[Verdict] = []
    for entry in parsed:
        if not isinstance(entry, dict):
            continue
        index = entry.get("index")
        if not isinstance(index, int) or not 0 <= index < len(batch):
            continue
        verdicts.append(
            Verdict(
                key=batch[index].key(),
                is_payload=bool(entry.get("is_payload")),
                technique=(entry.get("technique") or "").strip(),
                param=entry.get("param") or None,
            )
        )
    return verdicts


class NvidiaProvider:
    def __init__(self, model: str = DEFAULT_MODEL, client=None):
        self.model = model
        if client is not None:
            self._client = client
        else:
            from openai import OpenAI

            key = os.environ.get("NVIDIA_API_KEY")
            if not key:
                raise RuntimeError("NVIDIA_API_KEY is not set")
            self._client = OpenAI(
                base_url=BASE_URL,
                api_key=key,
                timeout=REQUEST_TIMEOUT,
                max_retries=2,
            )

    def judge(self, batch: list[Candidate]) -> list[Verdict]:
        response = self._client.chat.completions.create(
            model=self.model,
            temperature=0,
            max_tokens=2048,
            messages=[
                {"role": "system", "content": SYSTEM},
                {"role": "user", "content": build_prompt(batch)},
            ],
        )
        return parse_verdicts(response.choices[0].message.content, batch)
