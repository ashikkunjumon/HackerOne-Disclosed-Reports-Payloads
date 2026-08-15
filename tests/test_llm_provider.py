import json

from src.extractors.base import Candidate
from src.llm.provider import (
    BASE_URL,
    DEFAULT_MODEL,
    NvidiaProvider,
    Verdict,
    build_prompt,
    parse_verdicts,
)

BATCH = [
    Candidate(1, "open-redirect", "//evil.com", "?next=//evil.com", "open_redirect"),
    Candidate(1, "open-redirect", "def is_safe(url):", "vulnerable code", "open_redirect"),
]


def test_endpoint_and_model_are_the_verified_values():
    assert BASE_URL == "https://integrate.api.nvidia.com/v1"
    assert DEFAULT_MODEL == "openai/gpt-oss-120b"


def test_prompt_contains_every_candidate_and_its_index():
    prompt = build_prompt(BATCH)
    assert "//evil.com" in prompt and "def is_safe(url):" in prompt
    assert '"index": 0' in prompt or "index 0" in prompt


def test_parse_maps_verdicts_back_onto_candidate_keys():
    raw = json.dumps([
        {"index": 0, "is_payload": True, "technique": "Protocol-relative redirect.", "param": "next"},
        {"index": 1, "is_payload": False, "technique": "", "param": None},
    ])
    verdicts = parse_verdicts(raw, BATCH)
    assert [v.key for v in verdicts] == [c.key() for c in BATCH]
    assert verdicts[0].is_payload is True
    assert verdicts[0].param == "next"
    assert verdicts[1].is_payload is False


def test_parse_tolerates_a_fenced_json_response():
    raw = '```json\n[{"index": 0, "is_payload": true, "technique": "t", "param": null}]\n```'
    verdicts = parse_verdicts(raw, BATCH[:1])
    assert verdicts[0].is_payload is True


def test_parse_fails_closed_on_unparseable_output():
    assert parse_verdicts("the model rambled instead", BATCH) == []


def test_parse_ignores_out_of_range_indexes():
    raw = json.dumps([{"index": 99, "is_payload": True, "technique": "t", "param": None}])
    assert parse_verdicts(raw, BATCH) == []


def test_judge_uses_the_injected_client():
    class FakeCompletions:
        def create(self, **kwargs):
            self.kwargs = kwargs
            payload = json.dumps([
                {"index": 0, "is_payload": True, "technique": "Protocol-relative.", "param": "next"},
                {"index": 1, "is_payload": False, "technique": "", "param": None},
            ])
            return type("R", (), {
                "choices": [type("C", (), {"message": type("M", (), {"content": payload})()})()]
            })()

    class FakeClient:
        def __init__(self):
            self.chat = type("Chat", (), {"completions": FakeCompletions()})()

    client = FakeClient()
    verdicts = NvidiaProvider(client=client).judge(BATCH)
    assert len(verdicts) == 2
    assert verdicts[0].is_payload and not verdicts[1].is_payload
    assert client.chat.completions.kwargs["model"] == DEFAULT_MODEL


def test_a_null_content_response_does_not_crash():
    # The SDK returns message.content = None when a model puts its output in
    # another field or returns nothing. .strip() on None raised AttributeError
    # and killed the batch, which the run then counted as a network failure.
    class FakeCompletions:
        def create(self, **kwargs):
            return type("R", (), {
                "choices": [type("C", (), {"message": type("M", (), {"content": None})()})()]
            })()

    class FakeClient:
        def __init__(self):
            self.chat = type("Chat", (), {"completions": FakeCompletions()})()

    assert NvidiaProvider(client=FakeClient()).judge(BATCH) == []


def test_parse_verdicts_tolerates_none():
    assert parse_verdicts(None, BATCH) == []
