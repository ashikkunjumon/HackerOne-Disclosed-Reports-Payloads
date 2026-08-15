from src.extractors import EXTRACTORS
from src.extractors.sqli import extract

MD = """
Payload:

```
' UNION SELECT null,version(),null-- -
```

Also `1' AND SLEEP(5)-- ` and `1 OR 1=1` work. Confirmed with sqlmap.
"""


def payloads():
    return [c.payload for c in extract(1, MD)]


def test_finds_union_select():
    assert any("UNION SELECT" in p.upper() for p in payloads())


def test_finds_time_based():
    assert any("SLEEP(5)" in p.upper() for p in payloads())


def test_finds_boolean_tautology():
    assert any("1=1" in p for p in payloads())


def test_registered():
    assert EXTRACTORS["sqli"] is extract
