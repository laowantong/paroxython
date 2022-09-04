r"""Walk a directory, tag its Python files and make a database of the results.

USAGE:
    ```
    paroxython collect [options] DIRECTORY
    ```

OPTIONS:
    ```plain
    -c --cleanup=STR    Transformation to apply to the source code before
                        processing. [default: full]
                        Currently available:
                        • full: remove all blank lines, docstrings and
                                comments (except Paroxython hints).
                        • none: no transformation is applied.
    -e --skip=REGEX     Filter out any file whose name fully matches this
                        regular expression. NB: --glob precedes --skip.
                        [default: (__init__|setup|.*[-_]tests?)\.py]
    -g --glob=PATTERN   The names of the collected files must match this Unix-
                        like glob pattern (not a regular expression). Special
                        syntax: "**/" prefix means “this directory and all
                        subdirectories, recursively”. [default: **/*.py]
    --log               Print a detailed report of the labelling times.
    --no_timestamp      Don't store programs' last modification date.
    -o --output=PATH    The path of the resulting database. If not specified,
                        create a JSON file under the name "DIRECTORY_db.json".
                        Otherwise, use the extension (either ".json", ".sql"
                        or ".sqlite") to decide the format of the tag database.
                        [default: ]
    -t --taxonomy=PATH  The path of a TSV file mapping labels onto taxa. If not
                        specified, use the "taxonomy.tsv" present in DIRECTORY's
                        parent. If absent, use the included default taxonomy:
                        https://github.com/laowantong/paroxython/blob/0.7.0/paroxython/resources/taxonomy.tsv
    ```
"""

from pathlib import Path

from .goodies import print_exit
from .make_db import TagDatabase


def cli_wrapper(args):
    directory = Path(args["DIRECTORY"])
    if not directory.is_dir():
        print_exit(f"no directory at '{directory.absolute()}': aborted.")
    taxonomy = args.get("--taxonomy")
    if taxonomy:
        taxonomy_path = Path(taxonomy)
    else:
        taxonomy_path = directory.parent / "taxonomy.tsv"
        if not taxonomy_path.is_file():
            taxonomy_path = None
    db = TagDatabase(
        directory=directory,
        ignore_timestamps=args["--no_timestamp"],
        cleanup_strategy=args["--cleanup"],  # -> list_programs
        skip_pattern=args["--skip"],  # -> list_programs
        glob_pattern=args["--glob"],  # -> list_programs
        print_performances=args["--log"],  # -> labelled_programs
        taxonomy_path=taxonomy_path,  # -> Taxonomy
    )
    if not args["--output"]:
        db.write_json()
    elif args["--output"].endswith(".json"):
        db.write_json(Path(args["--output"]))
    elif args["--output"].endswith((".sqlite", ".sql")):
        db.write_sqlite(Path(args["--output"]))
