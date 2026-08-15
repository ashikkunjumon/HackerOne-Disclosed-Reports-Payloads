import json
from pathlib import Path

from src.config import load_classes
from src.emit import build_records, emit
from src.extractors.base import Candidate
from src.llm.provider import Verdict

CLASSES = load_classes()

CANDIDATES = [
    Candidate(827052, "open-redirect", "//evil.com", "?next=//evil.com", "open_redirect"),
    Candidate(827052, "open-redirect", "def is_safe(url):", "vulnerable code", "open_redirect"),
]

INDEX = {
    827052: {
        "id": 827052,
        "url": "https://hackerone.com/reports/827052",
        "title": "Open redirect in callback",
        "program": "GitLab",
        "reporter": "vakzz",
        "severity": "critical",
        "bounty": 20000,
        "disclosed_at": "2020-04-27",
    }
}


def verdicts():
    return [
        Verdict(CANDIDATES[0].key(), True, "Protocol-relative redirect.", "next"),
        Verdict(CANDIDATES[1].key(), False, "", None),
    ]


def test_rejected_candidates_are_excluded():
    records = build_records(CANDIDATES, verdicts(), INDEX, CLASSES)
    assert len(records) == 1
    assert records[0]["payload"] == "//evil.com"


def test_records_carry_full_provenance():
    record = build_records(CANDIDATES, verdicts(), INDEX, CLASSES)[0]
    for field in ("id", "url", "title", "program", "reporter", "severity", "bounty", "disclosed_at"):
        assert field in record["report"], field
    assert record["technique"] == "Protocol-relative redirect."
    assert record["param"] == "next"


def test_records_are_redacted():
    # Assembled at runtime, never a literal — see the note in tests/test_redact.py.
    fake_aws = "AK" + "IA" + "IOSFODNN7EXAMPLE"
    leaky = [Candidate(827052, "open-redirect", f"token={fake_aws}", "ctx", "open_redirect")]
    v = [Verdict(leaky[0].key(), True, "t", None)]
    records = build_records(leaky, v, INDEX, CLASSES)
    assert all(fake_aws not in r["payload"] for r in records)


def test_emit_writes_every_artifact(tmp_path):
    records = build_records(CANDIDATES, verdicts(), INDEX, CLASSES)
    emit(records, CLASSES, tmp_path)

    assert json.loads((tmp_path / "payloads.json").read_text())
    assert (tmp_path / "payloads.txt").read_text().strip()
    assert "//evil.com" in (tmp_path / "payloads" / "open-redirect.md").read_text()
    assert (tmp_path / "wordlists" / "open-redirect.txt").read_text().strip() == "//evil.com"
    assert "GitLab" in (tmp_path / "by-program" / "gitlab.md").read_text()
    assert (tmp_path / "top-payloads" / "by-bounty.md").exists()
    assert "Last Updated" in (tmp_path / "README.md").read_text()


def test_markdown_carries_the_report_link(tmp_path):
    emit(build_records(CANDIDATES, verdicts(), INDEX, CLASSES), CLASSES, tmp_path)
    page = (tmp_path / "payloads" / "open-redirect.md").read_text()
    assert "https://hackerone.com/reports/827052" in page
    assert "vakzz" in page


def test_wordlists_are_deduplicated(tmp_path):
    dupes = [
        Candidate(827052, "open-redirect", "//evil.com", "ctx-a", "open_redirect"),
        Candidate(827052, "open-redirect", "//evil.com", "ctx-b", "open_redirect"),
    ]
    v = [Verdict(c.key(), True, "t", None) for c in dupes]
    emit(build_records(dupes, v, INDEX, CLASSES), CLASSES, tmp_path)
    lines = (tmp_path / "wordlists" / "open-redirect.txt").read_text().split()
    assert lines == ["//evil.com"]


def test_a_secret_in_the_technique_text_is_redacted():
    # The model sees the unredacted payload and context, so its description
    # can quote a secret. That text is published verbatim otherwise.
    fake_aws = "AK" + "IA" + "IOSFODNN7EXAMPLE"
    v = [Verdict(CANDIDATES[0].key(), True, f"Supplies the key {fake_aws} as next.", "next")]
    records = build_records(CANDIDATES[:1], v, INDEX, CLASSES)
    assert records
    assert fake_aws not in records[0]["technique"]


def test_a_record_is_dropped_when_its_technique_cannot_be_cleared(tmp_path):
    blob = "Zx9Kq2Lm8Rt4Wv7Yb1Nc6Ho3Pj5Sd0Fg" * 4
    v = [Verdict(CANDIDATES[0].key(), True, f"Leaks {blob} to the attacker.", None)]
    assert build_records(CANDIDATES[:1], v, INDEX, CLASSES) == []


def test_a_secret_never_reaches_the_written_markdown(tmp_path):
    fake_aws = "AK" + "IA" + "IOSFODNN7EXAMPLE"
    v = [Verdict(CANDIDATES[0].key(), True, f"Uses {fake_aws} here.", "next")]
    emit(build_records(CANDIDATES[:1], v, INDEX, CLASSES), CLASSES, tmp_path)
    blob = "\n".join(p.read_text() for p in tmp_path.rglob("*") if p.is_file())
    assert fake_aws not in blob


def test_slugify_bounds_the_filename_length():
    from src.emit import MAX_SLUG, _slugify
    assert len(_slugify("A" * 5000)) <= MAX_SLUG


def test_slugify_leaves_no_trailing_separator_after_truncation():
    from src.emit import _slugify
    assert not _slugify(("word " * 200)).endswith("-")


def test_slugify_still_blocks_traversal_and_control_characters():
    from src.emit import _slugify
    assert "/" not in _slugify("../../etc/passwd")
    assert ".." not in _slugify("../../etc/passwd")
    assert "\x00" not in _slugify("prog\x00ram")
    assert _slugify("") == "unknown"


def test_emit_survives_an_absurd_program_name(tmp_path):
    # Reachable input: the program field comes from corpus data.
    index = {827052: dict(INDEX[827052], program="X" * 5000)}
    records = build_records(CANDIDATES[:1], [Verdict(CANDIDATES[0].key(), True, "t", None)],
                            index, CLASSES)
    emit(records, CLASSES, tmp_path)
    assert list((tmp_path / "by-program").glob("*.md"))


def test_a_secret_in_a_report_title_is_redacted():
    fake_aws = "AK" + "IA" + "IOSFODNN7EXAMPLE"
    index = {827052: dict(INDEX[827052], title=f"XXE leaking {fake_aws} from prod")}
    records = build_records(CANDIDATES[:1], [Verdict(CANDIDATES[0].key(), True, "t", None)],
                            index, CLASSES)
    assert records
    assert fake_aws not in records[0]["report"]["title"]


def test_an_internal_hostname_in_a_title_is_normalised():
    index = {827052: dict(INDEX[827052], title="Bug on https://internal.corp.acme.io/admin")}
    records = build_records(CANDIDATES[:1], [Verdict(CANDIDATES[0].key(), True, "t", None)],
                            index, CLASSES)
    assert "internal.corp.acme.io" not in records[0]["report"]["title"]


def test_an_uncleanable_title_does_not_discard_the_payload():
    blob = "Zx9Kq2Lm8Rt4Wv7Yb1Nc6Ho3Pj5Sd0Fg" * 4
    index = {827052: dict(INDEX[827052], title=f"Leak {blob}")}
    records = build_records(CANDIDATES[:1], [Verdict(CANDIDATES[0].key(), True, "t", None)],
                            index, CLASSES)
    assert len(records) == 1
    assert records[0]["report"]["title"] == "[redacted]"


def test_no_secret_from_a_title_reaches_any_written_file(tmp_path):
    fake_aws = "AK" + "IA" + "IOSFODNN7EXAMPLE"
    index = {827052: dict(INDEX[827052], title=f"XXE {fake_aws}", program=f"Acme {fake_aws}")}
    records = build_records(CANDIDATES[:1], [Verdict(CANDIDATES[0].key(), True, "t", None)],
                            index, CLASSES)
    emit(records, CLASSES, tmp_path)
    blob = "\n".join(p.read_text() for p in tmp_path.rglob("*") if p.is_file())
    assert fake_aws not in blob


def test_the_report_url_is_derived_not_redacted():
    index = {827052: dict(INDEX[827052], url="http://hackerone.com/reports/827052/")}
    records = build_records(CANDIDATES[:1], [Verdict(CANDIDATES[0].key(), True, "t", None)],
                            index, CLASSES)
    assert records[0]["report"]["url"] == "https://hackerone.com/reports/827052"


def test_a_title_with_brackets_does_not_corrupt_the_markdown_link(tmp_path):
    index = {827052: dict(INDEX[827052], title="XSS in [admin](panel) view")}
    records = build_records(CANDIDATES[:1], [Verdict(CANDIDATES[0].key(), True, "t", None)],
                            index, CLASSES)
    emit(records, CLASSES, tmp_path)
    page = (tmp_path / "payloads" / "open-redirect.md").read_text()
    assert "https://hackerone.com/reports/827052" in page


def test_multi_line_payloads_are_excluded_from_wordlists(tmp_path):
    multi = Candidate(827052, "xxe", '<?xml version="1.0"?>\n<!DOCTYPE foo>\n<foo/>',
                      "ctx", "xxe")
    records = build_records([multi], [Verdict(multi.key(), True, "t", None)], INDEX, CLASSES)
    emit(records, CLASSES, tmp_path)
    lines = (tmp_path / "wordlists" / "xxe.txt").read_text().splitlines()
    assert all(line.strip() for line in lines)
    assert not any(line.startswith("<?xml") for line in lines)


def test_multi_line_payloads_still_appear_in_json_and_markdown(tmp_path):
    multi = Candidate(827052, "xxe", '<?xml version="1.0"?>\n<!DOCTYPE foo>', "ctx", "xxe")
    records = build_records([multi], [Verdict(multi.key(), True, "t", None)], INDEX, CLASSES)
    emit(records, CLASSES, tmp_path)
    assert "<?xml" in (tmp_path / "payloads.json").read_text()
    assert "<?xml" in (tmp_path / "payloads" / "xxe.md").read_text()


def test_every_payloads_txt_line_carries_its_report_url(tmp_path):
    multi = Candidate(827052, "xxe", 'a\nb\nc', "ctx", "xxe")
    records = build_records([multi], [Verdict(multi.key(), True, "t", None)], INDEX, CLASSES)
    emit(records, CLASSES, tmp_path)
    for line in (tmp_path / "payloads.txt").read_text().splitlines():
        if line.strip():
            assert "\t" in line and "hackerone.com" in line


def test_readme_is_not_rewritten_when_nothing_changed(tmp_path):
    records = build_records(CANDIDATES, verdicts(), INDEX, CLASSES)
    emit(records, CLASSES, tmp_path)
    first = (tmp_path / "README.md").read_text()
    emit(records, CLASSES, tmp_path)
    assert (tmp_path / "README.md").read_text() == first


def test_readme_stamp_updates_when_content_changed(tmp_path):
    emit(build_records(CANDIDATES, verdicts(), INDEX, CLASSES), CLASSES, tmp_path)
    first = (tmp_path / "README.md").read_text()
    emit([], CLASSES, tmp_path)
    assert (tmp_path / "README.md").read_text() != first


def test_records_sharing_a_technique_appear_under_one_heading(tmp_path):
    shared = [
        Candidate(827052, "open-redirect", "//evil.com/one", "ctx1", "open_redirect"),
        Candidate(827052, "open-redirect", "//evil.com/two", "ctx2", "open_redirect"),
    ]
    v = [Verdict(c.key(), True, "Protocol-relative redirect.", None) for c in shared]
    emit(build_records(shared, v, INDEX, CLASSES), CLASSES, tmp_path)
    page = (tmp_path / "payloads" / "open-redirect.md").read_text()
    assert page.count("## Protocol-relative redirect.") == 1


def test_a_none_reporter_does_not_render_as_the_literal_string_none(tmp_path):
    index = {827052: dict(INDEX[827052], reporter=None)}
    records = build_records(CANDIDATES[:1], [Verdict(CANDIDATES[0].key(), True, "t", None)],
                            index, CLASSES)
    emit(records, CLASSES, tmp_path)
    page = (tmp_path / "payloads" / "open-redirect.md").read_text()
    assert "[None]" not in page
    assert "hackerone.com/None" not in page


def test_a_page_with_several_techniques_renders_several_headings(tmp_path):
    entries = [
        Candidate(827052, "open-redirect", "//evil.com/one", "ctx1", "open_redirect"),
        Candidate(827052, "open-redirect", "https://evil.com/two", "ctx2", "open_redirect"),
    ]
    v = [
        Verdict(entries[0].key(), True, "Protocol-relative redirect.", None),
        Verdict(entries[1].key(), True, "Absolute off-site redirect.", None),
    ]
    emit(build_records(entries, v, INDEX, CLASSES), CLASSES, tmp_path)
    page = (tmp_path / "payloads" / "open-redirect.md").read_text()
    assert "## Protocol-relative redirect." in page
    assert "## Absolute off-site redirect." in page


def test_the_technique_is_not_repeated_under_its_own_heading(tmp_path):
    # It is the group heading; printing it again in every entry body is noise.
    records = build_records(CANDIDATES[:1], [Verdict(CANDIDATES[0].key(), True,
                            "Protocol-relative redirect.", "next")], INDEX, CLASSES)
    emit(records, CLASSES, tmp_path)
    page = (tmp_path / "payloads" / "open-redirect.md").read_text()
    assert page.count("Protocol-relative redirect.") == 1


def test_punctuation_only_fragments_are_not_published():
    # Extractors pull these out of prose; they are not payloads and a
    # wordlist full of them is worse than one without.
    junk = ["'../'", "'\\../", "'../", "..", "'", "``", "   "]
    cands = [Candidate(827052, "path-traversal", j, "ctx", "path_traversal") for j in junk]
    verdicts = [Verdict(c.key(), True, "t", None) for c in cands]
    assert build_records(cands, verdicts, INDEX, CLASSES) == []


def test_a_real_short_payload_still_survives():
    keep = ["//evil.com", "../../etc/passwd", "{{7*7}}", "' OR 1=1--"]
    cands = [Candidate(827052, "path-traversal", k, "ctx", "path_traversal") for k in keep]
    verdicts = [Verdict(c.key(), True, "t", None) for c in cands]
    assert len(build_records(cands, verdicts, INDEX, CLASSES)) == len(keep)


def test_similar_techniques_cluster_under_one_heading(tmp_path):
    # Exact-sentence grouping produced 741 headings for 803 payloads, which is
    # a flat dump wearing a heading. Group on the leading significant words so
    # real variants -- svg onload, img onerror -- actually cluster.
    cands, verds = [], []
    for i, tech in enumerate([
        "Reflected XSS via svg onload attribute in the search field",
        "Reflected XSS via svg onload attribute in the profile name",
        "Reflected XSS via img onerror attribute in the comment body",
    ]):
        c = Candidate(827052, "xss", f"<svg onload=alert({i})>", f"ctx{i}", "xss")
        cands.append(c)
        verds.append(Verdict(c.key(), True, tech, None))
    emit(build_records(cands, verds, INDEX, CLASSES), CLASSES, tmp_path)
    page = (tmp_path / "payloads" / "xss.md").read_text()
    assert page.count("\n## ") == 2      # svg onload group, img onerror group


def test_a_group_heading_is_a_real_sentence_not_a_keyword_soup(tmp_path):
    c = Candidate(827052, "xss", "<svg onload=1>", "ctx", "xss")
    v = [Verdict(c.key(), True, "Reflected XSS via svg onload attribute", None)]
    emit(build_records([c], v, INDEX, CLASSES), CLASSES, tmp_path)
    page = (tmp_path / "payloads" / "xss.md").read_text()
    assert "## Reflected XSS via svg onload attribute" in page


def test_a_payload_containing_a_fence_cannot_escape_its_block(tmp_path):
    # A payload with ``` closed the fence early, and the rest of it rendered
    # as markdown -- headings and all -- corrupting the page structure.
    evil = 'type ```test";</script><script>alert(1)</script>\n## Impact\nreal heading?'
    c = Candidate(827052, "xss", evil, "ctx", "xss")
    emit(build_records([c], [Verdict(c.key(), True, "t", None)], INDEX, CLASSES),
         CLASSES, tmp_path)
    page = (tmp_path / "payloads" / "xss.md").read_text()
    # Headings must only exist OUTSIDE a fence. A raw line scan cannot tell the
    # difference, so track fence state the way a markdown parser would.
    depth, outside = None, []
    for line in page.splitlines():
        run = len(line) - len(line.lstrip("`"))
        if run >= 3:
            if depth is None:
                depth = run
            elif run >= depth:
                depth = None
            continue
        if depth is None and line.startswith("#"):
            outside.append(line)
    assert "## Impact" not in outside, outside
    assert "````" in page          # fence widened past the payload's own run


def test_an_ordinary_payload_still_uses_a_plain_fence(tmp_path):
    c = Candidate(827052, "xss", "<svg onload=alert(1)>", "ctx", "xss")
    emit(build_records([c], [Verdict(c.key(), True, "t", None)], INDEX, CLASSES),
         CLASSES, tmp_path)
    page = (tmp_path / "payloads" / "xss.md").read_text()
    assert "````" not in page
