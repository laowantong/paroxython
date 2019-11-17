import ast
from collections import defaultdict
from pathlib import Path
import regex
import sys

sys.path[0:0] = [str(Path(__file__).parent)]

from flatten import flatten


class Parser:

    ref_path = Path("paroxython/ref.md")

    def __init__(self):
        text = Parser.ref_path.read_text()
        rex = r"""(?msx)
            ^\#{5}\s+Construct\s+`(.+?)` # capture the label
            .+?\#{6}\s+Regex # ensure the next pattern is in the Regex section
            .+?```re\n+(.+?)\n``` # capture this pattern
        """
        self.constructs = {}
        for (label, pattern) in regex.findall(rex, text):
            if label in self.constructs:
                raise ValueError(f"Duplicated label '{label}'!")
            self.constructs[label] = regex.compile(f"(?mx){pattern}")

    def __call__(self, source):
        try:
            tree = ast.parse(source)
        except:
            print("Warning: unable to construct the AST")
            return {}
        self.flat_ast = flatten(tree)
        result = defaultdict(list)
        for (label, rex) in self.constructs.items():
            for match in rex.finditer(self.flat_ast, overlapped=True):
                d = match.capturesdict()
                for suffix in d.get("SUFFIX", [""]):
                    if suffix:
                        suffix = f"-{suffix}"
                    lines = "-".join(map(str, sorted(map(int, d["LINE"]))))
                    result[label + suffix].append(lines)
        return result


if __name__ == "__main__":
    source = Path("sandbox/source.py").read_text()
    for (i, line) in enumerate(source.splitlines(), 1):
        print(f"{i: 3} {line}")
    print()
    parse = Parser()
    for (label, lines) in parse(source).items():
        print(f"{label}: {' '.join(lines)}")
    Path("sandbox/flat_ast.txt").write_text(parse.flat_ast)
