from src.extractors import EXTRACTORS
from src.extractors.path_traversal import extract

MD = """
Payload:

```
![a](/uploads/11111111111111111111111111111111/../../../../../../etc/passwd)
```

Encoded variants: `%2e%2e%2f%2e%2e%2fetc/passwd` and `....//....//etc/passwd`
and `..\\..\\windows\\win.ini`.
"""


def payloads():
    return [c.payload for c in extract(1, MD)]


def test_finds_plain_traversal():
    assert any("../../" in p for p in payloads())


def test_finds_encoded_traversal():
    assert any("%2e%2e%2f" in p.lower() for p in payloads())


def test_finds_doubled_dot_bypass():
    assert any("....//" in p for p in payloads())


def test_finds_windows_traversal():
    assert any("win.ini" in p for p in payloads())


def test_registered():
    assert EXTRACTORS["path-traversal"] is extract
