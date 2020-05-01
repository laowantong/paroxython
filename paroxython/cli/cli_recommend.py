"""
USAGE:
    paroxython recommend [options] DB_PATH

OPTIONS:
    --pipe=PATH         Path of the command pipeline. If it is omitted, and DB_PATH is of the
                        form PREFIX_db.json, a value of PREFIX_pipe.py is used. If the associated
                        file is missing or malformed, no filter is applied. [default: ]
    --base=PATH         Value accessible by any shell command of the pipeline. If not specified,
                        this is parent directory of DB_PATH. [default: ]
    -o --output=PATH    The path of the resulting report. If it is omitted, and DB_PATH is
                        of the form PREFIX_db.json, a value of PREFIX_recommendations.json is
                        used. [default: ]
    -c --cost=STR       Learning cost assessment strategy. [default: zeno]
                        Currently available:
                        • zeno: the i-th segment of a taxon, if not already imparted, costs 2^(-i).
                                For instance, the taxon old/new/new will costs 2^-2 + 2^-3 = 0.375.
                        • length: simply count the number of new segments.


DESCRIPTION:
    Walk a directory, tag its Python files and make a database of the results.
"""

import json
from pathlib import Path

import regex  # type: ignore
from typed_ast.ast3 import literal_eval

from ..recommend_programs import Recommendations


def cli_wrapper(args):
    db_path = Path(args["DB_PATH"])
    parent_path = db_path.parent
    m = regex.fullmatch(r"(.+)[_-]db\.json", db_path.name)
    prefix = m[1] if m else None
    try:
        pipeline_path = Path(args["--pipe"] or parent_path / f"{prefix}_pipe.py")
        commands = literal_eval(pipeline_path.read_text())
    except Exception:  # Too much possible exceptions
        commands = []
    rec = Recommendations(
        commands=commands,
        db=json.loads(db_path.read_text()),
        base_path=Path(args["--base"] or parent_path),
        output_path=Path(args["--output"] or parent_path / f"{prefix}_recommendations.md"),
        cost_assessment_strategy=args["--cost"],
    )
    rec.run_pipeline()
    text = rec.get_markdown()
    rec.dump(text)
