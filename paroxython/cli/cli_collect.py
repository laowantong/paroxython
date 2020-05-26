r"""
USAGE:
    paroxython collect [options] DIRECTORY

OPTIONS:
    -c --cleanup=STR    Transformation to be applied to the source code
                        before processing. [default: full]
                        Currently available:
                        • full: remove all blank lines, docstrings and
                                comments (except Paroxython hints).
                        • none: no transformation is applied.
    -e --exclude=REGEX  Filter out any file whose name fully matches this
                        regular expression. NB: --glob precedes --exclude.
                        [default: "^(__init__|setup|.*[-_]tests?)\.py$"]
    -g --glob=PATTERN   The names of the collected files must match this
                        Unix-like glob pattern (not a regular expression).
                        Special syntax: "**/" prefix means “this directory
                        and all subdirectories, recursively”. [default:
                        "**/*.py"]
    -o --output=PATH    The path of the resulting database. If not
                        specified, create a JSON file under the name
                        "DIRECTORY_db.json". Otherwise, use the extension
                        (either ".json" or ".sqlite") to decide the format
                        of the database. [default: ]
    -t --taxonomy=PATH  The path of a TSV file mapping labels onto taxons.
                        If not specified, use the included copy of the table
                        whose last version is at https://bit.ly/2Yu0LqU.

DESCRIPTION:
    Walk a directory, tag its Python files and make a database of the results.
"""

from pathlib import Path

from ..make_db import Database


def cli_wrapper(args):
    db = Database(
        directory=Path(args["DIRECTORY"]),
        ignore_timestamps=False,
        cleanup_strategy=args["--cleanup"],
        exclude_pattern=args["--exclude"],
        glob_pattern=args["--glob"],
        taxonomy_path=Path(args["--taxonomy"]) if args["--taxonomy"] else None,
    )
    if not args["--output"]:
        db.write_json()
    elif args["--output"].endswith(".json"):
        db.write_json(Path(args["--output"]))
    elif args["--output"].endswith(".sqlite"):
        db.write_sqlite(Path(args["--output"]))
