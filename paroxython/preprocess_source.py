from collections import defaultdict
from token import DEDENT, INDENT, NEWLINE, STRING
from tokenize import COMMENT, NL, generate_tokens
from typing import Callable, Dict, List, Tuple, Set

import regex  # type: ignore

from .user_types import LabelName, LabelsSpans, Source, Span

HINT_COMMENT = "# paroxython:"

sub_main = regex.compile(r"(?ms)^if +__name__ *== *.__main__. *:.+").sub
sub_first_comments = regex.compile(r"\A(#.*\n)*").sub
sub_blank_lines = regex.compile(r"\s*\n").sub
sub_pass = regex.compile(r"(?m)^( *)pass\n\1(?!\s)").sub
sub_final_pass = regex.compile(r"(?m)^ *pass\Z").sub
subn_paroxython_comment = regex.compile(r"(?i)#\s*paroxython\s*:\s*").subn


def cleanup_factory(cleanup_strategy: str) -> Callable[[Source], Source]:
    cleanup = lambda source: source
    if cleanup_strategy == "full":
        cleanup = lambda source: sub_main("", full_cleaning(source))
    return cleanup


def full_cleaning(source: Source) -> Source:
    result = []
    previous_token = INDENT
    (previous_end_row, previous_end_col) = (-1, 0)
    lines = iter(sub_first_comments("", source).replace("\t", "    ").split("\n"))
    for token_info in generate_tokens(lambda: next(lines) + "\n"):
        (token, string, (start_row, start_col), (end_row, end_col), _) = token_info
        if start_row > previous_end_row:
            previous_end_col = 0
        result.append(" " * max(0, start_col - previous_end_col))
        if token == COMMENT:
            (string, n) = subn_paroxython_comment(f"{HINT_COMMENT} ", string)
            if n == 0:
                continue
            result.append(string)
        elif token == STRING and previous_token in (INDENT, DEDENT, NEWLINE):
            result.append("pass\n")  # replace the docstring by a pass statement
        else:
            result.append(string)
        if (previous_token, token) == (NEWLINE, NL):
            previous_token = NEWLINE
        else:
            previous_token = token
        (previous_end_row, previous_end_col) = (end_row, end_col)
    text = "".join(result).strip()
    text = sub_blank_lines("\n", text)
    text = sub_pass(r"\1", text)  # suppress most useless pass statements
    return Source(text)


class HintBuffer:
    """Layer on the operations of appending, opening and closing an hint."""

    def __init__(self, description: str) -> None:
        self.result: LabelsSpans = defaultdict(list)
        self.stack: Dict[LabelName, List[int]] = defaultdict(list)
        self.description = description

    def append_hint(self, label_name: LabelName, line_number: int) -> None:
        """Label a span consisting in the given line number."""
        self.result[label_name].append(Span(line_number, line_number))

    def open_hint(self, label_name: LabelName, line_number: int) -> None:
        self.stack[label_name].append(line_number)

    def get_champion(self, label_name: LabelName) -> List[Tuple[int, "HintBuffer"]]:
        """Return the last line number (if any) of the opening label, plus itself."""
        return [(self.stack[label_name][-1], self)] if self.stack[label_name] else []

    def close_hint(self, label_name: LabelName, line_number: int) -> None:
        """Label a span opened above and closed on the given line number."""
        self.result[label_name].append(Span(self.stack[label_name].pop(), line_number))

    def ensure_stack_is_empty(self) -> None:
        """Raise an error iff there remains at least one open label."""
        if any(self.stack.values()):
            raise ValueError(f"Unmatched opening hints for {self.description}: {self.stack}.")

    def get_result(self) -> LabelsSpans:
        """Return the result with sorted spans."""
        return {k: sorted(v) for (k, v) in self.result.items()}


label_pattern = regex.compile(r"^(\W*)([\w:]+)(\W*)$")


def collect_hints(source: Source) -> Tuple[LabelsSpans, LabelsSpans]:
    """Schedule for addition or deletion the hints appearing in the comments."""
    addition = HintBuffer("addition")
    deletion = HintBuffer("deletion")
    for (i, line) in enumerate(source.split("\n"), 1):
        (_, separator, hints) = line.partition(f"{HINT_COMMENT} ")
        if not separator:
            continue
        for hint in hints.split():
            (before, label, after) = label_pattern.match(hint).groups()
            hint_parts = f"{before}/{label}/{after}"
            if before in ("", "+", "-"):
                buffer = deletion if before == "-" else addition
                if after == "":
                    buffer.append_hint(label, i)
                elif after in ("...", "…"):
                    buffer.open_hint(label, i)
                else:
                    raise ValueError(f"Illegal last part  for hint '{hint_parts}' on line {i}.")
            elif before in ("...", "…"):
                if after:
                    raise ValueError(f"Illegal last part for hint '{hint_parts}' on line {i}.")
                champions = addition.get_champion(label) + deletion.get_champion(label)
                if not champions:
                    raise ValueError(f"Unmatched closing hint '{hint_parts}' on line {i}.")
                max(champions)[1].close_hint(label, i)
            else:
                raise ValueError(f"Illegal first part for hint '{hint_parts}' on line {i}.")
    addition.ensure_stack_is_empty()
    deletion.ensure_stack_is_empty()
    return (addition.get_result(), deletion.get_result())


match_isolated_hints = regex.compile(fr"\s*{HINT_COMMENT} (.+)").match


def centrifugate_hints(source: Source) -> Source:
    """Transform the isolated hints into all-encompassing hints."""
    lines = []
    hints: Set[str] = set()
    for line in source.split("\n"):
        m = match_isolated_hints(line)
        if m:
            hints.update(m[1].split())
        else:
            lines.append(line)
    if not hints:
        return source
    for i in (0, -1):
        if f" {HINT_COMMENT}" not in lines[i]:
            lines[i] += f" {HINT_COMMENT}"
    for hint in sorted(hints):
        lines[0] += f" {hint}..."
        lines[-1] += f" ...{hint}"
    return Source("\n".join(lines))


replace_hints = regex.compile(fr"\s*{HINT_COMMENT} .*").sub


def remove_hints(source: Source) -> Source:
    return replace_hints("", source).strip()


if __name__ == "__main__":
    source = open("../Python/maths/matrix_exponentiation.py").read()
    lines = source.split("\n")
    lines[13] += f" {HINT_COMMENT} test"
    source = Source("\n".join(lines))
    print(source)
    print("-" * 80)
    print(full_cleaning(source))
