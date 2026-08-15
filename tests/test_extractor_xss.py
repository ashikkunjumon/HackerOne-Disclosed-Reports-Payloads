from src.extractors import EXTRACTORS
from src.extractors.xss import extract

MD = """
Payload used:

```
<svg/onload=alert(document.domain)>
```

Also `"><img src=x onerror=alert(1)>` and a `javascript:alert(1)` URI.

Vulnerable sink:

```javascript
element.innerHTML = userInput;
```
"""


def payloads():
    return [c.payload for c in extract(1, MD)]


def test_finds_svg_onload():
    assert any("svg/onload" in p for p in payloads())


def test_finds_attribute_breakout():
    assert any("onerror=alert(1)" in p for p in payloads())


def test_finds_javascript_uri():
    assert any("javascript:" in p for p in payloads())


def test_registered():
    assert EXTRACTORS["xss"] is extract
