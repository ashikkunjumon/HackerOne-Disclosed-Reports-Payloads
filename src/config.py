"""Loads the declarative vulnerability-class registry."""

from dataclasses import dataclass
from pathlib import Path

import yaml

DEFAULT_PATH = Path("config/classes.yaml")


@dataclass(frozen=True)
class VulnClass:
    slug: str
    name: str
    cwe_aliases: tuple[str, ...]
    title_keywords: tuple[str, ...]
    body_keywords: tuple[str, ...]


def load_classes(path: Path = DEFAULT_PATH) -> dict[str, VulnClass]:
    raw = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(raw, list):
        raise ValueError(f"{path} must contain a list of class definitions")

    classes: dict[str, VulnClass] = {}
    for entry in raw:
        for field in ("slug", "name", "title_keywords"):
            if not entry.get(field):
                raise ValueError(f"class {entry.get('slug', '?')} is missing {field}")
        slug = entry["slug"]
        if slug in classes:
            raise ValueError(f"duplicate class slug: {slug}")
        classes[slug] = VulnClass(
            slug=slug,
            name=entry["name"],
            cwe_aliases=tuple(entry.get("cwe_aliases") or ()),
            title_keywords=tuple(entry["title_keywords"]),
            body_keywords=tuple(entry.get("body_keywords") or ()),
        )
    return classes
