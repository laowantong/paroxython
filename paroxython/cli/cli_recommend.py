"""
USAGE:
    paroxython recommend [options] DB_PATH

OPTIONS:
    -b --base=PATH      Value accessible by any shell command of the pipeline.
                        If not specified, this is parent directory of DB_PATH.
                        [default: ]
    -c --cost=STR       Learning cost assessment strategy. [default: zeno]
                        Currently available:
                        • zeno: the i-th edge of a taxon, if not already
                                imparted, costs 2^(-i). For instance, the taxon
                                old/new/new will costs 2^-2 + 2^-3 = 0.375.
                        • linear: simply count the number of new edges.
    -o --output=PATH    The path of the resulting report. If it is omitted, and
                        DB_PATH is of the form PREFIX_db.json, a value of
                        PREFIX_recommendations.json is used. [default: ]
    -p --pipe=PATH      Path of the command pipeline. If it is omitted, and
                        DB_PATH is of the form PREFIX_db.json, a value of
                        PREFIX_pipe.py is used. If the associated file is
                        missing or malformed, no filter is applied. [default: ]


DESCRIPTION:
    Walk a directory, tag its Python files and make a database of the results.
"""

import json
import sys
from pathlib import Path

import regex  # type: ignore
from typed_ast.ast3 import literal_eval

from ..recommend_programs import Recommendations


def cli_wrapper(args):
    db_path = Path(args["DB_PATH"])
    parent_path = db_path.parent
    m = regex.fullmatch(r"(.+)[_-]db\.json", db_path.name)
    prefix = m[1] if m else None
    pipeline_path = Path(args["--pipe"] or parent_path / f"{prefix}_pipe.py")
    if pipeline_path.is_file():
        try:
            commands = literal_eval(pipeline_path.read_text())
        except Exception:  # Too many possible exceptions
            sys.exit(f"The pipeline '{pipeline_path}' is malformed: aborted.")
    elif args["--pipe"]:
        sys.exit(f"No pipeline at '{pipeline_path}': aborted.")
    else:
        commands = []
    rec = Recommendations(
        commands=commands,
        db=json.loads(db_path.read_text()),
        base_path=Path(args["--base"] or parent_path),
        cost_assessment_strategy=args["--cost"],
    )
    rec.run_pipeline()
    output_path = Path(args["--output"] or parent_path / f"{prefix}_recommendations.md")
    output_path.write_text(rec.get_markdown())
    print(f"Dumped: {output_path.resolve()}.\n")
