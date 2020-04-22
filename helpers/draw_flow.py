import os
from pathlib import Path

import regex

paths = Path("paroxython").glob("*.py")
paths = list(
    path for path in paths if not str(path).endswith(("user_types.py", "goodies.py", "span.py"))
)
names = [str(path)[len("paroxython/") : -3] for path in paths]
base = "docs/flow"
find_all = regex.compile(fr"(?m)^from ({'|'.join(names)}) import").findall

Path(f"{base}.dot").write_text(
    "digraph G {\nnode [shape=box fontname=Courier style=filled fillcolor=cornsilk]\n%s\n}\n"
    % "\n".join(
        [
            '"*_db.json" [shape=cylinder fillcolor=moccasin]',
            '"*_db.sqlite" [shape=cylinder fillcolor=moccasin]',
            '"spec.md" [shape=note fillcolor=moccasin]',
            '"*_pipe.py" [shape=note fillcolor=moccasin]',
            '"*_taxonomy.tsv" [shape=note fillcolor=moccasin]',
            '"source files" [shape=folder fillcolor=moccasin]',
            '"sqlite_queries" [shape=folder fillcolor=moccasin]',
            'make_db -> "*_db.json"',
            'make_db -> "*_db.sqlite"',
            '"*_db.sqlite" -> sqlite_queries',
            '"*_db.json" -> filter_programs',
            '"spec.md" -> parse_program',
            '"source files" -> list_programs',
            '"*_taxonomy.tsv" -> map_taxonomy',
            '"*_pipe.py" -> recommend_programs',
            # Add invisible edges to make the layout more compact
            "sqlite_queries -> recommend_programs  [style=invis]",
            '"*_db.sqlite" -> "*_pipe.py"  [style=invis]',
            'list_programs -> "*_db.json"  [style=invis]',
            "compare_spans -> assess_costs  [style=invis]",
        ]
        + [
            f"{imported_name} -> {name}"
            for (name, path) in zip(names, paths)
            for imported_name in find_all(path.read_text())
        ]
    )
)
os.system(f"dot -Tpng {base}.dot > {base}.png; rm {base}.dot")
