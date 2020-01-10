import ast
from collections import defaultdict
from pathlib import Path
from typing import Callable, Dict, Iterator, Tuple, List
import sqlite3

import regex  # type: ignore

from user_types import Label, Labels, LabelName, LabelsSpans, Source, Program, Query
from flatten_ast import flatten_ast
from span import Span


def _simplify_negative_literals() -> Callable:
    sub = regex.compile(
        r"""(?mx)
                    ^(.*?)/_type='UnaryOp'
            (\n(?:.+\n)*?)\1/op/_type='USub'
             \n(?:.+\n)*? \1/operand/n=(.+)
        """
    ).sub
    return lambda flat_ast: sub(r"\1/_type='Num'\2\1/n=-\3", flat_ast)


simplify_negative_literals = _simplify_negative_literals()


find_all_constructs = regex.compile(
    r"""(?msx)
            ^\#{4}\s+Construct\s+`(.+?)` # capture the label's name
            .+?\#{5}\s+Definition # ensure the next pattern is in the Definition section
            .+?```(.*?)\n+(.*?)\n``` # capture the language and the pattern
        """
).findall


class Table:
    """A simple RDB consisting in one single table of labels."""

    def __init__(self):
        self.c = sqlite3.connect(":memory:")

    def create(self, labels: Labels) -> None:
        columns = [
            # use rowid as primary key:
            # https://www.sqlite.org/lang_createtable.html#rowid
            "name TEXT",
            "name_prefix TEXT",
            "name_suffix TEXT",
            "span TEXT",
            "span_start INTEGER",
            "span_end INTEGER",
        ]
        self.c.execute(f"CREATE TABLE t ({','.join(columns)})")
        self.insert_command = f"INSERT INTO t VALUES ({','.join('?' * len(columns))})"
        self.update(labels)

    def read(self, query: Query) -> Labels:
        groups: LabelsSpans = defaultdict(list)
        for (label_name, start, end) in self.c.execute(query):
            groups[label_name].append(Span([start, end]))
        return [Label(*item) for item in groups.items()]

    def update(self, labels: Labels) -> None:
        values = []
        for (name, spans) in labels:
            for span in spans:
                (name_prefix, _, name_suffix) = name.partition(":", 1)
                values.append(
                    (  # fmt:off
                        name,
                        name_prefix,
                        f":{name_suffix}",
                        str(span),
                        span.start,
                        span.end,
                    )  # fmt: on
                )
        self.c.executemany(self.insert_command, values)

    def delete(self) -> None:
        self.c.execute("DROP TABLE t")


class ProgramParser:
    """Compile the given construct definitions, and search them in a Program."""

    def __init__(self, ref_path: str = "paroxython/ref.md") -> None:
        """Compile the constructs to search."""
        self.ref_path = Path(ref_path)
        text = self.ref_path.read_text()
        self.constructs: Dict[LabelName, regex.Pattern] = {}
        self.queries: Dict[LabelName, Query] = {}
        for (label_name, language, pattern) in find_all_constructs(text):
            if label_name in self.constructs:
                raise ValueError(f"Duplicated name '{label_name}'!")  # pragma: no cover
            if language == "re":
                self.constructs[label_name] = regex.compile(f"(?mx){pattern}")
            elif language == "sql":
                self.queries[label_name] = pattern
        self.table = Table()

    def __call__(self, program: Program, yield_failed_matches: bool = False) -> Labels:
        """Analyze a given source and return its labels and their spans."""

        def try_to_bind(label_name: LabelName, span: Span) -> None:
            """Bind a name with a span, unless this binding is scheduled for deletion."""
            try:
                program.deletion[label_name].remove(span)
            except (KeyError, ValueError):
                result[label_name].append(span)

        try:
            tree = ast.parse(program.source)
        except (SyntaxError, ValueError) as exception:
            return [Label(f"ast_construction:{type(exception).__name__}", [])]
        self.flat_ast = simplify_negative_literals(flatten_ast(tree))

        labels: Labels = []
        for (label_name, rex) in self.constructs.items():
            result: LabelsSpans = defaultdict(list)
            for candidate in list(program.addition):
                if candidate == label_name or candidate.startswith(f"{label_name}:"):
                    result[candidate] = program.addition.pop(candidate)
            d = None
            for match in rex.finditer(self.flat_ast, overlapped=True):
                d = match.capturesdict()
                span = Span(d["LINE"])
                if d.get("SUFFIX"):  # there is a "SUFFIX" key and its value is not []
                    for suffix in d["SUFFIX"]:
                        try_to_bind(LabelName(f"{label_name}:{suffix}"), span)
                else:
                    try_to_bind(label_name, span)
            if yield_failed_matches and not d:
                labels.append(Label(label_name, []))
            else:
                labels.extend(Label(*item) for item in result.items())

        labels.extend(Label(*item) for item in program.addition.items())

        self.table.create(labels)
        for query in self.queries.values():
            derived_labels = self.table.read(query)
            self.table.update(derived_labels)
            labels.extend(derived_labels)
        self.table.delete()

        return sorted(labels)


if __name__ == "__main__":
    """Take an individual source, print its constructs and write its flat AST."""
    path = Path("sandbox/source.py")
    source = path.read_text().strip()
    if source.startswith("1   "):
        source = regex.sub(r"(?m)^.{1,4}", "", source)
    for (i, line) in enumerate(source.split("\n"), 1):
        print(f"{i:<4}{line}")
    program = Program(source=Source(source))
    print()
    parse = ProgramParser()
    acc = []
    for (name, spans) in parse(program, yield_failed_matches=False):
        spans_as_string = ", ".join(map(str, spans))
        acc.append(f"| `{name}` | {spans_as_string} |")
    print("\n".join(acc))
    Path("sandbox/flat_ast.txt").write_text(parse.flat_ast)
