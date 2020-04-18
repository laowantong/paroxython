from collections import defaultdict
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


def enumeration_to_html_factory(width=20, default_string=""):
    def enumeration_to_html(s):
        if not s:
            return default_string
        i = len(s)
        if i <= width:
            return s
        while i > width:
            candidate = s.rfind(",", 0, i)
            if candidate == -1:
                break
            i = candidate
        return f"<details><summary>{s[:i+2]}</summary>{s[i+2:]}</details>"

    return enumeration_to_html
