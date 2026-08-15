import json

from src.run import _previous_count


def test_previous_count_reads_the_published_file(tmp_path):
    (tmp_path / "payloads.json").write_text(json.dumps([{"a": 1}, {"a": 2}]))
    assert _previous_count(tmp_path) == 2


def test_previous_count_is_zero_when_absent_or_corrupt(tmp_path):
    assert _previous_count(tmp_path) == 0
    (tmp_path / "payloads.json").write_text("{not json")
    assert _previous_count(tmp_path) == 0
