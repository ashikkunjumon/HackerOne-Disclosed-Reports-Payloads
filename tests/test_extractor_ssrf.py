from src.extractors import EXTRACTORS
from src.extractors.ssrf import extract

MD = """
Request the metadata endpoint:

```
http://169.254.169.254/latest/meta-data/iam/security-credentials/
```

Bypass with `http://[::1]/` or `gopher://127.0.0.1:6379/_INFO` or
`http://2130706433/`.
"""


def payloads():
    return [c.payload for c in extract(1, MD)]


def test_finds_cloud_metadata_ip():
    assert any("169.254.169.254" in p for p in payloads())


def test_finds_gopher_scheme():
    assert any("gopher://" in p for p in payloads())


def test_finds_ipv6_loopback():
    assert any("[::1]" in p for p in payloads())


def test_finds_decimal_ip():
    assert any("2130706433" in p for p in payloads())


def test_registered():
    assert EXTRACTORS["ssrf"] is extract
