"""Shared markdown-walking primitives for payload extractors."""

import hashlib
import re
from dataclasses import dataclass

CONTEXT_CHARS = 200
MAX_PAYLOAD_CHARS = 500

_FENCE = re.compile(r"```[a-zA-Z0-9_+-]*\n(.*?)```", re.DOTALL)
_INLINE = re.compile(r"`([^`\n]{1,300})`")
_URL = re.compile(r"https?://[^\s\)\]\>\"'`]+")
_HEADING = re.compile(r"^#{1,6}\s*(.+)$", re.MULTILINE)
_REPRO = re.compile(
    r"steps?\s+to\s+reproduce|reproduction\s+steps?|proof\s+of\s+concept|\bpoc\b",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class Candidate:
    report_id: int
    cls: str
    payload: str
    context: str
    extractor: str

    def key(self) -> str:
        digest = hashlib.sha1(f"{self.payload}\x00{self.context}".encode())
        return digest.hexdigest()


def _context_for(md: str, start: int, end: int) -> str:
    lo = max(0, start - CONTEXT_CHARS)
    hi = min(len(md), end + CONTEXT_CHARS)
    return md[lo:hi].strip()


def _matches(md: str, pattern: re.Pattern, context_source: str | None = None):
    """Find pattern in `md`, but take context from `context_source`.

    The two differ when scanning masked text: masking preserves offsets, so
    the match positions still index correctly into the original markdown.
    """
    source = md if context_source is None else context_source
    out = []
    for match in pattern.finditer(md):
        text = match.group(1) if match.groups() else match.group(0)
        out.append((text, _context_for(source, match.start(), match.end())))
    return out


def _mask(md: str, pattern: re.Pattern) -> str:
    """Blank out claimed regions, preserving length so offsets stay valid."""
    return pattern.sub(lambda m: " " * len(m.group(0)), md)


def code_blocks(md: str, context_source: str | None = None) -> list[tuple[str, str]]:
    return _matches(md, _FENCE, context_source)


def inline_code(md: str, context_source: str | None = None) -> list[tuple[str, str]]:
    return _matches(md, _INLINE, context_source)


def urls(md: str, context_source: str | None = None) -> list[tuple[str, str]]:
    return _matches(md, _URL, context_source)


def repro_lines(md: str, context_source: str | None = None) -> list[tuple[str, str]]:
    """Prose lines under a 'Steps to reproduce' / 'PoC' heading.

    Spec 7.3's fourth candidate source. Researchers routinely write the
    payload into the prose of a repro step instead of fencing it, and the
    other three walkers only ever look inside fences, backtick spans and bare
    URLs -- so without this those payloads are unreachable by every extractor.

    Scoped to repro sections rather than all prose: prose generally is mostly
    narrative, and scanning it would bury stage 4 in candidates it has to pay
    to reject. Emitted line by line, so a payload is one line rather than the
    whole section.
    """
    source = md if context_source is None else context_source
    out: list[tuple[str, str]] = []
    headings = list(_HEADING.finditer(md))
    for index, heading in enumerate(headings):
        if not _REPRO.search(heading.group(1)):
            continue
        start = heading.end()
        end = headings[index + 1].start() if index + 1 < len(headings) else len(md)
        offset = start
        for line in md[start:end].splitlines(keepends=True):
            stripped = line.strip()
            if stripped:
                out.append((stripped, _context_for(source, offset, offset + len(line))))
            offset += len(line)
    return out


def regions(md: str) -> list[tuple[str, str]]:
    """Every scannable region, each piece of text claimed exactly once.

    Without this partition a URL inside a fenced block is captured by the
    fence walker, again by the inline walker if backticked, and again by the
    URL walker -- three candidates for one payload, with contexts that differ
    just enough that key() cannot collapse them. Stage 4 then pays three
    times for the same string, multiplied across every extractor.

    A fourth source -- prose lines under a repro-style heading -- runs last,
    over text with the other three already masked out, so a payload written
    unfenced into a repro step is still reachable without being claimed twice.
    """
    blocks = code_blocks(md)
    after_fences = _mask(md, _FENCE)
    spans = inline_code(after_fences, md)
    after_inline = _mask(after_fences, _INLINE)
    links = urls(after_inline, md)
    after_urls = _mask(after_inline, _URL)
    prose = repro_lines(after_urls, md)
    return blocks + spans + links + prose


def scan(
    md: str,
    report_id: int,
    cls: str,
    extractor: str,
    patterns: tuple[str, ...],
) -> list[Candidate]:
    """Emit one Candidate per distinct region matching any pattern."""
    compiled = [re.compile(p, re.IGNORECASE) for p in patterns]
    seen: set[str] = set()
    found: list[Candidate] = []

    for text, context in regions(md):
        for pattern in compiled:
            match = pattern.search(text)
            if not match:
                continue
            payload = text.strip()[:MAX_PAYLOAD_CHARS]
            if not payload:
                continue
            candidate = Candidate(report_id, cls, payload, context, extractor)
            if candidate.key() in seen:
                continue
            seen.add(candidate.key())
            found.append(candidate)
            break

    return found
