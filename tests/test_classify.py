from src.classify import classify_report
from src.config import load_classes

CLASSES = load_classes()


def classify(record, body=""):
    return classify_report(record, body, CLASSES)


def test_weakness_is_the_primary_signal():
    result = classify({"id": 1, "title": "unrelated", "weakness": "Open Redirect"})
    assert result.classes == ("open-redirect",)
    assert result.signal == "weakness"


def test_weakness_matches_as_a_substring():
    # Real corpus values include "Path Traversal: '.../...//'" and
    # "Relative Path Traversal" alongside plain "Path Traversal".
    for value in ["Path Traversal", "Relative Path Traversal", "Path Traversal: '.../...//'"]:
        result = classify({"id": 1, "title": "x", "weakness": value})
        assert result.classes == ("path-traversal",), value


def test_rce_aliases_cover_all_three_corpus_spellings():
    for value in ["Code Injection", "Command Injection - Generic", "OS Command Injection"]:
        assert classify({"id": 1, "title": "x", "weakness": value}).classes == ("rce",), value


def test_null_weakness_falls_back_to_title():
    result = classify({"id": 1, "title": "Reflected XSS on login page", "weakness": None})
    assert result.classes == ("xss",)
    assert result.signal == "title"


def test_body_is_the_last_resort():
    result = classify(
        {"id": 1, "title": "Interesting behaviour", "weakness": None},
        body="The application evaluates jinja2 expressions supplied by the user.",
    )
    assert result.classes == ("ssti",)
    assert result.signal == "body"


def test_ssti_is_reachable_despite_having_no_weakness_alias():
    result = classify({"id": 1, "title": "Server-Side Template Injection in preview", "weakness": None})
    assert result.classes == ("ssti",)


def test_a_report_can_belong_to_several_classes():
    result = classify({"id": 1, "title": "SSRF chained with an open redirect", "weakness": None})
    assert set(result.classes) == {"ssrf", "open-redirect"}


def test_unclassifiable_report_yields_no_classes():
    result = classify({"id": 1, "title": "Rate limiting missing", "weakness": "Misconfiguration"})
    assert result.classes == ()
    assert result.signal == "none"


def test_short_acronyms_do_not_match_inside_ordinary_words():
    # "rce" is a substring of "resource" and "lfi" of "selfie"; a bare
    # substring test would file both of these under the wrong class.
    assert classify({"id": 1, "title": "Uncontrolled Resource Consumption", "weakness": None}).classes == ()
    assert classify({"id": 1, "title": "Selfie upload crashes the app", "weakness": None}).classes == ()


def test_acronyms_still_match_as_whole_words():
    assert classify({"id": 1, "title": "RCE via image parser", "weakness": None}).classes == ("rce",)
    assert classify({"id": 1, "title": "LFI in template loader", "weakness": None}).classes == ("path-traversal",)
