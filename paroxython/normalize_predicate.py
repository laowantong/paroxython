from typing import Tuple

import regex  # type: ignore

from .compare_spans import compare_spans
from .goodies import print_warning
from .user_types import Predicate


def normalize_predicate(predicate: str) -> Tuple[Predicate, bool]:
    """Ensure that the given predicate is correct or can be salvaged."""
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
    predicate = predicate.strip()
    if predicate not in compare_spans:
        # If there is only one x (resp. y), expand it into x≤x (resp. y≤y)
        predicate = regex.sub(r"^([^x]*)x([^x]*)$", r"\1x≤x\2", predicate)
        predicate = regex.sub(r"^([^y]*)y([^y]*)$", r"\1y≤y\2", predicate)
        # Convert usual comparison operators
        predicate = predicate.replace("<=", "≤").replace("==", "=")
        # Ignore all other characters
        predicate = regex.sub(r"[^xy<=≤]", "", predicate)
        if predicate != predicate:  # pragma: no cover
            print_warning(f"predicate '{predicate}' normalized into '{predicate}'.")
        if predicate not in compare_spans:
            raise ValueError(f"Malformed predicate '{predicate}' in the pipeline.")
    return (compare_spans[predicate], negated)
