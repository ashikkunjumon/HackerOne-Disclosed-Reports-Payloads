"""Server-side request forgery payload shapes."""

from src.extractors.base import Candidate, scan

CLS = "ssrf"
NAME = "ssrf"

PATTERNS = (
    r"169\.254\.169\.254",                    # AWS/GCP/Azure metadata
    r"metadata\.google\.internal",
    r"\b127\.0\.0\.1\b|\blocalhost\b",
    r"\[::1\]|\[0:0:0:0:0:0:0:1\]",
    r"\b(gopher|dict|file|ftp|ldap|jar|netdoc)://",
    r"\b(0x7f[0-9a-f]{6}|2130706433|0177\.0\.0\.1)\b",   # encoded loopback
    r"\b(10|192\.168|172\.(1[6-9]|2[0-9]|3[01]))\.\d",   # RFC1918
    r"\bburpcollaborator\b|\binteract\.sh\b|\bngrok\.io\b",
)


def extract(report_id: int, md: str) -> list[Candidate]:
    return scan(md, report_id, CLS, NAME, PATTERNS)
