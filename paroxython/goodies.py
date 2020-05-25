import sys
from collections import defaultdict
from math import log2
from textwrap import wrap
from typing import Callable, Tuple, Union
from unicodedata import normalize

import regex  # type: ignore

from .user_types import Span


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


def add_line_numbers(source: str) -> str:
    """Return a numbered version of the given source code. Result readable up to 999 lines."""
    return "\n".join(f"{n: <4}{line}" for (n, line) in enumerate(source.split("\n"), 1))


def enumeration_to_txt_factory(
    width: int = 20,
    default_string: str = "",
    sep: str = "<br>",
    template: str = "<details><summary>{summary}</summary>{details}</details>",
    initial_indent: str = "   ",  # take into account the details marker
) -> Callable[[str], str]:
    """Return a function formatting an enumeration string on a given column width."""

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


def cost_bucket(cost: int) -> str:
    """Among a predetermined set of intervals, return that including the given positive number.

    The intervals are `[0, 0]`, `]0, 0.25[`, `[0.25, 0.5[`, `[0.5, 1[`, `[1, 2[`, `[2,
    4[`, `[4, 8[`, and so on. The result is returned as a string ready to be included in the
    recommendation report.

    >>> cost_bucket(0.75)
    "in [0.5, 1["
    """
    if cost == 0:
        return "0"
    if cost < 0.25:
        return "in ]0, 0.25["
    if cost < 0.5:
        return "in [0.25, 0.5["
    if cost < 1:
        return "in [0.5, 1["
    upper = 2 ** int(log2(cost))
    lower = 2 ** int(log2(cost) + 1)
    return f"in [{upper}, {lower}["


def couple_to_string(couple: Union[Span, Tuple[int, int]]) -> str:
    """Return a deduplicated string representation of the given couple or span.

    >>> couple_to_string((12, 15))
    "12-15"
    >>> couple_to_string((12, 12))
    "12"
    >>> couple_to_string(Span(12, 15))
    "12-15"
    """
    return f"{couple[0]}" + ("" if couple[0] == couple[1] else f"-{couple[1]}")


def print_warning(message: str):
    print(f"Warning: {message}", file=sys.stderr)
