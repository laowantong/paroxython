import ast
from typing import Any

import regex  # type: ignore

extract_ids = regex.compile(r"Name\(id='(.+?)'\)").findall
remove_context = regex.compile(r", ctx=.+?\(\)").sub
deduplicate = dict.fromkeys  # deduplicate whilst preserving order


def flatten_ast(node: Any, prefix: str = "") -> str:
    if isinstance(node, ast.AST):
        acc = [f"{prefix}/_type='{type(node).__name__}'\n"]
        if isinstance(node, ast.expr):
            node_repr = remove_context("", ast.dump(node))
            ids = ":".join(deduplicate(extract_ids(node_repr)))
            acc.append(f"{prefix}/_ids={ids}\n")
            expr_hash = hex(hash(node_repr) & 0xFFFFFFFF)
            acc.append(f"{prefix}/_hash={expr_hash}\n")
        if "lineno" in node._attributes:
            acc.append(f"{prefix}/lineno={node.lineno}\n")
        for (name, x) in ast.iter_fields(node):
            if name == "orelse" and isinstance(node, (ast.For, ast.While, ast.AsyncFor)):
                name = "loopelse"  # this makes the "orelse" clause specific to conditionals
            acc.append(flatten_ast(x, f"{prefix}/{name}"))
        return "".join(acc)
    elif isinstance(node, list):
        acc = [f"{prefix}/length={len(node)}\n"]
        for (i, x) in enumerate(node):
            acc.append(flatten_ast(x, f"{prefix}/{i}"))
        return "".join(acc)
    else:
        return f"{prefix}={node!r}\n"


if __name__ == "__main__":
    Path = __import__("pathlib").Path
    source = Path("sandbox/source.py").read_text()
    print(flatten_ast(ast.parse(source)))
