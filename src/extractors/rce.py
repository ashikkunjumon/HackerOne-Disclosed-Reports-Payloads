"""Remote code execution and command injection payload shapes."""

from src.extractors.base import Candidate, scan

CLS = "rce"
NAME = "rce"

PATTERNS = (
    r"[;&|]{1,2}\s*(id|whoami|uname|cat|ls|curl|wget|nc|ping|sleep)\b",
    r"\$\([^)]{1,120}\)",                  # command substitution
    r"`[^`\n]{1,120}`",                    # backtick substitution
    r"\bbash\s+-i\b|/dev/tcp/",            # reverse shell
    r"\bnc\s+-[a-z]*e\b",
    r"\b(system|exec|popen|passthru|shell_exec|eval|assert)\s*\(",
    r"\bRuntime\.getRuntime\(\)\.exec\b|\bProcessBuilder\b",
    r"\b__import__\s*\(|\bos\.system\s*\(|\bsubprocess\.",
    r"%0a(id|whoami|uname)\b",
)


def extract(report_id: int, md: str) -> list[Candidate]:
    return scan(md, report_id, CLS, NAME, PATTERNS)
