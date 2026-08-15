"""SQL injection payload shapes."""

from src.extractors.base import Candidate, scan

CLS = "sqli"
NAME = "sqli"

PATTERNS = (
    r"\bunion\s+(all\s+)?select\b",
    r"\bor\s+1\s*=\s*1\b|\band\s+1\s*=\s*1\b",
    r"\bsleep\s*\(\s*\d+\s*\)|\bpg_sleep\s*\(|\bwaitfor\s+delay\b",
    r"\bbenchmark\s*\(",
    r"\bextractvalue\s*\(|\bupdatexml\s*\(",
    r"\binformation_schema\b",
    r"\bversion\s*\(\s*\)|@@version",
    r"--\s|#\s*$|/\*.*?\*/",
    r"'\s*(or|and)\s*'",
)


def extract(report_id: int, md: str) -> list[Candidate]:
    return scan(md, report_id, CLS, NAME, PATTERNS)
