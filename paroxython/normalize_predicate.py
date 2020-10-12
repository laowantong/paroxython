"""Process an input string to interpret it as a known predicate."""

from typing import Callable, Tuple

import regex  # type: ignore

from .compare_spans import compare_spans
from .goodies import print_warning, print_fail
from .user_types import Predicate


def normalize_predicate(
    predicate: str,
    search_not_1: Callable = regex.compile(r"not\s+").search,
    search_not_2: Callable = regex.compile(r"\s+not").search,
    sub_is: Callable = regex.compile(r" is\b|\bis ").sub,
    sub_forbidden_chars: Callable = regex.compile(r"[^xy<=≤]").sub,
    sub_identity: Callable = regex.compile(r"^(x=y|y=x)$").sub,
    sub_one_x: Callable = regex.compile(r"^([^x]*)x([^x]*)$").sub,
    sub_one_y: Callable = regex.compile(r"^([^y]*)y([^y]*)$").sub,
) -> Tuple[Predicate, bool]:
    """Ensure that the given predicate is correct or can be salvaged.

    Description:
        The system first determines whether the predicate is negated or not, which can be expressed
        either by an exclamation mark prefix or the word “not”. In both cases, the negation marker
        is extracted from the given string.

        The resulting string is then normalized, i.e. replaced by a key of the dictionary
        `compare_spans` defined in `paroxython.compare_spans`.
        .. include:: ../docs/md/pipeline_documentation.md
            :start-after: user input.
            :end-before: ### Positive semantic triples

    Examples:
        Browse
        [`test_normalize_predicate.py`](https://repo/tests/test_normalize_predicate.py)
        on GitHub.

    Args:
        predicate (str): Plain string to be interpreted as a predicate.
        search_not_1 (Callable, optional): Function searching `"not "`.
        search_not_2 (Callable, optional): Function searching `" not"`.
        sub_is (Callable, optional): Function replacing `" is"` or `"is "`.
        sub_forbidden_chars (Callable, optional): Function replacing all characters not in `"xy<=≤"`.
        sub_identity (Callable, optional): Function replacing `"x=y"` or `"y=x"`.
        sub_one_x (Callable, optional): Function replacing isolated`"x"`.
        sub_one_y (Callable, optional): Function replacing isolated`"y"`.

    Note:
        [No default argument to be explicitly provided.](developer_manual/index.html#default-argument-trick)

    Raises:
        ValueError: Raised when the input string is malformed beyond recognition.

    Returns:
        Tuple[Predicate, bool]: A tuple whose first member is a function (more precisely, a value
            of the dictionary `compare_spans`), and second member is a boolean indicating whether
            the result of this predicate must be negated.
    """
    predicate = predicate.lower().strip()
    negated = True
    if predicate.startswith("!"):
        predicate = predicate[1:]
    elif search_not_1(predicate):
        predicate = predicate.replace("not ", "")
    elif search_not_2(predicate):
        predicate = predicate.replace(" not", "")
    else:
        negated = False
    original = predicate = predicate.strip()
    predicate = sub_is("", predicate)  # Suppress "is" when it is followed or preceded by a space.
    if predicate not in compare_spans:
        predicate = predicate.replace("<=", "≤").replace("==", "=")  # Convert usual operators.
        predicate = sub_forbidden_chars("", predicate)  # Ignore all other characters.
        predicate = sub_identity("x=y≤x=y", predicate)  # Treat the special case of identity.
        predicate = sub_one_x(r"\1x≤x\2", predicate)  # If there is only one x, expand it into x≤x.
        predicate = sub_one_y(r"\1y≤y\2", predicate)  # If there is only one y, expand it into y≤y.
        if original != predicate:
            print_warning(f"predicate '{original}' normalized into '{predicate}'.")
        if predicate not in compare_spans:
            print_fail(f"Malformed predicate '{predicate}' in the pipeline.")
    return (compare_spans[predicate], negated)
