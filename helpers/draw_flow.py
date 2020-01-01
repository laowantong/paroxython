import os
from pathlib import Path

import regex

paths = Path("paroxython").glob("*.py")
paths = list(path for path in paths if not str(path).endswith("declarations.py"))
names = [str(path)[len("paroxython/") : -3] for path in paths]
base = "docs/flow"
find_all = regex.compile(fr"(?m)^from ({'|'.join(names)}) import").findall

Path(f"{base}.dot").write_text(
    "digraph G {\nnode [shape=box fontname=Courier style=filled fillcolor=cornsilk]\n%s\n}\n"
    % "\n".join(
        [
            '"db.json" [shape=cylinder fillcolor=moccasin]',
            '"ref.md" [shape=note fillcolor=moccasin]',
            'make_db -> "db.json"',
            '"db.json" -> program_filter',
            '"ref.md" -> source_parser',
        ]
        + [
            f"{imported_name} -> {name}"
            for (name, path) in zip(names, paths)
            for imported_name in find_all(path.read_text())
        ]
    )
)
os.system(f"dot -Tpng {base}.dot > {base}.png")
