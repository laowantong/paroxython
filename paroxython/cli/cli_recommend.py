"""
USAGE:
    paroxython recommend [options] PIPELINE_PATH

OPTIONS:
    --db=DB_PATH        Path of the JSON database. If it is omitted, and PIPELINE_PATH is of the
                        form PREFIX_pipe.py, a value of PREFIX_db.json is used. [default: ]
    --base=PATH         Value accessible by any shell command of the pipeline. If not specified,
                        this is parent directory of PIPELINE_PATH. [default: ]
    -o --output=PATH    The path of the resulting report. If it is omitted, and PIPELINE_PATH is
                        of the form PREFIX_pipe.py, a value of PREFIX_recommendations.json is
                        used. [default: ]
    -c --cost=STR       Learning cost assessment strategy. [default: zeno]
                        Currently available:
                        • zeno: the i-th segment of a taxon, if not already imparted, costs 2^(-i).
                                For instance, the taxon old/new/new will costs 2^-2 + 2^-3 = 0.375.
                        • length: simply count the number of new segments.


DESCRIPTION:
    Walk a directory, tag its Python files and make a database of the results.
"""

import regex  # type: ignore
from pathlib import Path
import json
import context
from recommend_programs import Recommendations
from typed_ast.ast3 import literal_eval


def cli_wrapper(args):
    pipeline_path = Path(args["PIPELINE_PATH"])
    parent_path = pipeline_path.parent
    m = regex.fullmatch(r"(.+)[_-]pipe(?:line)?\.py", pipeline_path.name)
    prefix = m[1] if m else None
    rec = Recommendations(
        commands=literal_eval(pipeline_path.read_text()),
        db=json.loads(Path(args["--db"] or parent_path / f"{prefix}_db.json").read_text()),
        base_path=Path(args["--base"] or parent_path),
        output_path=Path(args["--output"] or parent_path / f"{prefix}_recommendations.md"),
        cost_assessment_strategy=args["--cost"],
    )
    rec.run_pipeline()
    text = rec.get_markdown()
    rec.dump(text)
