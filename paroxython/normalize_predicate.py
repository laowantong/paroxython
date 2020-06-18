"""Process an input string to interpret it as a known predicate."""

from typing import Tuple

import regex  # type: ignore

from .compare_spans import compare_spans
from .goodies import print_warning
from .user_types import Predicate


def normalize_predicate(predicate: str) -> Tuple[Predicate, bool]:
    """Ensure that the given predicate is correct or can be salvaged.

    Description:
        The system first determines whether the predicate is negated or not, which can be expressed
        either by an exclamation mark prefix or the word “not”. In this case, the negation marker
        is extracted from the given string.

        The resulting string is then normalized, _i.e._ replaced by a key of the dictionary
        `compare_spans` defined in `paroxython.compare_spans`.
        .. include:: ../docs/md/pipeline_documentation.md
            :start-after: user input.
            :end-before: ### Positive semantic triples

    Examples:
        Browse
        [`test_normalize_predicate.py`](https://github.com/laowantong/paroxython/blob/master/tests/test_normalize_predicate.py)
        on GitHub.

    Args:
        predicate (str): Plain string to be interpreted as a predicate.

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
    elif regex.search(r"not\s+", predicate):
        predicate = predicate.replace("not ", "")
    elif regex.search(r"\s+not", predicate):
        predicate = predicate.replace(" not", "")
    else:
        negated = False
    original = predicate = predicate.strip()
    predicate = regex.sub(r" is\b|\bis ", "", predicate)
    if predicate not in compare_spans:
        # Convert usual comparison operators
        predicate = predicate.replace("<=", "≤").replace("==", "=")
        # Ignore all other characters
        predicate = regex.sub(r"[^xy<=≤]", "", predicate)
        # Treat the special case of identity
        predicate = regex.sub(r"^(x=y|y=)$", "x=y≤x=y", predicate)
        # If there is only one x (resp. y), expand it into x≤x (resp. y≤y)
        predicate = regex.sub(r"^([^x]*)x([^x]*)$", r"\1x≤x\2", predicate)
        predicate = regex.sub(r"^([^y]*)y([^y]*)$", r"\1y≤y\2", predicate)
        if original != predicate:  # pragma: no cover
            print_warning(f"predicate '{original}' normalized into '{predicate}'.")
        if predicate not in compare_spans:
            raise ValueError(f"Malformed predicate '{predicate}' in the pipeline.")
    return (compare_spans[predicate], negated)
