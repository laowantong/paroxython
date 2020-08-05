"""A grab bag of various generic functions and factories."""

import sys
from collections import defaultdict
from math import log2
from textwrap import wrap
from typing import Callable, Dict, Tuple, Union
from unicodedata import normalize

import regex  # type: ignore

from .user_types import Span


def title_to_slug_factory() -> Callable:
    """Return a function mapping a string to the appropriate slug, optionally disambiguated.

    Returns:
        Callable[[str, Optional[bool]]]: A function taking a string and an optional boolean
            `deduplicate` (default: `False`). If `True`, when two or more strings produce the same
            slug, a numeric suffix is added to the second one (`"-1"`), the third one (`"-2"`), and
            so on.

    Examples:
        See [`test_goodies.py`](https://repo/paroxython/tests/test_goodies.py).
    """
    slug_counts: Dict[str, int] = defaultdict(int)
    cache: Dict[str, str] = {}

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
    initial_indent: int = 3,  # take into account the details marker
) -> Callable[[str], str]:
    """Return a function formatting an enumeration on a given column width.

    This function is used by `recommend_programs.get_markdown()` to limit the width of the last
    column of the Markdown tables, as in the following example:

    | Cost  | Taxon | Location |
    |:---|:---|:---|
    | 0.9375 | `type/number/integer/literal` | <details><summary>1, 1, 1, 1, </summary>1, 1, 2, 2, 2, <br>2, 2, 3, 3, 3</details> |

    The enumeration, given as a string, is wrapped onto one or several lines of at most `width`
    characters. The first line and the remaining ones are formatted separately according to the
    given `template`.

    Args:
        width (int, optional): Column width.
            Defaults to `20`.
        default_string (str, optional): String to return when the enumeration is empty.
            Defaults to `""`.
        sep (str, optional): Separator between wrapped lines.
            Defaults to `"<br>"`.
        template (str, optional): A formatting string on the first line (referred as `summary`)
            and the remaining ones (referred as `details`).
            Defaults to `"<details><summary>{summary}</summary>{details}</details>"`.
        initial_indent (str, optional): Approximate space-width of the detail marker (e.g.,
            `"▶︎ "`).
            Defaults to `3`.

    Returns:
        Callable[[str], str]: Function returning a wrapped version of a given string.

    Example:
        >>> enumeration_to_txt = enumeration_to_txt_factory(7)  # create the function
        >>> enumeration_to_txt("1, 2, 3, 4, 5-6, 7, 8, 9")      # use it
        "<details><summary>1,</summary>2, 3,<br>4, 5-6,<br>7, 8, 9</details>"
    """

    def enumeration_to_txt(s: str) -> str:
        if not s:
            return default_string
        if len(s) <= width:
            return s
        lines = wrap(s, width, initial_indent=" " * initial_indent)
        summary = lines[0][initial_indent:]
        details = sep.join(lines[1:])
        return template.format(summary=summary, details=details)

    return enumeration_to_txt


def cost_bucket(cost: int) -> str:
    r"""Return an interval including a given positive number.

    The intervals are predefined as \([0, 0], ]0, 0.25[, [2^{i-2}, 2^{i-1}[, \dots\) for all
    natural numbers \(i\). The result is returned as a string ready to be included in the
    recommendation report.

    Examples:
        >>> cost_bucket(0)
        "0"
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

    Examples:
        >>> couple_to_string((12, 15))
        "12-15"
        >>> couple_to_string((12, 12))
        "12"
        >>> couple_to_string(Span(12, 15))
        "12-15"
    """
    return f"{couple[0]}" + ("" if couple[0] == couple[1] else f"-{couple[1]}")


def print_warning(message: str):
    """Print the given message on `sys.stderr`."""
    print(f"Warning: {message}", file=sys.stderr)
