"""Server-side template injection payload shapes."""

from src.extractors.base import Candidate, scan

CLS = "ssti"
NAME = "ssti"

PATTERNS = (
    r"\{\{.{1,200}?\}\}",                  # Jinja2 / Twig / Handlebars
    r"\$\{.{1,200}?\}",                    # Freemarker / JSP EL / Velocity
    r"<%=.{1,200}?%>",                     # ERB / JSP scriptlet
    r"\{%.{1,200}?%\}",                    # Jinja statement
    r"__globals__|__class__|__subclasses__|__mro__",
    r"\bfreemarker\b|\bvelocity\b|\bsmarty\b",
    r"#set\s*\(|#\{.{1,200}?\}",
)


def extract(report_id: int, md: str) -> list[Candidate]:
    return scan(md, report_id, CLS, NAME, PATTERNS)
