from src.extractors import EXTRACTORS
from src.extractors.idor import extract

MD = """
Request:

```
GET /api/v1/users/1337/invoices HTTP/1.1
Host: target.com
```

Changing `?user_id=1337` to another value returns their data.
Also works with the UUID `550e8400-e29b-41d4-a716-446655440000`.
"""


def payloads():
    return [c.payload for c in extract(1, MD)]


def test_finds_numeric_id_in_path():
    assert any("/users/1337/" in p for p in payloads())


def test_finds_id_parameter():
    assert any("user_id=" in p for p in payloads())


def test_finds_uuid():
    assert any("550e8400" in p for p in payloads())


def test_registered():
    assert EXTRACTORS["idor"] is extract
