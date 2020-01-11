import ast
from collections import defaultdict
from pathlib import Path
from typing import Callable, Dict

import regex  # type: ignore

from user_types import Label, Labels, LabelName, LabelsSpans, Source, Program, Query
from flatten_ast import flatten_ast
from span import Span
from derived_labels_db import DB


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


class ProgramParser:
    """Compile the given construct definitions, and search them in a Program."""

    def __init__(self, ref_path: str = "docs/ref.md") -> None:
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
        self.db = DB()

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
            return [Label(LabelName(f"ast_construction:{type(exception).__name__}"), [])]
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

        self.db.create(labels)
        for query in self.queries.values():
            derived_labels = self.db.read(query)
            self.db.update(derived_labels)
            labels.extend(derived_labels)
        self.db.delete()

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
