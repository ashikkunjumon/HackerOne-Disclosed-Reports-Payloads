from pathlib import Path

from src.config import VulnClass, load_classes

SLUGS = {
    "open-redirect", "xss", "ssrf", "sqli", "ssti",
    "path-traversal", "xxe", "csrf", "idor", "rce",
}


def test_loads_all_ten_classes():
    classes = load_classes(Path("config/classes.yaml"))
    assert set(classes) == SLUGS


def test_each_class_is_fully_populated():
    classes = load_classes(Path("config/classes.yaml"))
    for slug, vc in classes.items():
        assert isinstance(vc, VulnClass)
        assert vc.slug == slug
        assert vc.name, f"{slug} missing name"
        assert vc.title_keywords, f"{slug} has no title keywords"


def test_ssti_has_no_cwe_aliases():
    # No report in the corpus carries a template-injection weakness value,
    # so SSTI must be reachable by keyword alone.
    classes = load_classes(Path("config/classes.yaml"))
    assert classes["ssti"].cwe_aliases == ()
    assert "template injection" in classes["ssti"].title_keywords


def test_path_traversal_alias_is_a_substring_not_an_exact_value():
    classes = load_classes(Path("config/classes.yaml"))
    assert "Path Traversal" in classes["path-traversal"].cwe_aliases
