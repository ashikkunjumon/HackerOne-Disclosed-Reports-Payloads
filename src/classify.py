"""Stage 2 — assign reports to vulnerability classes."""

import re
from dataclasses import dataclass

from src.config import VulnClass


@dataclass(frozen=True)
class Classification:
    report_id: int
    classes: tuple[str, ...]
    signal: str


def _match(haystack: str, needles: tuple[str, ...]) -> bool:
    """Substring match, word-bounded for single alphanumeric tokens.

    Short acronyms are substrings of ordinary words -- "rce" appears inside
    "resource", "lfi" inside "selfie" -- so a bare substring test
    misclassifies. Multi-word and punctuation-bearing needles like
    "Path Traversal" or "../../" keep plain substring matching, since word
    boundaries do not behave usefully around them.
    """
    for needle in needles:
        needle = needle.lower()
        if needle.isalnum():
            if re.search(rf"\b{re.escape(needle)}\b", haystack):
                return True
        elif needle in haystack:
            return True
    return False


def classify_report(
    record: dict,
    body: str,
    classes: dict[str, VulnClass],
) -> Classification:
    report_id = record["id"]
    weakness = (record.get("weakness") or "").lower()
    title = (record.get("title") or "").lower()
    body_lower = body.lower()

    if weakness:
        hits = tuple(s for s, c in classes.items() if _match(weakness, c.cwe_aliases))
        if hits:
            return Classification(report_id, hits, "weakness")

    hits = tuple(s for s, c in classes.items() if _match(title, c.title_keywords))
    if hits:
        return Classification(report_id, hits, "title")

    hits = tuple(s for s, c in classes.items() if _match(body_lower, c.body_keywords))
    if hits:
        return Classification(report_id, hits, "body")

    return Classification(report_id, (), "none")
