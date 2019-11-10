import ast
import ast2json
import regex
from collections import defaultdict
import json


def flatten(tree):
    metadata_rex = regex.compile(
        r"""(?mx), (             # These keys always follow another one.
        "col_offset":\d+ |       # The column is not relevant for the structure.
        "lineno":\d+ |           # The line number already appears above in the tree.
        "ctx":{"_type":".+?"}    # The context information is external to the node.
    )"""
    )

    def suppress_metadata(node):
        """ Delete any information depending on the position of the node in the source. """
        return metadata_rex.sub("", json.dumps(node, separators=(",", ":")))

    def node_hash(node):
        """ Calculate a unique identifier for a given node. """
        return hex(hash(suppress_metadata(node)))

    def item_order(item):
        """ build a key to sort the nodes from the simplest to the most complex. """
        return (
            item[0] == "body",  # Relegate nested lines to the end,
            isinstance(item[1], (dict, list)),  # after other collections,
            item[0],  # and start with elementary types
        )

    def walk(node, prefix=""):
        if isinstance(node, (dict, list)):
            acc = [f"{prefix}/hash={node_hash(node)}\n"]
            if isinstance(node, dict):
                acc.extend(
                    walk(v, f"{prefix}/{k}")
                    for (k, v) in sorted(node.items(), key=item_order)
                )
            else:
                acc.append(f"{prefix}/length={len(node)}\n")
                acc.extend(walk(x, f"{prefix}/{i}") for (i, x) in enumerate(node))
            return "".join(acc)
        else:
            return f"{prefix}={node!r}\n"

    return walk(tree)


class Parser:
    def __init__(self, trait_path):
        with open(trait_path) as f:
            text = f.read()
        rex = r"""(?msx)
            ^\#{5}\s+`(.+?)` # capture the label
            .+?
            \#{6}\s+Regex # ensure the next pattern is in the Regex section
            .+?
            ```re\n+(.+?)\n``` # capture this pattern
        """
        self.traits = {}
        for (label, pattern) in regex.findall(rex, text):
            if label in self.traits:
                raise ValueError(f"Duplicated label '{label}'!")
            self.traits[label] = regex.compile(f"(?mx){pattern}")

    def __call__(self, source):
        tree = ast2json.ast2json(ast.parse(source))
        code = flatten(tree)
        open("logs/draft.txt", "w").write(code)
        result = defaultdict(list)
        for (label, rex) in self.traits.items():
            for match in rex.finditer(code, overlapped=True):
                d = match.capturesdict()
                for suffix in d.get("SUFFIX", [""]):
                    if suffix:
                        suffix = f"-{suffix}"
                    lines = "-".join(sorted(d["LINE"]))
                    result[label + suffix].append(lines)
        for label in result:
            result[label] = ", ".join(result[label])
        return result


if __name__ == "__main__":
    parse = Parser("traits.md")
    with open("draft.py") as f:
        source = f.read()
    for (i, line) in enumerate(source.splitlines(), 1):
        print(f"{i:2}  {line}")
    result = parse(source)
    for (label, lines) in sorted(result.items()):
        print(f"{label}: {lines}")
