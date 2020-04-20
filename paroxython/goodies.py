from collections import defaultdict
from textwrap import wrap
from typing import Callable, Optional
from unicodedata import normalize

import regex  # type: ignore

from user_types import Source


def title_to_slug_factory():
    slug_counts = defaultdict(int)
    cache = {}

    def title_to_slug(title, deduplicate=False):
        title = title.strip()
        if title not in cache:
            slug = normalize("NFD", title.lower()).encode("ASCII", "ignore").decode("ASCII")
            slug = slug.replace(" ", "-")
            slug = regex.sub(r"[^\w-]", "", slug)
            cache[title] = slug
        if deduplicate:
            slug = cache[title]
            slug_counts[slug] += 1
            slug = f"{slug}-{slug_counts[slug] - 1}"
            slug_counts[slug] += 1
            slug = slug.rstrip("-0")
            return slug
        else:
            return cache[title]

    return title_to_slug


def add_line_numbers(source: Source) -> str:
    return "\n".join(f"{n: <4}{line}" for (n, line) in enumerate(source.split("\n"), 1))


def enumeration_to_txt_factory(
    width: int = 20,
    default_string: str = "",
    sep: str = "<br>",
    template: str = "<details><summary>{summary}</summary>{details}</details>",
    initial_indent: str = "   ",  # take into account the details marker
) -> Callable[[str], str]:
    """Return a function formatting a enumeration string on a given column width."""

    def enumeration_to_txt(s: str) -> str:
        if not s:
            return default_string
        if len(s) <= width:
            return s
        lines = wrap(s, width, initial_indent=initial_indent)
        summary = lines[0][len(initial_indent) :]
        details = sep.join(lines[1:])
        return template.format(summary=summary, details=details)

    return enumeration_to_txt
