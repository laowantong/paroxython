import os
from pathlib import Path

import regex

paths = Path("paroxython").glob("*.py")
paths = list(path for path in paths if not str(path).endswith("user_types.py"))
names = [str(path)[len("paroxython/") : -3] for path in paths]
base = "docs/flow"
find_all = regex.compile(fr"(?m)^from ({'|'.join(names)}) import").findall

Path(f"{base}.dot").write_text(
    "digraph G {\nnode [shape=box fontname=Courier style=filled fillcolor=cornsilk]\n%s\n}\n"
    % "\n".join(
        [
            '"db.json" [shape=cylinder fillcolor=moccasin]',
            '"db.sqlite" [shape=cylinder fillcolor=moccasin]',
            '"spec.md" [shape=note fillcolor=moccasin]',
            '"default_taxonomy.tsv" [shape=note fillcolor=moccasin]',
            '"source files" [shape=folder fillcolor=moccasin]',
            '"sqlite_queries" [shape=folder fillcolor=moccasin]',
            '"syllabus.txt" [shape=note fillcolor=moccasin]',
            'make_db -> "db.json"',
            'make_db -> "db.sqlite"',
            '"db.sqlite" -> sqlite_queries',
            '"db.json" -> filter_programs',
            '"spec.md" -> parse_program',
            '"source files" -> generate_programs',
            '"default_taxonomy.tsv" -> map_taxonomy',
            '"syllabus.txt" -> recommend_programs',
        ]
        + [
            f"{imported_name} -> {name}"
            for (name, path) in zip(names, paths)
            for imported_name in find_all(path.read_text())
        ]
    )
)
os.system(f"dot -Tpng {base}.dot > {base}.png; rm {base}.dot")
