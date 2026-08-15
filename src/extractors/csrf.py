"""Cross-site request forgery payload shapes."""

from src.extractors.base import Candidate, scan

CLS = "csrf"
NAME = "csrf"

PATTERNS = (
    r"<form\b[^>]*\b(action|method)\s*=",
    r"document\.forms\[\s*\d*\s*\]\.submit\s*\(",
    r"\bcsrf[_-]?token\b|\bauthenticity_token\b|\b_token\b|\bxsrf\b",
    r"<img\b[^>]*\bsrc\s*=\s*[\"']https?://",
    r"\bfetch\s*\([^)]*credentials\s*:\s*[\"']include",
    r"\bSameSite\s*=\s*None\b",
)


def extract(report_id: int, md: str) -> list[Candidate]:
    return scan(md, report_id, CLS, NAME, PATTERNS)
