"""XML external entity payload shapes."""

from src.extractors.base import Candidate, scan

CLS = "xxe"
NAME = "xxe"

PATTERNS = (
    r"<!DOCTYPE\b",
    r"<!ENTITY\b",
    r"\bSYSTEM\s+[\"']",
    r"\bPUBLIC\s+[\"']",
    r"file:///",
    r"\bxi:include\b",
    r"\bexpect://|\bphp://filter",
)


def extract(report_id: int, md: str) -> list[Candidate]:
    return scan(md, report_id, CLS, NAME, PATTERNS)
