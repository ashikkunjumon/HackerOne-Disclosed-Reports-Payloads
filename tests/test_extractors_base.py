from src.extractors.base import (
    Candidate,
    code_blocks,
    inline_code,
    regions,
    repro_lines,
    scan,
    urls,
)

MD = """
Some prose here.

```
GET /redirect?url=//evil.com HTTP/1.1
```

Inline `//evil.com` mention and a link https://target.com/a?next=//evil.com here.
"""


def test_code_blocks_returns_fence_contents():
    blocks = code_blocks(MD)
    assert len(blocks) == 1
    assert "GET /redirect?url=//evil.com" in blocks[0][0]


def test_inline_code_returns_backtick_spans():
    spans = [text for text, _ in inline_code(MD)]
    assert "//evil.com" in spans


def test_urls_returns_bare_links():
    found = [text for text, _ in urls(MD)]
    assert any("target.com" in u for u in found)


def test_context_is_bounded():
    for _, context in code_blocks(MD) + inline_code(MD) + urls(MD):
        assert len(context) <= 400


def test_candidate_key_is_stable_and_content_addressed():
    a = Candidate(1, "xss", "<svg onload=1>", "ctx", "xss")
    b = Candidate(999, "sqli", "<svg onload=1>", "ctx", "other")
    c = Candidate(1, "xss", "<img src=x>", "ctx", "xss")
    assert a.key() == b.key()
    assert a.key() != c.key()


def test_scan_matches_patterns_and_deduplicates():
    found = scan(MD, report_id=7, cls="open-redirect", extractor="open_redirect",
                 patterns=(r"//evil\.com",))
    assert found
    assert all(c.report_id == 7 and c.cls == "open-redirect" for c in found)
    assert len({c.key() for c in found}) == len(found)


def test_regions_claims_each_piece_of_text_once():
    # The URL inside the fenced block must not also be returned by the
    # URL walker; the fence already claimed it.
    found = regions(MD)
    from_url_walker = [t for t, _ in found if t.startswith("https://target.com")]
    assert len(from_url_walker) == 1


def test_scan_does_not_emit_the_same_payload_three_times():
    found = scan(MD, report_id=7, cls="open-redirect", extractor="open_redirect",
                 patterns=(r"//evil\.com",))
    payloads = [c.payload for c in found]
    assert len(payloads) == len(set(payloads))


REPRO_MD = """
## Summary

Some narrative prose mentioning <svg onload=alert(1)> that is NOT a repro step.

## Steps to reproduce

1. Log in as a normal user.
2. Enter <img src=x onerror=alert(1)> into the display-name field.
3. Observe the alert.

## Impact

More narrative prose with <script>alert(2)</script> in it.
"""


def test_repro_lines_finds_payloads_written_as_prose():
    found = [text for text, _ in repro_lines(REPRO_MD)]
    assert any("onerror=alert(1)" in t for t in found)


def test_repro_lines_ignores_prose_outside_a_repro_section():
    found = " ".join(text for text, _ in repro_lines(REPRO_MD))
    assert "onload=alert(1)" not in found      # under Summary
    assert "alert(2)" not in found             # under Impact


def test_repro_lines_stops_at_the_next_heading():
    found = [text for text, _ in repro_lines(REPRO_MD)]
    assert not any(t.startswith("##") for t in found)


def test_regions_includes_repro_prose_without_double_claiming():
    from src.extractors.xss import extract
    payloads = [c.payload for c in extract(1, REPRO_MD)]
    assert any("onerror=alert(1)" in p for p in payloads)
    assert len(payloads) == len(set(payloads))
