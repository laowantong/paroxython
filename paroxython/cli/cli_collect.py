r"""
USAGE:
    paroxython collect [options] DIRECTORY

OPTIONS:
    -g --glob=PATTERN  The names of the collected files must match this Unix-like glob pattern
                        (not a regular expression). Special syntax: "**/" prefix means “this
                        directory and all subdirectories, recursively”. [default: "**/*.py"]
    -e --exclude=REGEX  Filter out any file whose name fully matches this regular expression.
                        [default: "^(__init__|setup|.*[-_]tests?)\.py$"]
    -c --cleanup=STR    Transformation to be applied to the source-codes before their processing.
                        [default: full]
                        Currently available:
                        • full: remove all blank lines, docstrings and comments (except Paroxython
                                hints).
                        • none: no transformation is applied.
    -o --output=PATH    The path of the resulting database. If not specified, create a JSON file
                        under the name "DIRECTORY_db.json". Otherwise, use the extension (either
                        ".json" or ".sqlite") to decide the format of the database. [default: ]

DESCRIPTION:
    Walk a directory, tag its Python files and make a database of the results.
"""

from pathlib import Path

from ..make_db import Database


def cli_wrapper(args):
    db = Database(
        directory=Path(args["DIRECTORY"]),
        cleanup_strategy=args["--cleanup"],
        exclude_pattern=args["--exclude"],
        glob_pattern=args["--glob"],
    )
    if not args["--output"]:
        db.write_json()
    elif args["--output"].endswith(".json"):
        db.write_json(args["--output"])
    elif args["--output"].endswith(".sqlite"):
        db.write_sqlite(Path(args["--output"]))
