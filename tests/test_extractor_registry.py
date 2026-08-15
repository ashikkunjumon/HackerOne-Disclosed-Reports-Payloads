from src.config import load_classes
from src.extractors import EXTRACTORS


def test_every_configured_class_has_an_extractor():
    assert set(EXTRACTORS) == set(load_classes())


def test_extractors_return_an_empty_list_for_unrelated_prose():
    md = "The team acknowledged the report and shipped a fix in the next release."
    for slug, extract in EXTRACTORS.items():
        assert extract(1, md) == [], slug
