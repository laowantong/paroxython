"""
.. tip::
    Several functions declare a compiled and bound regex pattern as an optional argument. It is not
    meant to be provided by the caller. Its default value will be used systematically, with the
    benefit of being evaluated only once.
"""

from collections import defaultdict
from token import DEDENT, INDENT, NEWLINE, STRING
from tokenize import COMMENT, NL, generate_tokens
from typing import Callable, Dict, List, Tuple, Set

import regex  # type: ignore

from .user_types import LabelName, LabelsSpans, Source, Span

HINT_COMMENT = "# paroxython:"


class Cleanup:
    def __init__(self, cleanup_strategy: str):
        """Collection of cleaning static methods to be applied to a source code.

        The constructor selects the desired transformation.

        Args:
            cleanup_strategy (str): The name of the transformation. Currently, any other name than
                `"full"` (corresponding to `full_cleaning()` comes down to the identity function).

        Returns:
            Callable[[Source], Source]: A function that will clean up a given source code.
        """
        self.run = lambda source: source
        if cleanup_strategy == "full":
            self.run = Cleanup.full_cleaning

    @staticmethod
    def full_cleaning(source: Source) -> Source:
        r"""Remove as much noise (comments, etc.) as possible in the given source code.

        1. Suppress initial comments.
        2. Suppress `if __name__ == '__main__'` part.
        3. Replace tabulations with spaces.
        4. Normalize Paroxython hint comments.
        5. Replace docstrings with `pass` statements (most of which being suppressed at the end of the
        process).
        6. Suppress empty or blank lines.
        7. Suppress useless `pass` statements.

        Args:
            source (Source): The source to be cleaned.

        Returns:
            Source: The cleaned source.

        Examples:
            - Empty or blank lines are suppressed.
            <div><div style="display: inline-block; width: 49%;; vertical-align: top"><script src="https://gist-it.appspot.com/github.com/laowantong/paroxython/raw/master/tests/test_cleanup_source.py?slice=13:18&footer=0"></script></div> <div style="display: inline-block; width: 49%;; vertical-align: top"><script src="https://gist-it.appspot.com/github.com/laowantong/paroxython/raw/master/tests/test_cleanup_source.py?slice=19:21&footer=0"></script></div></div>
            - Normal inline comments are suppressed.
            <div><div style="display: inline-block; width: 49%;; vertical-align: top"><script src="https://gist-it.appspot.com/github.com/laowantong/paroxython/raw/master/tests/test_cleanup_source.py?slice=24:29&footer=0"></script></div> <div style="display: inline-block; width: 49%;; vertical-align: top"><script src="https://gist-it.appspot.com/github.com/laowantong/paroxython/raw/master/tests/test_cleanup_source.py?slice=30:35&footer=0"></script></div></div>
            - Commented lines are suppressed.
            <div><div style="display: inline-block; width: 49%;; vertical-align: top"><script src="https://gist-it.appspot.com/github.com/laowantong/paroxython/raw/master/tests/test_cleanup_source.py?slice=38:48&footer=0"></script></div> <div style="display: inline-block; width: 49%;; vertical-align: top"><script src="https://gist-it.appspot.com/github.com/laowantong/paroxython/raw/master/tests/test_cleanup_source.py?slice=49:52&footer=0"></script></div></div>
            - Shebang is suppressed.
            <div><div style="display: inline-block; width: 49%;; vertical-align: top"><script src="https://gist-it.appspot.com/github.com/laowantong/paroxython/raw/master/tests/test_cleanup_source.py?slice=55:57&footer=0"></script></div> <div style="display: inline-block; width: 49%;; vertical-align: top"><script src="https://gist-it.appspot.com/github.com/laowantong/paroxython/raw/master/tests/test_cleanup_source.py?slice=58:59&footer=0"></script></div></div>
            - Encoding declaration is suppressed.
            <div><div style="display: inline-block; width: 49%;; vertical-align: top"><script src="https://gist-it.appspot.com/github.com/laowantong/paroxython/raw/master/tests/test_cleanup_source.py?slice=62:64&footer=0"></script></div> <div style="display: inline-block; width: 49%;; vertical-align: top"><script src="https://gist-it.appspot.com/github.com/laowantong/paroxython/raw/master/tests/test_cleanup_source.py?slice=65:66&footer=0"></script></div></div>
            - Docstrings of classes and functions are suppressed.
            <div><div style="display: inline-block; width: 49%;; vertical-align: top"><script src="https://gist-it.appspot.com/github.com/laowantong/paroxython/raw/master/tests/test_cleanup_source.py?slice=69:80&footer=0"></script></div> <div style="display: inline-block; width: 49%;; vertical-align: top"><script src="https://gist-it.appspot.com/github.com/laowantong/paroxython/raw/master/tests/test_cleanup_source.py?slice=81:86&footer=0"></script></div></div>
            - Docstrings of modules are suppressed.
            <div><div style="display: inline-block; width: 49%;; vertical-align: top"><script src="https://gist-it.appspot.com/github.com/laowantong/paroxython/raw/master/tests/test_cleanup_source.py?slice=89:99&footer=0"></script></div> <div style="display: inline-block; width: 49%;; vertical-align: top"><script src="https://gist-it.appspot.com/github.com/laowantong/paroxython/raw/master/tests/test_cleanup_source.py?slice=100:104&footer=0"></script></div></div>
            - A `pass` statement is added to empty classes if needed.
            <div><div style="display: inline-block; width: 49%;; vertical-align: top"><script src="https://gist-it.appspot.com/github.com/laowantong/paroxython/raw/master/tests/test_cleanup_source.py?slice=107:112&footer=0"></script></div> <div style="display: inline-block; width: 49%;; vertical-align: top"><script src="https://gist-it.appspot.com/github.com/laowantong/paroxython/raw/master/tests/test_cleanup_source.py?slice=113:115&footer=0"></script></div></div>
            - Useless `pass` statements are suppressed.
            <div><div style="display: inline-block; width: 49%;; vertical-align: top"><script src="https://gist-it.appspot.com/github.com/laowantong/paroxython/raw/master/tests/test_cleanup_source.py?slice=118:126&footer=0"></script></div> <div style="display: inline-block; width: 49%;; vertical-align: top"><script src="https://gist-it.appspot.com/github.com/laowantong/paroxython/raw/master/tests/test_cleanup_source.py?slice=127:133&footer=0"></script></div></div>
            - Mixes of comments and docstrings are suppressed.
            <div><div style="display: inline-block; width: 49%;; vertical-align: top"><script src="https://gist-it.appspot.com/github.com/laowantong/paroxython/raw/master/tests/test_cleanup_source.py?slice=136:140&footer=0"></script></div> <div style="display: inline-block; width: 49%;; vertical-align: top"><script src="https://gist-it.appspot.com/github.com/laowantong/paroxython/raw/master/tests/test_cleanup_source.py?slice=141:142&footer=0"></script></div></div>
            - Paroxython's label hints are **preserved** and **normalized**.
            <div><div style="display: inline-block; width: 49%;; vertical-align: top"><script src="https://gist-it.appspot.com/github.com/laowantong/paroxython/raw/master/tests/test_cleanup_source.py?slice=145:151&footer=0"></script></div> <div style="display: inline-block; width: 49%;; vertical-align: top"><script src="https://gist-it.appspot.com/github.com/laowantong/paroxython/raw/master/tests/test_cleanup_source.py?slice=152:158&footer=0"></script></div></div>
            - `if __name__ == "__main__":` part is suppressed.
            <div><div style="display: inline-block; width: 49%;; vertical-align: top"><script src="https://gist-it.appspot.com/github.com/laowantong/paroxython/raw/master/tests/test_cleanup_source.py?slice=161:164&footer=0"></script></div> <div style="display: inline-block; width: 49%;; vertical-align: top"><script src="https://gist-it.appspot.com/github.com/laowantong/paroxython/raw/master/tests/test_cleanup_source.py?slice=165:166&footer=0"></script></div></div>

        .. warning::
            Useless pass statements are preserved when they are not followed by a line with a same
            indentation level.
        """
        result = []
        previous_token = INDENT
        (previous_end_row, previous_end_col) = (-1, 0)
        source = Cleanup.suppress_first_comments(source)
        source = Cleanup.suppress_name_equals_main_stuff(source)
        source = source.replace("\t", "    ")
        lines = iter(source.split("\n"))
        for token_info in generate_tokens(lambda: next(lines) + "\n"):
            (token, string, (start_row, start_col), (end_row, end_col), _) = token_info
            if start_row > previous_end_row:
                previous_end_col = 0
            result.append(" " * max(0, start_col - previous_end_col))
            if token == COMMENT:
                (string, n) = Cleanup.normalize_paroxython_comments(string)
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
        text = Cleanup.suppress_blank_lines(text)
        text = Cleanup.suppress_useless_pass_statements(text)
        return Source(text)

    @staticmethod
    def suppress_first_comments(source: str, sub=regex.compile(r"\A(#.*\n)*").sub) -> str:
        """Replace all comments placed on the first lines of the source code."""
        return sub("", source)

    @staticmethod
    def suppress_name_equals_main_stuff(
        source: str, sub: Callable = regex.compile(r"(?ms)^if +__name__ *== *.__main__. *:.+").sub
    ) -> str:
        """Suppress `if __name__ == '__main__'` part."""
        return sub("", source)

    @staticmethod
    def normalize_paroxython_comments(
        source: str,
        subn: Callable = regex.compile(
            r"\s*".join(regex.split(r"\b", regex.sub(r"\s+", "", HINT_COMMENT))) + r"\s*",
            regex.IGNORECASE,
        ).subn,
    ) -> str:
        r"""Replace and count all the hint comment strings, made space- and case-insensitive.

        For instance, if `HINT_COMMENT` is `"# paroxython:"` (its default value), the actual search
        pattern will be `r"(?i)#\s*paroxython\s*:\s*"`.
        """
        return subn(f"{HINT_COMMENT} ", source)

    @staticmethod
    def suppress_blank_lines(source: str, sub: Callable = regex.compile(r"\s*\n").sub) -> str:
        """Suppress all empty or blank lines in the given source."""
        return sub("\n", source)

    @staticmethod
    def suppress_useless_pass_statements(
        source: str, sub: Callable = regex.compile(r"(?m)^( *)pass\n\1(?!\s)").sub,
    ) -> str:
        """Suppress all `pass` statements followed by a line with a same level of indentation."""
        return sub(r"\1", source)


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


def match_label(hint: str, match: Callable = regex.compile(r"^(\W*)([\w:]+)(\W*)$").match):
    return match(hint)


def collect_hints(source: Source) -> Tuple[LabelsSpans, LabelsSpans]:
    """Schedule for addition or deletion the hints appearing in the comments."""
    addition = HintBuffer("addition")
    deletion = HintBuffer("deletion")
    for (i, line) in enumerate(source.split("\n"), 1):
        (_, separator, hints) = line.partition(f"{HINT_COMMENT} ")
        if not separator:
            continue
        for hint in hints.split():
            (before, label, after) = match_label(hint).groups()
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


def match_isolated_hints(
    line: str, match: Callable = regex.compile(fr"\s*{HINT_COMMENT} (.+)").match
) -> str:
    """Match all hints isolated on their own lines."""
    return match(line)


def centrifugate_hints(source: Source) -> Source:
    """Transform the isolated hints into all-encompassing hints.

    When a hint is isolated on its own line, it is considered to extend to the entire program.
    These hints are moved to both ends of the source, and made open on the first line and close on
    the last line.

    Args:
        source (Source): The source to be centrifugated.

    Returns:
        Source: A centrifugated source.

    Examples:
        - Some isolated hints (`hint_3` and `hint_5` are centrifugated).
        <div><div style="display: inline-block; width: 49%;; vertical-align: top"><script src="https://gist-it.appspot.com/github.com/laowantong/paroxython/raw/master/tests/test_centrifugate_hints.py?slice=10:17&footer=0"></script></div> <div style="display: inline-block; width: 49%;; vertical-align: top"><script src="https://gist-it.appspot.com/github.com/laowantong/paroxython/raw/master/tests/test_centrifugate_hints.py?slice=18:23&footer=0"></script></div></div>
        - Some trailing isolated hints (`hint_5` and `hint_6` are centrifugated).
        <div><div style="display: inline-block; width: 49%;; vertical-align: top"><script src="https://gist-it.appspot.com/github.com/laowantong/paroxython/raw/master/tests/test_centrifugate_hints.py?slice=26:33&footer=0"></script></div> <div style="display: inline-block; width: 49%;; vertical-align: top"><script src="https://gist-it.appspot.com/github.com/laowantong/paroxython/raw/master/tests/test_centrifugate_hints.py?slice=34:39&footer=0"></script></div></div>
        - No isolated hints (no centrifugation of the existing hints).
        <div><div style="display: inline-block; width: 49%;; vertical-align: top"><script src="https://gist-it.appspot.com/github.com/laowantong/paroxython/raw/master/tests/test_centrifugate_hints.py?slice=42:47&footer=0"></script></div> <div style="display: inline-block; width: 49%;; vertical-align: top"><script src="https://gist-it.appspot.com/github.com/laowantong/paroxython/raw/master/tests/test_centrifugate_hints.py?slice=48:53&footer=0"></script></div></div>
    """
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


def remove_hints(
    source: Source, sub_hints: Callable = regex.compile(fr"\s*{HINT_COMMENT} .*").sub,
) -> Source:
    """Remove all Paroxython hints from the given source.

    Args:
        source (Source): The source, already processed for its hints.
        replace_hints (Callable, optional): A function replacing all hints.

    Returns:
        Source: The source deprived from its hints.
    """
    return Source(sub_hints("", source).strip())


if __name__ == "__main__":
    source = open("../Python/maths/matrix_exponentiation.py").read()
    lines = source.split("\n")
    lines[13] += f" {HINT_COMMENT} test"
    source = Source("\n".join(lines))
    cleanup = Cleanup("full").run
    print(source)
    print("-" * 80)
    print(cleanup(source))
