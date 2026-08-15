"""Cross-site scripting payload shapes."""

from src.extractors.base import Candidate, scan

CLS = "xss"
NAME = "xss"

PATTERNS = (
    r"<\s*(script|svg|img|iframe|body|details|video|audio|object|embed|math)\b",
    r"\bon(load|error|mouseover|focus|click|toggle|animationstart)\s*=",
    r"javascript\s*:",
    r"\balert\s*\(|\bconfirm\s*\(|\bprompt\s*\(",
    r"document\.(domain|cookie)",
    r"&lt;\s*(script|svg|img)\b",
    r"\"\s*>\s*<",
)


def extract(report_id: int, md: str) -> list[Candidate]:
    return scan(md, report_id, CLS, NAME, PATTERNS)
