import json
from pathlib import Path

from src.config import load_classes
from src.run import extract_candidates

CLASSES = load_classes()


def test_extracts_only_for_classified_classes(tmp_path):
    reports = tmp_path / "reports"
    reports.mkdir()
    (reports / "1.md").write_text("Payload: `?next=//evil.com` redirects off-site.")
    index = {1: {"id": 1, "title": "Open redirect in callback", "weakness": "Open Redirect"}}

    candidates = extract_candidates(index, tmp_path, CLASSES)
    assert candidates
    assert {c.cls for c in candidates} == {"open-redirect"}


def test_unclassified_reports_produce_nothing(tmp_path):
    reports = tmp_path / "reports"
    reports.mkdir()
    (reports / "1.md").write_text("The team shipped a fix.")
    index = {1: {"id": 1, "title": "Rate limiting", "weakness": "Misconfiguration"}}

    assert extract_candidates(index, tmp_path, CLASSES) == []


def test_missing_body_is_skipped(tmp_path):
    (tmp_path / "reports").mkdir()
    index = {999: {"id": 999, "title": "XSS somewhere", "weakness": "Cross-site Scripting (XSS) - Generic"}}
    assert extract_candidates(index, tmp_path, CLASSES) == []


def test_extract_candidates_writes_the_stage_2_and_3_artifacts(tmp_path):
    reports = tmp_path / "reports"
    reports.mkdir()
    (reports / "1.md").write_text("Payload: `?next=//evil.com` redirects off-site.")
    index = {1: {"id": 1, "title": "Open redirect in callback", "weakness": "Open Redirect"}}
    data_dir = tmp_path / "data"

    candidates = extract_candidates(index, tmp_path, CLASSES, data_dir=data_dir)

    assert candidates
    classified = json.loads((data_dir / "classified.json").read_text())
    assert classified["1"]["classes"] == ["open-redirect"]
    assert classified["1"]["signal"]

    lines = (data_dir / "candidates.jsonl").read_text().splitlines()
    assert len(lines) == len(candidates)
    assert json.loads(lines[0])["class"] == "open-redirect"


def test_extract_candidates_without_a_data_dir_writes_nothing(tmp_path):
    reports = tmp_path / "reports"
    reports.mkdir()
    (reports / "1.md").write_text("Payload: `?next=//evil.com` redirects off-site.")
    index = {1: {"id": 1, "title": "Open redirect in callback", "weakness": "Open Redirect"}}

    extract_candidates(index, tmp_path, CLASSES)

    assert not (tmp_path / "data" / "classified.json").exists()
