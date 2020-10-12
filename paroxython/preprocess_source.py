"""
Bring together everything relative to the pre-processing of a given source code.

## Cleaning

A useful, albeit not essential, step is to cleanse the code of all its algorithmically irrelevant
features (blank lines, comments, docstrings, etc.). Lots of examples are provided in the `Cleanup`
class documentation below.

## Manual hints: preservation, centrifugation and scheduling

Certain comments intentionally survive the cleaning step, the so-called “manual hints”, introduced
[here](user_manual/index.html#manual-hints).

- If they appear at the end of a nonempty line of code, they are preserved as they are.
- If they extend over an entire line (excluding the initial blanks), they are considered to be
  featured by the entire program. They are replaced by two hints, one put at the beginning and
  the other at the end of the source code, thus delimiting the totality of the program. This
  operation is called “centrifugation”.

In either case, these hints were manually placed by the user to modify the behavior of Paroxython,
by asking it either to add the taxa that it missed, or to delete those that it unduly produced. This
is at this step that they are scheduled for addition or deletion (respectively). For the moment, the
information is just stored: `paroxython.parse_program.ProgramParser` will process it when required.
"""

from collections import defaultdict
from token import DEDENT, INDENT, NEWLINE, STRING
from tokenize import COMMENT, NL, generate_tokens
from typing import Callable, Dict, List, Tuple, Set

import regex  # type: ignore

from .goodies import print_fail
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
        r'''Remove as much noise (comments, etc.) as possible in the given source code.

        Description:
            1. Suppress initial comments.
            2. Suppress `if __name__ == '__main__'` part.
            3. Suppress `sys.path` injections (frequently used to simplify `import` behavior).
            4. Replace tabulations with spaces.
            5. Normalize Paroxython hint comments.
            6. Replace docstrings with `pass` statements (most of which being suppressed at the end
               of the process).
            7. Suppress empty or blank lines.
            8. Suppress useless `pass` statements.

        Examples:
            - Empty or blank lines are suppressed.
            ```python
            foo = bar


            bar = buzz

            ```
            ```python
            foo = bar
            bar = buzz
            ```
            - Normal inline comments are suppressed.
            ```python
            foo = bar # lorem ipsum
            fizz = [
                "foo", # lorem
                "bar", # ipsum
            ]
            ```
            ```python
            foo = bar
            fizz = [
                "foo",
                "bar",
            ]
            ```
            - Commented lines are suppressed.
            ```python
            # lorem ipsum
            # dolor amet
            def foo(bar):
                # lorem
                # ipsum
                if foo == bar:
                    # lorem
                    return []
                # lorem
            # ipsum
            ```
            ```python
            def foo(bar):
                if foo == bar:
                    return []
            ```
            - Shebang is suppressed.
            ```python
            #!/usr/bin/env python
            foobar()
            ```
            ```python
            foobar()
            ```
            - Encoding declaration is suppressed.
            ```python
            # coding=utf8
            foobar()
            ```
            ```python
            foobar()
            ```
            - Docstrings of classes and functions are suppressed.
            ```python
            class Foo:
                """Lorem.

                Ipsum dolor.
                """
                def foo(self, bar):
                    """Lorem ipsum."""
                    return 1
            def bar():
                """Ipsum dolor"""
                return 2
            ```
            ```python
            class Foo:
                def foo(self, bar):
                    return 1
            def bar():
                return 2
            ```
            - Docstrings of modules are suppressed.
            ```python
            """Lorem.

            Ipsum Dolor."""

            """Lorem ipsum dolor sic amet."""

            a = """consectetur
            adipiscing
            elit.
            """
            ```
            ```python
            a = """consectetur
            adipiscing
            elit.
            """
            ```
            - A `pass` statement is added to empty classes if needed.
            ```python
            class Foo:
                """Lorem.

                Ipsum dolor.
                """
            ```
            ```python
            class Foo:
                pass
            ```
            - Useless `pass` statements are suppressed.
            ```python
            foo()
            pass
            if bar():
                pass
            else:
                pass
                foobar()
                pass
            ```
            ```python
            foo()
            if bar():
                pass
            else:
                foobar()
                pass
            ```
            - Mixes of comments and docstrings are suppressed.
            ```python
            # Lorem
            # Ipsum
            """Dolor."""
            foobar()
            ```
            ```python
            foobar()
            ```
            - Paroxython's label hints are **preserved** and **normalized**.
            ```python
            foo = bar #   Paroxython   :   hint_1   hint_2
            #paroxython: hint_3
            fizz = [
                "foo", # lorem
                "bar", # paroxython: hint_4
            ]
            ```
            ```python
            foo = bar # paroxython: hint_1   hint_2
            # paroxython: hint_3
            fizz = [
                "foo",
                "bar", # paroxython: hint_4
            ]
            ```
            - `if __name__ == "__main__":` part is suppressed.
            ```python
            foo = bar
            if __name__ == "__main__":
                bar = foo
            ```
            ```python
            foo = bar
            ```
            - `sys.path` injections are suppressed.
            ```python
            __import__("sys").path[0:0] = ["programs"]
            (28433 * 2**7830457 + 1) % 10**10
            ```
            ```python
            (28433 * 2**7830457 + 1) % 10**10
            ```

            All examples above automatically extracted from
            [test_cleanup_source.py](https://repo/tests/test_cleanup_source.py).

        .. warning::
            Useless pass statements are preserved when they are not followed by a line with a same
            indentation level.
        '''
        result = []
        previous_token = INDENT
        (previous_end_row, previous_end_col) = (-1, 0)
        text = str(source)
        text = Cleanup.suppress_first_comments(text)
        text = Cleanup.suppress_main_guard(text)
        text = Cleanup.suppress_sys_path_injection(text)
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

        Argument `sub` [not to be explicitly provided.](developer_manual/index.html#default-argument-trick)
        """
        return sub("", source)

    @staticmethod
    def suppress_main_guard(
        source: str, sub: Callable = regex.compile(r"(?ms)^if +__name__ *== *.__main__. *:.+").sub
    ) -> str:
        """Suppress `if __name__ == '__main__'` part.

        Argument `sub` [not to be explicitly provided.](developer_manual/index.html#default-argument-trick)
        """
        return sub("", source)

    @staticmethod
    def suppress_sys_path_injection(
        source: str,
        sub: Callable = regex.compile(r'(?m)^__import__\("sys"\)\.path\[0:0\] = .+\n').sub,
    ) -> str:
        """Suppress lines starting with `__import__("sys").path[0:0] = `.

        Argument `sub` [not to be explicitly provided.](developer_manual/index.html#default-argument-trick)
        """
        return sub("", source)

    @staticmethod
    def normalize_paroxython_comments(
        source: str,
        subn: Callable = regex.compile(
            r"\s*".join(regex.split(r"(\w+)", HINT_COMMENT.replace(" ", ""))) + r"\s*",
            regex.IGNORECASE,
        ).subn,
    ) -> Tuple[str, int]:
        r"""Replace and count all the hint comment strings, made space- and case-insensitive.

        For instance, if `HINT_COMMENT` is `"# paroxython:"` (its default value), the actual search
        pattern will be `r"(?i)#\s*paroxython\s*:\s*"`.

        Argument `subn` [not to be explicitly provided.](developer_manual/index.html#default-argument-trick)
        """
        return subn(f"{HINT_COMMENT} ", source)

    @staticmethod
    def suppress_blank_lines(source: str, sub: Callable = regex.compile(r"\s*\n").sub) -> str:
        """Suppress all empty or blank lines in the given source.

        Argument `sub` [not to be explicitly provided.](developer_manual/index.html#default-argument-trick)
        """
        return sub("\n", source)

    @staticmethod
    def suppress_useless_pass_statements(
        source: str,
        sub: Callable = regex.compile(r"(?m)^( *)pass\n\1(?!\s)").sub,
    ) -> str:
        """Suppress all `pass` statements followed by a line with a same level of indentation.

        Argument `sub` [not to be explicitly provided.](developer_manual/index.html#default-argument-trick)
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
        ```python
        foo = bar # paroxython: hint_1 hint_2
        # paroxython: hint_3
        fizz = [
            "foo",
            "bar", # paroxython: hint_4
            # paroxython: hint_5
        ]
        ```
        ```python
        foo = bar # paroxython: hint_1 hint_2 hint_3... hint_5...
        fizz = [
            "foo",
            "bar", # paroxython: hint_4
        ] # paroxython: ...hint_3 ...hint_5
        ```
        - Some trailing isolated hints (`hint_5` and `hint_6` are centrifugated).
        ```python
        foo = bar # paroxython: hint_1 hint_2
        fizz = [
            "foo",
            "bar", # paroxython: hint_3
        ] # paroxython: hint_4
        # paroxython: hint_5
        # paroxython: hint_6
        ```
        ```python
        foo = bar # paroxython: hint_1 hint_2 hint_5... hint_6...
        fizz = [
            "foo",
            "bar", # paroxython: hint_3
        ] # paroxython: hint_4 ...hint_5 ...hint_6
        ```
        - No isolated hints (no centrifugation of the existing hints).
        ```python
        foo = bar # paroxython: hint_1 hint_2
        fizz = [
            "foo",
            "bar", # paroxython: hint_4
        ]
        ```
        ```python
        foo = bar # paroxython: hint_1 hint_2
        fizz = [
            "foo",
            "bar", # paroxython: hint_4
        ]
        ```

        All examples above automatically extracted from
        [test_centrifugate_hints.py](https://repo/tests/test_centrifugate_hints.py).

        Argument `match_isolated_hints` [not to be explicitly provided.](developer_manual/index.html#default-argument-trick)

    <center>
    <iframe src='https://gfycat.com/ifr/ExcellentKeyElver' frameborder='0' scrolling='no' width='320' height='266'></iframe>
    </center>
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
            print_fail(f"Unmatched opening hints for {self.description}: {self.stack}.")

    def get_result(self) -> LabelsSpans:
        """Return the result with sorted spans."""
        return {k: sorted(v) for (k, v) in self.result.items()}


def collect_hints(
    source: Source,
    match_label: Callable = regex.compile(r"^((?:-|\+|\.\.\.|…)?)(\w.*?)((?:\.\.\.|…)?)$").match,
) -> Tuple[LabelsSpans, LabelsSpans]:
    """Schedule for addition or deletion the hints appearing in the comments.

    Description:
        On this stage, the source code is scanned for manual hints. This function set them aside in
        two separate containers (depending on whether the user intends to add or remove them). They
        will later be used to tweak the labelling results obtained by static analysis.

    Args:
        source (Source): A source code.
        match_label (Callable, optional): A function matching a string:

            - optionally starting with `"+"`, `"-"`, `"..."` or `"…"`;
            - continuing with one alphanumeric character (`"[_0-9a-zA-Z]"`) and optionally a
              sequence of characters other than a newline (together they constitute the label);
            - optionally ending with `"..."` or `"…"`.

            [Not to be explicitly provided.](developer_manual/index.html#default-argument-trick)

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
            m = match_label(hint)
            if m is None:
                print_fail(f"Malformed hint '{hint}' on line {i}.")
            (before, label, after) = m.groups()
            if before in ("", "+", "-"):
                buffer = deletion if before == "-" else addition
                if after:
                    buffer.open_hint(label, i)
                else:
                    buffer.append_hint(label, i)
            else:  # `before` is in ("...", "…")
                if after:
                    print_fail(f"Illegal last part for hint {m.groups()} on line {i}.")
                champions = addition.get_champion(label) + deletion.get_champion(label)
                if not champions:
                    print_fail(f"Unmatched closing hint {m.groups()} on line {i}.")
                max(champions)[1].close_hint(label, i)
    addition.ensure_stack_is_empty()
    deletion.ensure_stack_is_empty()
    return (addition.get_result(), deletion.get_result())


def remove_hints(
    source: Source,
    sub_hints: Callable = regex.compile(fr"\s*{HINT_COMMENT} .*").sub,
) -> Source:
    """Once they are collected, remove all Paroxython hints from the given source.

    Argument `sub_hints` [not to be explicitly provided.](developer_manual/index.html#default-argument-trick)
    """
    return Source(sub_hints("", source).strip())
