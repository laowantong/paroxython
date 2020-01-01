import os
from pathlib import Path

import regex

paths = list(Path("paroxython").glob("*.py"))
names = [str(path)[len("paroxython/") : -3] for path in paths]
base = "docs/flow"

Path(f"{base}.dot").write_text(
    "digraph G {\n    node [shape=box fontname=Courier style=filled fillcolor=cornsilk]\n%s\n}\n"
    % "\n".join(
        [
            '    "db.json" [shape=cylinder fillcolor=moccasin]',
            '    "ref.md" [shape=note fillcolor=moccasin]',
            '    make_db -> "db.json"',
            '    "db.json" -> program_filter',
            '    "ref.md" -> source_parser',
        ]
        + [
            f"    {imported_name} -> {name}"
            for (name, path) in zip(names, paths)
            for imported_name in regex.findall(
                fr"(?m)^from ({'|'.join(names)}) import", path.read_text()
            )
        ]
    )
)
os.system(f"dot -Tpng {base}.dot > {base}.png")
