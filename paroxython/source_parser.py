import ast
import sys
from collections import defaultdict
from pathlib import Path
from typing import Callable, Dict, Iterator, List, NamedTuple, Tuple

import regex  # type: ignore

from flatten import flatten
from span import Span


class Label(NamedTuple):
    name: str
    span: List[Span]


def _simplify_negative_litterals() -> Callable:
    sub = regex.compile(
        r"""(?mx)
                    ^(.*?)/_type='UnaryOp'
            (\n(?:.+\n)*?)\1/op/_type='USub'
             \n(?:.+\n)*? \1/operand/n=(.+)
        """
    ).sub
    return lambda flat_ast: sub(r"\1/_type='Num'\2\1/n=-\3", flat_ast)


simplify_negative_litterals = _simplify_negative_litterals()


find_all_constructs = regex.compile(
    r"""(?msx)
            ^\#{4}\s+Construct\s+`(.+?)` # capture the label's name
            .+?\#{5}\s+Regex # ensure the next pattern is in the Regex section
            .+?```re\n+(.+?)\n``` # capture this pattern
        """
).findall


class SourceParser:
    """Compile the given construct definitions, and search them in a source-code."""

    def __init__(self, ref_path: str = "paroxython/ref.md") -> None:
        """Compile the constructs to search."""
        self.ref_path = Path(ref_path)
        text = self.ref_path.read_text()
        self.constructs: Dict[str, regex.Pattern] = {}
        for (label_name, pattern) in find_all_constructs(text):
            if label_name in self.constructs:
                raise ValueError(f"Duplicated name '{label_name}'!")
            self.constructs[label_name] = regex.compile(f"(?mx){pattern}")

    def __call__(
        self,
        source: str,
        manual_hints: Tuple[Dict[str, List[Span]], Dict[str, List[Span]]] = None,
        yield_failed_matches: bool = False,
    ) -> Iterator[Label]:
        """Analyze a given program source and yield its labels and their spans."""

        (addition, deletion) = manual_hints or ({}, {})

        def try_to_bind_name_and_span(label_name: str, span: Span) -> None:
            """Bind a name with a span, unless this binding is scheduled for deletion."""
            try:
                deletion[label_name].remove(span)
            except (KeyError, ValueError):
                result[label_name].append(span)

        try:
            tree = ast.parse(source)
        except (SyntaxError, ValueError):
            return print("Warning: unable to construct the AST")
        self.flat_ast = simplify_negative_litterals(flatten(tree))

        for (label_name, rex) in self.constructs.items():
            result: Dict[str, List[Span]] = defaultdict(list)
            for candidate in list(addition):
                if candidate == label_name or candidate.startswith(f"{label_name}:"):
                    result[candidate] = addition.pop(candidate)
            d = None
            for match in rex.finditer(self.flat_ast, overlapped=True):
                d = match.capturesdict()
                span = Span(d["LINE"])
                if d.get("SUFFIX"):  # there is a "SUFFIX" key and its value is not []
                    for suffix in d["SUFFIX"]:
                        try_to_bind_name_and_span(f"{label_name}:{suffix}", span)
                else:
                    try_to_bind_name_and_span(label_name, span)
            if yield_failed_matches and not d:
                yield Label(label_name, [])
            else:
                yield from (Label(name, spans) for (name, spans) in result.items())
        yield from (Label(name, spans) for (name, spans) in addition.items())


if __name__ == "__main__":
    """Take an individual source-code, print its constructs and write its flat AST."""
    time = __import__("time")
    source = Path("sandbox/source.py").read_text().strip()
    if source.startswith("1   "):
        source = regex.sub(r"(?m)^.{1,4}", "", source)
    for (i, line) in enumerate(source.split("\n"), 1):
        print(f"{i:<4}{line}")
    print()
    parse = SourceParser()
    start = time.perf_counter()
    acc = []
    for (name, spans) in sorted(parse(source, yield_failed_matches=False)):
        stop = time.perf_counter()
        spans_as_string = ", ".join(map(str, spans))
        acc.append(f"{stop - start:7.4f} s.: | `{name}` | {spans_as_string} |")
        start = stop
    print("\n".join(acc))
    Path("sandbox/flat_ast.txt").write_text(parse.flat_ast)
