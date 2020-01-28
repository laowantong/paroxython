import ast
from typing import Any

import regex  # type: ignore

extract_ids = regex.compile(r"Name\(id='(.+?)'\)").findall
remove_context = regex.compile(r", ctx=.+?\(\)").sub
deduplicate_whilst_preserving_order = dict.fromkeys


def flatten_ast(node: Any, prefix="", path="") -> str:
    if isinstance(node, ast.AST):
        acc = [f"{prefix}/_type='{type(node).__name__}'\n"]
        if isinstance(node, ast.expr):
            node_repr = remove_context("", ast.dump(node))
            ids = ":".join(deduplicate_whilst_preserving_order(extract_ids(node_repr)))
            acc.append(f"{prefix}/_ids={ids}\n")
            expr_hash = hex(hash(node_repr) & 0xFFFFFFFF)
            acc.append(f"{prefix}/_hash={expr_hash}\n")
        if "lineno" in node._attributes:
            acc.append(f"{prefix}/_pos={node.lineno}:{path[2:-1]}\n")
        fields = ast.iter_fields(node)
        if isinstance(node, ast.FunctionDef):
            # reject `body` behind `decorator_list` and `returns`, whose line number is those of `def` clause
            fields = iter(sorted(fields, key=lambda c: c[0] == "body"))
        for (i, (name, x)) in enumerate(fields):
            if name == "orelse" and isinstance(node, (ast.For, ast.While, ast.AsyncFor)):
                name = "loopelse"  # this makes the "orelse" clause specific to conditionals
            elif name == "targets" and isinstance(node, ast.Assign):
                name = "assigntargets"
            elif name == "target" and isinstance(node, ast.AugAssign):
                name = "assigntarget"
            elif name == "value" and isinstance(node, (ast.Assign, ast.AugAssign)):
                name = "assignvalue"
            acc.append(flatten_ast(x, f"{prefix}/{name}", f"{path}{i}-"))
        return "".join(acc)
    elif isinstance(node, list):
        acc = [f"{prefix}/length={len(node)}\n"]
        for (i, x) in enumerate(node, 1):
            acc.append(flatten_ast(x, f"{prefix}/{i}", f"{path}{i}-"))
        return "".join(acc)
    else:
        return f"{prefix}={node!r}\n"


if __name__ == "__main__":
    Path = __import__("pathlib").Path
    source = Path("sandbox/source.py").read_text()
    print(flatten_ast(ast.parse(source)))
