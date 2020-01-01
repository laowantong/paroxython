from collections import defaultdict
from typing import Dict, List, Tuple

import regex  # type: ignore

from declarations import LabelName, LabelsSpans, Source
from span import Span


class HintBuffer:
    """Layer on the operations of appending, opening and closing an hint."""

    def __init__(self, description: str) -> None:
        self.result: LabelsSpans = defaultdict(list)
        self.stack: Dict[LabelName, List[int]] = defaultdict(list)
        self.description = description

    def append_hint(self, label_name: LabelName, line_number: int) -> None:
        """Label a span consisting in the given line number."""
        self.result[label_name].append(Span([line_number]))

    def open_hint(self, label_name: LabelName, line_number: int) -> None:
        self.stack[label_name].append(line_number)

    def get_champion(self, label_name: LabelName) -> List[Tuple[int, "HintBuffer"]]:
        """Return the last line number (if any) of the opening label, plus itself."""
        return [(self.stack[label_name][-1], self)] if self.stack[label_name] else []

    def close_hint(self, label_name: LabelName, line_number: int) -> None:
        """Label a span opened above and closed on the given line number."""
        self.result[label_name].append(Span([self.stack[label_name].pop(), line_number]))

    def ensure_stack_is_empty(self) -> None:
        """Raise an error iff there remains at least one open label."""
        if any(self.stack.values()):
            raise ValueError(f"Unmatched opening hints for {self.description}: {self.stack}.")

    def get_result(self) -> LabelsSpans:
        """Return the result with sorted spans."""
        return {k: sorted(v) for (k, v) in self.result.items()}


def retrieve_manual_hints(source: Source) -> Tuple[LabelsSpans, LabelsSpans]:
    """Schedule for addition or deletion the hints appearing in the comments."""
    addition = HintBuffer("addition")
    deletion = HintBuffer("deletion")
    for (i, line) in enumerate(source.split("\n"), 1):
        (_, separator, hints) = line.partition("# paroxython: ")
        if not separator:
            continue
        for hint in hints.split():
            (prefix, label, suffix) = regex.split(r"(\w+(?::\w+)?)", hint, maxsplit=1)
            if prefix in ("", "+", "-"):
                buffer = deletion if prefix == "-" else addition
                if suffix == "":
                    buffer.append_hint(label, i)
                elif suffix in ("...", "…"):
                    buffer.open_hint(label, i)
                else:
                    raise ValueError(f"Illegal suffix for hint '{hint}' on line {i}.")
            elif prefix in ("...", "…"):
                if suffix:
                    raise ValueError(f"Illegal suffix for hint '{hint}' on line {i}.")
                champions = addition.get_champion(label) + deletion.get_champion(label)
                if not champions:
                    raise ValueError(f"Unmatched closing hint '{hint}' on line {i}.")
                max(champions)[1].close_hint(label, i)
            else:
                raise ValueError(f"Illegal prefix for hint '{hint}' on line {i}.")
    addition.ensure_stack_is_empty()
    deletion.ensure_stack_is_empty()
    return (addition.get_result(), deletion.get_result())
