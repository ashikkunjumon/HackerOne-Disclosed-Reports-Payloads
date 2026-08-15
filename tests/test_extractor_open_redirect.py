from pathlib import Path

from src.extractors import EXTRACTORS
from src.extractors.open_redirect import extract

FIXTURE = Path("tests/fixtures/open_redirect_report.md").read_text()


def payloads():
    return [c.payload for c in extract(827052, FIXTURE)]


def test_finds_the_protocol_relative_payload():
    assert any("//evil.com" in p for p in payloads())


def test_finds_the_backslash_variant():
    assert any(r"/\/evil.com" in p for p in payloads())


def test_finds_the_userinfo_at_variant():
    assert any("target.com@evil.com" in p for p in payloads())


def test_every_candidate_carries_report_and_class():
    for candidate in extract(827052, FIXTURE):
        assert candidate.report_id == 827052
        assert candidate.cls == "open-redirect"
        assert candidate.extractor == "open_redirect"
        assert candidate.context


def test_registered_in_the_extractor_registry():
    assert EXTRACTORS["open-redirect"] is extract


def test_the_reference_url_decoy_is_not_a_candidate():
    # The fixture's OWASP cheat-sheet link is an ordinary reference. An
    # unanchored //host pattern matches the host part of every absolute
    # URL, which would flag a citation in almost every report.
    assert not any("cheatsheetseries.owasp.org" in p for p in payloads())
