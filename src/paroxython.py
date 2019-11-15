import ast
from collections import defaultdict
from pathlib import Path

import regex

CONSTRUCT_PATH = Path("constructs.md")
EXTRACT_IDS = regex.compile(r"Name\(id='(.+?)'\)").findall
REMOVE_CONTEXT = regex.compile(r", ctx=.+?\(\)").sub


def flatten(node, prefix=""):
    if isinstance(node, ast.AST):
        acc = [f"{prefix}/_type='{type(node).__name__}'\n"]
        if isinstance(node, ast.expr):
            node_repr = REMOVE_CONTEXT("", ast.dump(node))
            ids = "''".join(sorted(set(EXTRACT_IDS(node_repr))))
            acc.append(f"{prefix}/_ids='{ids}'\n")
            expr_hash = hex(hash(node_repr) & 0xFFFFFFFF)
            acc.append(f"{prefix}/_hash={expr_hash}\n")
        if "lineno" in node._attributes:
            acc.append(f"{prefix}/lineno={node.lineno}\n")
        for (name, x) in ast.iter_fields(node):
            acc.append(flatten(x, f"{prefix}/{name}"))
        return "".join(acc)
    elif isinstance(node, list):
        acc = [f"{prefix}/length={len(node)}\n"]
        for (i, x) in enumerate(node):
            acc.append(flatten(x, f"{prefix}/{i}"))
        return "".join(acc)
    else:
        return f"{prefix}={node!r}\n"


class Parser:
    def __init__(self, construct_path):
        text = construct_path.read_text()
        rex = r"""(?msx)
            ^\#{5}\s+Construct\s+`(.+?)` # capture the label
            .+?
            \#{6}\s+Regex # ensure the next pattern is in the Regex section
            .+?
            ```re\n+(.+?)\n``` # capture this pattern
        """
        self.constructs = {}
        for (label, pattern) in regex.findall(rex, text):
            if label in self.constructs:
                raise ValueError(f"Duplicated label '{label}'!")
            self.constructs[label] = regex.compile(f"(?mx){pattern}")

    def __call__(self, source):
        self.code = flatten(ast.parse(source))
        result = defaultdict(list)
        for (label, rex) in self.constructs.items():
            for match in rex.finditer(self.code, overlapped=True):
                d = match.capturesdict()
                for suffix in d.get("SUFFIX", [""]):
                    if suffix:
                        suffix = f"-{suffix}"
                    lines = "-".join(map(str, sorted(map(int, d["LINE"]))))
                    result[label + suffix].append(lines)
        for label in result:
            result[label] = ", ".join(result[label])
        return result


if __name__ == "__main__":
    parse = Parser(CONSTRUCT_PATH)
    source = Path("draft.py").read_text()
    for (i, line) in enumerate(source.splitlines(), 1):
        print(f"{i:2}  {line}")
    result = parse(source)
    Path("logs/draft.txt").write_text(parse.code)
    for (label, lines) in sorted(result.items()):
        print(f"{label}: {lines}")
