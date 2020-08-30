import os
from pathlib import Path

import regex

paths = Path("paroxython").glob("*.py")
paths = list(
    path
    for path in paths
    if not str(path).endswith(
        (
            "user_types.py",
            "goodies.py",
            "span.py",
            "analyze_one.py",
            "cli_collect.py",
            "cli_recommend.py",
            "cli.py",
            "cli_tag.py",
        )
    )
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
            '"*_db.json" [shape=cylinder fillcolor="#c5f541" color="#435214" penwidth=1 height=1]',
            '"*_db.sqlite" [shape=cylinder fillcolor="#c5f541" color="#435214" penwidth=1 height=1]',
            '"spec.md" [shape=note fillcolor="#f57141" color="#662f17" penwidth=1]',
            '"*_pipe.py" [shape=note fillcolor="#f57141" color="#662f17" penwidth=1]',
            '"taxonomy.tsv" [shape=note fillcolor="#f57141" color="#662f17" penwidth=1]',
            '"source files" [shape=folder fillcolor="#f57141" color="#662f17" penwidth=1]',
            '"*_recommendations.md" [shape=note fillcolor="#c5f541" color="#435214" penwidth=1]',
            'make_db -> "*_db.json"',
            'make_db -> "*_db.sqlite"',
            '"*_db.json" -> filter_programs',
            '"spec.md" -> parse_program',
            '"source files" -> list_programs',
            '"taxonomy.tsv" -> map_taxonomy',
            '"*_pipe.py" -> recommend_programs',
            'recommend_programs -> "*_recommendations.md"',
            # Add invisible edges to reshape the layout
            '"*_db.sqlite" -> "*_pipe.py"  [style=invis]',
            '"list_programs" -> "flatten_ast"  [style=invis]',
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
