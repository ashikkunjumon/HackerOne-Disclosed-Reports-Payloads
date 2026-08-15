"""Open redirect payload shapes."""

from src.extractors.base import Candidate, scan

CLS = "open-redirect"
NAME = "open_redirect"

PATTERNS = (
    r"[?&](next|url|redirect|redirect_uri|return|returnTo|dest|destination|continue|r|u)=\S",
    r"(?<!:)//[a-z0-9.-]+\.[a-z]{2,}",     # protocol-relative
    r"/\\+/",                              # backslash-slash confusion
    r"https?://[^\s/]+@[a-z0-9.-]+",       # userinfo @ confusion
    r"%2f%2f",                             # encoded protocol-relative
    r"\.\.;/",                             # path-segment tricks in redirects
    r"%0d%0a|%0a|%0d",                     # CRLF in redirect targets
)


def extract(report_id: int, md: str) -> list[Candidate]:
    return scan(md, report_id, CLS, NAME, PATTERNS)
