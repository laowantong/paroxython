"""
Bring together everything relative to the pre-processing of a given source code.

## Cleaning

A useful, albeit not essential, step is to cleanse the code of all its algorithmically irrelevant
features (blank lines, comments, docstrings, etc.). Lots of examples are provided in the `Cleanup`
class documentation. Be aware that a certain category of comment is intentionally preserved at this
stage, the so-called “manual hints”, presented in the next paragraph.

## Manual hints

On a given source code, the labelling algorithm may sometimes produce false positives or false
negatives. Moreover, the semantics of some features may be subjective (e.g., `topic:fun`) or beyond
the capabilities of Paroxython (e.g., deciding the relevance of the `short_circuit` property of a
boolean condition). In any case, the user has the possibility to manually label certain lines of
their source code to hint either the presence or absence of a given feature.

The addition of a label is hinted by a comment starting with `# paroxython:`.

>>> if i < len(s) and s[i] == x: # paroxython: +short_circuit:And

Note that `short_circuit:And` is a label (of the kind defined, but not necessarily included in
[spec.md](https://repo/paroxython/resources/spec.md)), and
not a taxon. It will be later converted into one or more taxa (according to the mapping of
[taxonomy.tsv](https://repo/paroxython/resources/taxonomy.tsv)).

To delete a label, prefix it with a minus symbol. For instance, the following hint requalifies an
addition into a concatenation:

>>> print(a + b) # paroxython: -addition_operator +concatenation_operator

If a label should span over several lines, it is hinted on the first line with a `...` suffix
(meaning “to be continued”), and on the last line with a `...` prefix (meaning “continuing”). In the
following example, a label `super_loop` is manually substituted to the calculated label `loop:for`:

>>> for x in s: # paroxython: +super_loop... -loop:for...
...     foo()
...     bar() # paroxython: ...super_loop ...loop:for

Of course, the opening and the closing of a spanning label must be correctly balanced.

Some tolerances exist for the syntax:

- `+` can be omitted.
- `...` (three dots) can be written `…` (HORIZONTAL ELLIPSIS, U+2026).
- `# paroxython:` is neither space- nor case-sensitive.
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

        Description:
            1. Suppress initial comments.
            2. Suppress `if __name__ == '__main__'` part.
            3. Replace tabulations with spaces.
            4. Normalize Paroxython hint comments.
            5. Replace docstrings with `pass` statements (most of which being suppressed at the end
               of the process).
            6. Suppress empty or blank lines.
            7. Suppress useless `pass` statements.

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

            All examples above automatically extracted from
            [test_cleanup_source.py](https://repo/tests/test_cleanup_source.py).

        .. warning::
            Useless pass statements are preserved when they are not followed by a line with a same
            indentation level.
        """
        result = []
        previous_token = INDENT
        (previous_end_row, previous_end_col) = (-1, 0)
        text = str(source)
        text = Cleanup.suppress_first_comments(text)
        text = Cleanup.suppress_main_guard(text)
        text = text.replace("\t", "    ")
        lines = iter(text.split("\n"))
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
    def suppress_first_comments(
        source: str, sub: Callable = regex.compile(r"\A(#.*\n)*").sub
    ) -> str:
        """Replace all comments placed on the first lines of the source code.

        Argument `sub` [not to be explicitly provided.](docs_developer_manual/index.html#default-argument-trick)
        """
        return sub("", source)

    @staticmethod
    def suppress_main_guard(
        source: str, sub: Callable = regex.compile(r"(?ms)^if +__name__ *== *.__main__. *:.+").sub
    ) -> str:
        """Suppress `if __name__ == '__main__'` part.

        Argument `sub` [not to be explicitly provided.](docs_developer_manual/index.html#default-argument-trick)
        """
        return sub("", source)

    @staticmethod
    def normalize_paroxython_comments(
        source: str,
        subn: Callable = regex.compile(
            r"\s*".join(regex.split(r"(\w+)", HINT_COMMENT.replace(" ", ""))) + r"\s*",
            regex.IGNORECASE,
        ).subn,
    ) -> str:
        r"""Replace and count all the hint comment strings, made space- and case-insensitive.

        For instance, if `HINT_COMMENT` is `"# paroxython:"` (its default value), the actual search
        pattern will be `r"(?i)#\s*paroxython\s*:\s*"`.

        Argument `subn` [not to be explicitly provided.](docs_developer_manual/index.html#default-argument-trick)
        """
        return subn(f"{HINT_COMMENT} ", source)

    @staticmethod
    def suppress_blank_lines(source: str, sub: Callable = regex.compile(r"\s*\n").sub) -> str:
        """Suppress all empty or blank lines in the given source.

        Argument `sub` [not to be explicitly provided.](docs_developer_manual/index.html#default-argument-trick)
        """
        return sub("\n", source)

    @staticmethod
    def suppress_useless_pass_statements(
        source: str, sub: Callable = regex.compile(r"(?m)^( *)pass\n\1(?!\s)").sub,
    ) -> str:
        """Suppress all `pass` statements followed by a line with a same level of indentation.

        Argument `sub` [not to be explicitly provided.](docs_developer_manual/index.html#default-argument-trick)
        """
        return sub(r"\1", source)


def centrifugate_hints(
    source: Source, match_isolated_hints: Callable = regex.compile(fr"\s*{HINT_COMMENT} (.+)").match
) -> Source:
    """Transform the isolated hints into all-encompassing hints.

    Description:
        When a hint is isolated on its own line, it is considered to extend to the entire program.
        These hints are moved to both ends of the source (centrifugated), and made open on the
        first line and close on the last line.

    Examples:
        - Some isolated hints (`hint_3` and `hint_5` are centrifugated).
        <div><div style="display: inline-block; width: 49%;; vertical-align: top"><script src="https://gist-it.appspot.com/github.com/laowantong/paroxython/raw/master/tests/test_centrifugate_hints.py?slice=10:17&footer=0"></script></div> <div style="display: inline-block; width: 49%;; vertical-align: top"><script src="https://gist-it.appspot.com/github.com/laowantong/paroxython/raw/master/tests/test_centrifugate_hints.py?slice=18:23&footer=0"></script></div></div>
        - Some trailing isolated hints (`hint_5` and `hint_6` are centrifugated).
        <div><div style="display: inline-block; width: 49%;; vertical-align: top"><script src="https://gist-it.appspot.com/github.com/laowantong/paroxython/raw/master/tests/test_centrifugate_hints.py?slice=26:33&footer=0"></script></div> <div style="display: inline-block; width: 49%;; vertical-align: top"><script src="https://gist-it.appspot.com/github.com/laowantong/paroxython/raw/master/tests/test_centrifugate_hints.py?slice=34:39&footer=0"></script></div></div>
        - No isolated hints (no centrifugation of the existing hints).
        <div><div style="display: inline-block; width: 49%;; vertical-align: top"><script src="https://gist-it.appspot.com/github.com/laowantong/paroxython/raw/master/tests/test_centrifugate_hints.py?slice=42:47&footer=0"></script></div> <div style="display: inline-block; width: 49%;; vertical-align: top"><script src="https://gist-it.appspot.com/github.com/laowantong/paroxython/raw/master/tests/test_centrifugate_hints.py?slice=48:53&footer=0"></script></div></div>

        All examples above automatically extracted from
        [test_centrifugate_hints.py](https://repo/tests/test_centrifugate_hints.py).

        Argument `match_isolated_hints` [not to be explicitly provided.](docs_developer_manual/index.html#default-argument-trick)
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


class HintBuffer:
    """Layer on the operations of appending, opening and closing a hint, used by `collect_hints`."""

    def __init__(self, description: str) -> None:
        self.result: LabelsSpans = defaultdict(list)
        self.stack: Dict[LabelName, List[int]] = defaultdict(list)
        self.description = description

    def append_hint(self, label_name: LabelName, line_number: int) -> None:
        """Label a span consisting in the given line number."""
        self.result[label_name].append(Span(line_number, line_number))

    def open_hint(self, label_name: LabelName, line_number: int) -> None:
        """Store the line number associated with a given opening hint."""
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


def collect_hints(
    source: Source, match_label: Callable = regex.compile(r"^(\W*)([\w:]+)(\W*)$").match
) -> Tuple[LabelsSpans, LabelsSpans]:
    """Schedule for addition or deletion the hints appearing in the comments.

    Description:
        On this stage, the source code is scanned for manual hints. They are set aside in two
        separate containers (depending on whether the user intends to add or remove them). They
        will later be used to tweak the labelling results obtained by static analysis.

    Args:
        source (Source): A source code.
        match_label (Callable, optional): A function matching a label composed of alphanumeric
            characters and colons. [Not to be explicitly provided.](docs_developer_manual/index.html#default-argument-trick)

    Raises:
        ValueError: Raised in various cases of malformed input.

    Returns:
        Tuple[LabelsSpans, LabelsSpans]: A couple of dictionaries associating labels with lists of
            spans. The first [resp. second] member collects the labels that the source code author
            has manually added [resp. suppressed].

    Example:
        >>> source = '''
        ...     1   foo() # paroxython: +hint_1...
        ...     2   bar() # paroxython: hint_2 hint_3 -hint_4
        ...     3   biz() # paroxython: ...hint_1
        ...     4   buz() # paroxython: -hint_2
        ... '''
        >>> collect_hints(source)
        (
            {
                "hint_1": [Span(start=1, end=3)],
                "hint_2": [Span(start=2, end=2)],
                "hint_3": [Span(start=2, end=2)],
            },
            {
                "hint_2": [Span(start=4, end=4)],
                "hint_4": [Span(start=2, end=2)],
            },
        )
        ```
    """
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


def remove_hints(
    source: Source, sub_hints: Callable = regex.compile(fr"\s*{HINT_COMMENT} .*").sub,
) -> Source:
    """Once they are collected, remove all Paroxython hints from the given source.

    Argument `sub_hints` [not to be explicitly provided.](docs_developer_manual/index.html#default-argument-trick)
    """
    return Source(sub_hints("", source).strip())
