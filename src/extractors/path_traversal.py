"""Path traversal and local file inclusion payload shapes."""

from src.extractors.base import Candidate, scan

CLS = "path-traversal"
NAME = "path_traversal"

PATTERNS = (
    r"\.\./|\.\.\\",                       # plain traversal, both separators
    r"%2e%2e(%2f|%5c)",                    # single-encoded
    r"%252e%252e",                         # double-encoded
    r"\.\.\.\.//|\.\.;/",                  # filter-bypass doublings
    r"\bfile:///",
    r"/etc/(passwd|shadow|hosts)\b",
    r"\bwin\.ini\b|\bboot\.ini\b|\bwin32\.ini\b",
    r"\bproc/self/(environ|cmdline)\b",
    r"\bphp://(filter|input)\b|\bexpect://",
)


def extract(report_id: int, md: str) -> list[Candidate]:
    return scan(md, report_id, CLS, NAME, PATTERNS)
