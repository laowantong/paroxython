import os
from pathlib import Path

import regex

paths = Path("paroxython").glob("*.py")
paths = list(
    path
    for path in paths
    if not str(path).endswith(("user_types.py", "goodies.py", "span.py", "analyze_one.py"))
)
names = [str(path)[len("paroxython/") : -3] for path in paths]
base = "docs/resources/flow"
find_all = regex.compile(fr"(?m)^from \.({'|'.join(names)}) import").findall

Path(f"{base}.dot").write_text(
    """digraph G {
        node [shape=box fontname=Menlo fontsize=16 style="rounded,filled" textcolor="#646464" fillcolor="#F5CA41" color="#B38D01" penwidth=2]
        edge [penwidth=2 color="#646464"]
        %s
    }
    """
    % "\n".join(
        [
            '"*_db.json" [shape=cylinder fillcolor="#CCCCCC" color="#646464" penwidth=1]',
            '"*_db.sqlite" [shape=cylinder fillcolor="#CCCCCC" color="#646464" penwidth=1]',
            '"spec.md" [shape=note fillcolor="#CCCCCC" color="#646464" penwidth=1]',
            '"*_pipe.py" [shape=note fillcolor="#CCCCCC" color="#646464" penwidth=1]',
            '"taxonomy.tsv" [shape=note fillcolor="#CCCCCC" color="#646464" penwidth=1]',
            '"source files" [shape=folder fillcolor="#CCCCCC" color="#646464" penwidth=1]',
            # '"sqlite_queries" [shape=folder fillcolor="#CCCCCC" color="#646464" penwidth=1]',
            'make_db -> "*_db.json"',
            'make_db -> "*_db.sqlite"',
            # '"*_db.sqlite" -> sqlite_queries',
            '"*_db.json" -> filter_programs',
            '"spec.md" -> parse_program',
            '"source files" -> list_programs',
            '"taxonomy.tsv" -> map_taxonomy',
            '"*_pipe.py" -> recommend_programs',
            # Add invisible edges to make the layout more compact
            # "sqlite_queries -> recommend_programs  [style=invis]",
            '"*_db.sqlite" -> "*_pipe.py"  [style=invis]',
            # "compare_spans -> assess_costs  [style=invis]",
        ]
        + [
            f"{imported_name} -> {name}"
            for (name, path) in zip(names, paths)
            for imported_name in find_all(path.read_text())
        ]
    )
)
os.system(f"dot -Tpng {base}.dot > {base}.png; rm {base}.dot")

base = "docs/resources/filter_flow"
text = Path("paroxython/filter_programs.py").read_text()
text = regex.search(r"(?s)<graphviz>(.+)</graphviz>", text)[1]
text = text.replace("# ", "        ")

Path(f"{base}.dot").write_text(
    f"""digraph G {{
        node [shape=box fontname=Menlo fontsize=16 style="rounded,filled" textcolor="#646464" fillcolor="#F5CA41" color="#B38D01" penwidth=2]
        edge [penwidth=2 color="#646464"]
        rankdir=LR;
        {text}
    }}
    """
)
os.system(f"dot -Tpng {base}.dot > {base}.png; rm {base}.dot")
