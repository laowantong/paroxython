import ast
from collections import defaultdict
from pathlib import Path
import regex
import sys

sys.path[0:0] = [str(Path(__file__).parent)]

from flatten import flatten
from span import Span


def simplify_negative_litterals():
    sub = regex.compile(
        r"""(?mx)
                    ^(.*?)/_type='UnaryOp'
            (\n(?:.+\n)*?)\1/op/_type='USub'
             \n(?:.+\n)*? \1/operand/n=(.+)
        """
    ).sub
    return lambda flat_ast: sub(r"\1/_type='Num'\2\1/n=-\3", flat_ast)


simplify_negative_litterals = simplify_negative_litterals()


find_all_constructs = regex.compile(
    r"""(?msx)
            ^\#{4}\s+Construct\s+`(.+?)` # capture the label's name
            .+?\#{5}\s+Regex # ensure the next pattern is in the Regex section
            .+?```re\n+(.+?)\n``` # capture this pattern
        """
).findall


class Parser:
    """Compile the given construct definitions, and search them in a source-code."""

    def __init__(self, ref_path="paroxython/ref.md"):
        """Compile the constructs to search."""
        self.ref_path = Path(ref_path)
        text = self.ref_path.read_text()
        self.constructs = {}
        for (label_name, pattern) in find_all_constructs(text):
            if label_name in self.constructs:
                raise ValueError(f"Duplicated name '{label_name}'!")
            self.constructs[label_name] = regex.compile(f"(?mx){pattern}")

    def __call__(self, source, yield_failed_matches=False):
        """Analyze a given program source and yield its labels and their spans."""
        try:
            tree = ast.parse(source)
        except (SyntaxError, ValueError):
            return print("Warning: unable to construct the AST")
        self.flat_ast = simplify_negative_litterals(flatten(tree))
        for (label_name, rex) in self.constructs.items():
            result = defaultdict(list)
            d = None
            for match in rex.finditer(self.flat_ast, overlapped=True):
                d = match.capturesdict()
                span = Span(d["LINE"])
                if d.get("SUFFIX"):  # there is a "SUFFIX" key and its value is not []
                    for suffix in d["SUFFIX"]:
                        result[f"{label_name}:{suffix}"].append(span)
                else:
                    result[label_name].append(span)
            if yield_failed_matches and not d:
                yield (label_name, [])
            else:
                yield from result.items()


if __name__ == "__main__":
    time = __import__("time")
    source = Path("sandbox/source.py").read_text()
    for (i, line) in enumerate(source.splitlines(), 1):
        print(f"{i: 3} {line}")
    print()
    parse = Parser()
    start = time.perf_counter()
    acc = []
    for (name, spans) in parse(source, yield_failed_matches=False):
        stop = time.perf_counter()
        spans = ", ".join(map(str, spans))
        acc.append(f"{stop - start:7.4f} s.: | `{name}` | {spans} |")
        start = stop
    print("\n".join(sorted(acc, reverse=True)))
    Path("sandbox/flat_ast.txt").write_text(parse.flat_ast)
