"""Insecure direct object reference request shapes."""

from src.extractors.base import Candidate, scan

CLS = "idor"
NAME = "idor"

PATTERNS = (
    r"\b(GET|POST|PUT|PATCH|DELETE)\s+/\S*/\d{2,}\b",
    r"[?&](id|user_id|userid|account_id|uid|order_id|invoice_id|team_id|object_id)=",
    r"\"(id|user_id|account_id|uuid)\"\s*:",
    r"\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b",
    r"/api/v\d+/\S*/\d{2,}",
)


def extract(report_id: int, md: str) -> list[Candidate]:
    return scan(md, report_id, CLS, NAME, PATTERNS)
