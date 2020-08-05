r"""Walk a directory, tag its Python files and make a database of the results.

USAGE:
    ```
    paroxython collect [options] DIRECTORY
    ```

OPTIONS:
    ```plain
    -c --cleanup=STR    Transformation to be applied to the source code
                        before processing. [default: full]
                        Currently available:
                        • full: remove all blank lines, docstrings and
                                comments (except Paroxython hints).
                        • none: no transformation is applied.
    -e --skip=REGEX     Filter out any file whose name fully matches this
                        regular expression. NB: --glob precedes --skip.
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
                        of the tag database. [default: ]
    --no_timestamp      Don't store programs' last modification date.
    -t --taxonomy=PATH  The path of a TSV file mapping labels onto taxa.
                        If not specified, use the included default taxonomy:
                        https://github.com/laowantong/paroxython/blob/0.4.3/paroxython/resources/taxonomy.tsv
    ```
"""

from pathlib import Path

from ..make_db import Database


def cli_wrapper(args):
    taxonomy_path = Path(args["--taxonomy"]) if args["--taxonomy"] else None
    db = Database(
        directory=Path(args["DIRECTORY"]),
        ignore_timestamps=args["--no_timestamp"],
        cleanup_strategy=args["--cleanup"],  # -> list_programs
        skip_pattern=args["--skip"],  # -> list_programs
        glob_pattern=args["--glob"],  # -> list_programs
        taxonomy_path=taxonomy_path,  # -> Taxonomy
    )
    if not args["--output"]:
        db.write_json()
    elif args["--output"].endswith(".json"):
        db.write_json(Path(args["--output"]))
    elif args["--output"].endswith(".sqlite"):
        db.write_sqlite(Path(args["--output"]))
