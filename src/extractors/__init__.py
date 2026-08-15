"""Registry of per-class payload extractors."""

from collections.abc import Callable

from src.extractors import (
    csrf,
    idor,
    open_redirect,
    path_traversal,
    rce,
    sqli,
    ssrf,
    ssti,
    xss,
    xxe,
)
from src.extractors.base import Candidate

Extractor = Callable[[int, str], list[Candidate]]

EXTRACTORS: dict[str, Extractor] = {
    "open-redirect": open_redirect.extract,
    "xss": xss.extract,
    "ssrf": ssrf.extract,
    "sqli": sqli.extract,
    "ssti": ssti.extract,
    "path-traversal": path_traversal.extract,
    "xxe": xxe.extract,
    "csrf": csrf.extract,
    "idor": idor.extract,
    "rce": rce.extract,
}
