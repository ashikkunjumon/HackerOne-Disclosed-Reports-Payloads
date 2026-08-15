from src.extractors import EXTRACTORS
from src.extractors.ssti import extract

MD = """
Submitting `{{7*7}}` renders `49`.

Escalation:

```
{{config.__class__.__init__.__globals__['os'].popen('id').read()}}
```

Freemarker variant: `${7*7}` and `<%= 7*7 %>`.
"""


def payloads():
    return [c.payload for c in extract(1, MD)]


def test_finds_jinja_probe():
    assert any("{{7*7}}" in p for p in payloads())


def test_finds_globals_escalation():
    assert any("__globals__" in p for p in payloads())


def test_finds_dollar_brace_variant():
    assert any("${7*7}" in p for p in payloads())


def test_registered():
    assert EXTRACTORS["ssti"] is extract
