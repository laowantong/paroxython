r"""Search a program for the features specified in `spec.md`."""

from collections import defaultdict
from os.path import dirname
from pathlib import Path
from typed_ast import ast3 as ast
from typing import Callable, Dict, List, Iterator, Tuple


import regex  # type: ignore

from .derived_labels_db import DerivedLabelsDatabase
from .flatten_ast import flatten_ast
from .user_types import (
    Label,
    LabelName,
    Labels,
    LabelsSpans,
    Program,
    Query,
    Source,
    Span,
)

__pdoc__ = {
    "ProgramParser": "",
    "ProgramParser.__init__": True,
    "ProgramParser.__call__": True,
    "foobar": True,
}


def find_all_features(
    specifications: str,
    find_all: Callable = regex.compile(
        r"(?ms)"
        r"^\#{4}\s+Feature\s+`(.+?)`"  # capture the label's pattern
        r".+?\#{5}\s+Specification"  # ensure the sequel is in the Specification section
        r".+?```(.*?)\n+(.*?)\n?```"  # capture the language and the specification
    ).findall,
) -> Iterator[Tuple[LabelName, str, str]]:
    """Iterate on all tuples defining an algorithmic feature in the given specification text.

    Args:
        specifications (str): Normally, the contents of
            [`spec.md`](https://repo/paroxython/resources/spec.md).
        find_all (Callable, optional): A function finding all feature-defining triples of the text.
            [Not to be explicitly provided.](docs_developer_manual/index.html#default-argument-trick)

    Returns:
        Iterator[Tuple[LabelName, str, str]]: An iterator yielding all matching triples of the form:

            1. label name pattern (e.g., `"try"` or `"try_raise|try_except"`),
            2. language (currently, `"re"` or `"sql"`),
            3. specification (respectively, a regular expression pattern or an SQL query).
    """
    return find_all(specifications)


def pos_to_span(pos: List[str]) -> Span:
    """Convert a list of positions (as captured in a specification string) into a single span.

    Args:
        pos (List[str]): A non-empty list of strings of the form `f"{line_number}:{path}"`

    Returns:
        Span: A named tuple consisting of:

            - `start`: the line number extracted from the first string;
            - `end`: the line number extracted from the last string (the same as `start` if there
                is only one string);
            - `path`: the path extracted from the first string.

            Note that all other substrings, if any, are ignored.

    Examples:
        >>> pos_to_span(["1:path_1"])
        Span(1, 1, "path_1")
        >>> pos_to_span(["1:path_1", "2:path_2"])
        Span(1, 2, "path_1")
        >>> pos_to_span(["1:path_1", "2:path_2", "3:path_3", "4:path_4"])
        Span(1, 4, "path_1")
    """
    (start, path) = pos[0].split(":")
    (end, _) = pos[-1].split(":")
    return Span(int(start), int(end), path)


DEFAULT_SPEC_PATH = Path(dirname(__file__)) / "resources" / "spec.md"


def get_bindings(
    label_prefix: LabelName, captures: Dict[str, List[str]]
) -> Iterator[Tuple[LabelName, Span]]:
    r"""Analyze the matches of a feature, and bind the corresponding names and spans.

    Args:
        label_prefix (LabelName): The name of a feature specified by a regular expression. Note that
            such a name is literal: contrary to those defined by an SQL query, they cannot include
            the alternation meta-character (`"|"`).
        captures (Dict[str, List[str]]): A dictionary of the named groups and lists of all the
            captures of those groups, as matched by the function `regex.finditer()`. Contains a
            non-empty entry `"POS"` and, optionally, an entry `"SUFFIX"`. All other entries are
            ignored.

    Yields:
        Iterator[Tuple[LabelName, Span]]: At least one binding between a label name and a span.

    Examples:
        The simplest cases happen when there is one or several `"POS"`, but no `"SUFFIX"`:

        >>> get_bindings("null_operation", {"POS": ["4:1-3-1-5-1-"]})
        ("null_operation", Span(start=4, end=4, path="1-3-1-5-1-"))
        >>> get_bindings("while", {"POS": ["11:2-", "16:2-1-4-2-1-2-"]})
        ("while", Span(start=11, end=16, path="2-"))
        >>> get_bindings("divisibility_test", {
        ...     "POS": ["15:3-5-1-2-1-0-"],
        ...     "SUFFIX": []
        ... })
        ("divisibility_test", Span(start=15, end=15, path="3-5-1-2-1-0-"))

        When there are as many `"POS"` than `"SUFFIX"`, they are binded pairwise. The
        resulting spans cannot span multiple lines:

        >>> get_bindings("literal", {
        ...     "POS": ["16:3-5-1-2-1-1-1-0-"],
        ...     "SUFFIX": ["False"],
        ... })
        ("literal:False", Span(start=16, end=16, path="3-5-1-2-1-1-1-0-"))
        >>> get_bindings("if_test_atom", {
        ...     "POS": ["31:5-2-1-0-0-0-", "31:5-2-1-0-0-2-1-1-", "31:5-2-1-0-2-1-"],
        ...     "SUFFIX": ["b", "a", "greatest"],
        ... })
        ("if_test_atom:b", Span(start=31, end=31, path="5-2-1-0-0-0-"))
        ("if_test_atom:a", Span(start=31, end=31, path="5-2-1-0-0-2-1-1-"))
        ("if_test_atom:greatest", Span(start=31, end=31, path="5-2-1-0-2-1-"))

        In all other cases, `"POS"` is interpreted as delimiting only one occurrence (which can span
        multiple lines), and associated repeatedly with the different suffixes:

        >>> get_bindings("import_module", {"POS": ["1:1-"], "SUFFIX": ["m1", "m2", "m3"]})
        ("import_module:m1", Span(start=1, end=1, path="1-"))
        ("import_module:m2", Span(start=1, end=1, path="1-"))
        ("import_module:m3", Span(start=1, end=1, path="1-"))
        >>> get_bindings("function_decorator", {
        ...     "POS": ["1:1-", "1:1-2-1-", "2:1-2-2-", "3:1-2-3-", "5:1-5-1-"],
        ...     "SUFFIX": ["bizz", "foo", "bar"],
        ... })
        ("function_decorator:bizz", Span(start=1, end=5, path="1-")),
        ("function_decorator:foo", Span(start=1, end=5, path="1-")),
        ("function_decorator:bar", Span(start=1, end=5, path="1-")),

    Warning:
        Consider the problem of detecting the feature `for` in the following program:

        ```python
        for (i, j) in seq:
            pass
        ```

        With such a multi-line feature, it is normally enough to capture **two** positions, namely
        those of its start (1) and its end (2). However, in this case we want to suffix `for` with
        the names of the **two** iterations variables (`for:i` and `for:j`). If we devise the
        regular expression specification without special care:

        ```re
                ^(.*)/_type=For
        \n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
        (
        \n(?:\1.+\n)*?\1/target(/.+)?/id=(?P<SUFFIX>.+)
        )+
        \n(?:\1.+\n)* \1/.*/_pos=(?P<POS>.+)
        ```

        ... as many positions as there are suffixes will be passed to the present function:

        >>> get_bindings("for", {'POS': ['1:1-', '2:1-2-1-'], 'SUFFIX': ['i', 'j']})
        ("for:i", Span(start=1, end=1, path="1-"))
        ("for:j", Span(start=2, end=2, path="1-2-1-"))

        ... which will result in two (wrong) bindings instead of one. The workaround implemented in
        [spec.md](https://repo/paroxython/resources/spec.md#feature-for) consists in capturing as
        many supplementary positions as iteration variables:

        ```re
                ^(.*)/_type=For
        \n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
        (
        \n(?:\1.+\n)*?\1/(?P<_1>target(/.+)?)/_pos=(?P<POS>.+)
        \n(?:\1.+\n)*?\1/(?P=_1)             /id=(?P<SUFFIX>.+)
        )+
        \n(?:\1.+\n)* \1/.*/_pos=(?P<POS>.+)
        ```

        So, there are now two more positions in the captured dictionary. Since they are not at the
        ends of the list, they are ignored by `pos_to_span`, and the result is now correct:

        >>> get_bindings("for", {
        ...     'POS': ['1:1-', '1:1-0-0-1-', '1:1-0-0-2-', '2:1-2-1-'],
        ...      '_1': ['target/elts/1', 'target/elts/2'],  # ignored at this level
        ...      'SUFFIX': ['i', 'j']
        ... })
        ("for:i", Span(start=1, end=2, path="1-"))
        ("for:j", Span(start=1, end=2, path="1-"))
    """
    if captures.get("SUFFIX"):
        # There is a "SUFFIX" key and its value is not `[]`.
        if len(captures["POS"]) == len(captures["SUFFIX"]):
            # When there are as many matched positions as suffixes, associate them in parallel.
            for (suffix, pos) in zip(captures["SUFFIX"], captures["POS"]):
                yield (LabelName(f"{label_prefix}:{suffix}"), pos_to_span([pos]))
        else:
            # When there are more or less matched positions than suffixes, interpret the positions
            # as defining a unique span, and associate it with each suffix.
            span = pos_to_span(captures["POS"])
            for suffix in captures["SUFFIX"]:
                yield (LabelName(f"{label_prefix}:{suffix}"), span)
    else:
        # There is no "SUFFIX" key or its value is `[]`.
        yield (label_prefix, pos_to_span(captures["POS"]))


class ProgramParser:
    def __init__(self, spec_path: Path = DEFAULT_SPEC_PATH) -> None:
        """Collect the features specified at `spec_path`.

        Args:
            spec_path (Path, optional): The path of the specification file. Defaults to
                [spec.md](https://repo/paroxython/resources/spec.md).

        Raises:
            ValueError: Fail when a given feature appears multiple times in the specification file,
                and when the language is not `"re"` or `"sql"`, and the specification is non-empty.

        Description:
            Some features are searched for with a regular expression, some with an SQL query.
            Distribute them in their respective dictionary. Compile the regular expressions and
            pre-bind the appropriate method. Create an instance of the database of derived labels.
        """
        self.spec_path = spec_path
        text = self.spec_path.read_text()
        self.features: Dict[LabelName, regex.Pattern] = {}
        self.queries: Dict[LabelName, Query] = {}
        for (label_pattern, language, specification) in find_all_features(text):
            if label_pattern in self.features:  # pragma: no cover
                raise ValueError(f"Duplicated name '{label_pattern}'!")
            if language == "re":
                self.features[label_pattern] = regex.compile(f"(?mx){specification}").finditer
            elif language == "sql":
                self.queries[label_pattern] = Query(specification)
            elif specification.strip() != "":  # pragma: no cover
                raise ValueError(f"Unknow language '{language}' for '{label_pattern}'!")
        self.derived_labels_database = DerivedLabelsDatabase()

    def __call__(self, program: Program, yield_failed_matches: bool = False) -> Labels:
        """Parse a given program and return its labels with their spans.

        Args:
            program (Program): A `Program` object, with its fields `source`, `addition` and
                `deletion` populated.
            yield_failed_matches (bool, optional): If `True`, add to the returned labels those
                which have not been found in the program. Each one is associated with an empty
                list of spans. For testing purposes only. Defaults to `False`.

        Returns:
            Labels: A sorted list of labels, associating each label name with its spans.

        Description:
            1. Parse the given program. If this fails, return a list consisting in a single label,
              `"ast_construction:"`, followed by the error name. Otherwise, flatten the resulting
              AST.
            2. Search the flat AST for every feature which is specified by a regular expression.
              Take care to avoid adding those features which are scheduled for deletion at the same
              span.
            3. Update the matching features with those featured for addition.
            4. Use the features found so far to derive (directly and indirectly) all those specified
              by an SQL query.
            5. Return the found features.

        Note:
            The computation of the derived features is done in a single pass, which require them to
            be in a correct dependency order. This order is checked by `helpers/reformat_spec.py`,
            which is executed each time the tests are launched.
        """

        # If the program can be parsed, flatten its AST.
        try:
            tree = ast.parse(program.source)
        except (SyntaxError, ValueError) as exception:
            return [Label(LabelName(f"ast_construction:{type(exception).__name__}"), [])]
        self.flat_ast = flatten_ast(tree)

        # Search the flat AST for every feature which is specified by a regular expression.
        labels: LabelsSpans = defaultdict(list)
        for (label_prefix, finditer) in self.features.items():
            failed_match = True
            for match in finditer(self.flat_ast, overlapped=True):
                failed_match = False
                for (label_name, span) in get_bindings(label_prefix, match.capturesdict()):
                    try:  # Unless this binding is scheduled for deletion...
                        program.deletion[label_name].remove(Span(span.start, span.end))
                    except (KeyError, ValueError):  # ... actually bind the name with the span.
                        labels[label_name].append(span)
            if yield_failed_matches and failed_match:
                labels[label_prefix] = []

        # Update the matching features with those featured for addition.
        for (label_name, spans) in program.addition.items():
            labels[label_name].extend(spans)
            labels[label_name].sort()

        # Now, use the features found so far to derive all those specified by an SQL query.
        result = [Label(*item) for item in labels.items()]
        self.derived_labels_database.create(result)  # The search is seeded with the know features.
        for (label_pattern, query) in self.queries.items():
            # Try to derive, from the DB current state, some label names matching `label_pattern`.
            derived_labels = self.derived_labels_database.read(query)
            if derived_labels:
                # Bingo! update the DB state and the result with the new labels.
                self.derived_labels_database.update(derived_labels)
                result.extend(derived_labels)
            elif yield_failed_matches:
                result.append(Label(label_pattern, []))
        # Empty the DB to make it ready for the next program.
        self.derived_labels_database.delete()

        return sorted(result)


if __name__ == "__main__":
    # Take an individual source, print its features and write its flat AST.
    from .goodies import couple_to_string

    path = Path("sandbox/source.py")
    source = path.read_text().strip()
    if source.startswith("1   "):
        source = regex.sub(r"(?m)^.{1,4}", "", source)
    for (i, line) in enumerate(source.split("\n"), 1):
        print(f"{i:<4}{line}")
    program = Program(source=Source(source), labels=[], taxa=[], addition={}, deletion={})
    print()
    parse = ProgramParser()
    acc = []
    for (name, spans) in sorted(parse(program, yield_failed_matches=False)):
        spans_as_string = ", ".join(map(couple_to_string, spans))
        acc.append(f"| `{name}` | {spans_as_string} |")
        # acc[-1] += " %s |" % ", ".join(f"{span.path}" for span in spans)
    print("\n".join(acc))
    Path("sandbox/flat_ast.txt").write_text(parse.flat_ast)
