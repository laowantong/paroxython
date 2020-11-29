r"""
Read and execute a pipeline of commands and report the learning costs.

USAGE:
    ```
    paroxython recommend [options] DB_PATH
    ```

DESCRIPTION:
    ```plain
    Requires an existing database previously generated by the command:

        paroxython collect DIRECTORY

    ... and a pipeline of commands describing which concepts (taxa) are
    already known, which ones need to be illustrated or must be avoided. By
    default, it results in a list of recommended programs, along with their
    total learning costs and the individual learning cost of each of the
    concepts they feature. These results are presented in Markdown format.
    With the option `-o stdout` the program list is simply printed to stdout.
    ```

SHORTCUT:
    ```plain
    For DB_PATH, instead of the path of a tag database, you can provide the
    DIRECTORY previously collected. Paroxython will automatically look for the
    tag database at DIRECTORY/../DIRECTORY_db.json.
    ```

OPTIONS:
    ```plain
    -b --base=PATH      Value accessible, with the syntax "{base}", by any shell
                        command of the pipeline. If not specified, this is the
                        parent directory of DB_PATH. [default: ]
    -c --cost=STR       Learning cost assessment strategy. [default: zeno]
                        Currently available:
                        • zeno: the i-th edge of a taxon, if not already
                                imparted, costs 2^(-i). For instance, the taxon
                                old/new/new will costs 2^-2 + 2^-3 = 0.375.
                        • linear: simply count the number of new edges.
    -o --output=PATH    The path of the resulting report. If it is omitted, and
                        DB_PATH is of the form PREFIX_db.json, a value of
                        PREFIX_recommendations.md is used. If it is STDOUT, the
                        sorted list of recommended (but not hidden) programs, is
                        printed on the standard output. [default: ]
    -p --pipe=PATH      Path of the command pipeline. If it is omitted, and
                        DB_PATH is of the form PREFIX_db.json, a value of
                        PREFIX_pipe.py is used. If the associated file is
                        missing or malformed, no filter is applied. [default: ]
    -f --format=STR     The format of program titles in the report. This string
                        can contains the following identifiers (between braces):
                        • name: filename of the program.
                        • path: program key in the DB "programs" dictionary.
                        • prefix: name of DB_PATH, minus any "_db.json" suffix.
                        • absolute: absolute path to DB_PATH's parent folder.
                        • relative: relative path to DB_PATH's parent folder.
                        Shortcut: if format is "vscode", makes program names to
                            be clickable and opening in VS Code.
                        [default: `{name}`]
    ```

EXAMPLE:
    ```plain
    Use `-o stdout` to pipe the results into another shell command. For instance,
    let's assume that:

    - your program repository is `path/to/programs`;
    - your tag database is at its default location `path/to/programs_db.json`;
    - your pipeline is at its default location `path/to/programs_pipe.py`.

    Then, to copy (not move) all the recommended programs to an existing
    directory DEST, just do:

    paroxython recommend -o stdout path/to/programs_db.json \
        | xargs  -I {} sh -c "cp path/to/programs/{} DEST"
    ```
"""

import json
import sys
from pathlib import Path

import regex  # type: ignore
from typed_ast.ast3 import literal_eval

from .goodies import print_success, print_exit
from .recommend_programs import Recommendations


def cli_wrapper(args):
    db_path = Path(args["DB_PATH"])
    if not db_path.exists():
        print_exit(f"no file or directory at '{db_path.absolute()}': aborted.")
    parent_path = db_path.parent
    if db_path.is_dir():
        for suffix in ("_db", "-db"):
            db_path = parent_path / f"{db_path.name}{suffix}.json"
            if db_path.is_file():
                break
        else:
            print_exit(f"unable to locate a tag database in '{parent_path}': aborted.")
    m = regex.fullmatch(r"(.+[_-])db\.json", db_path.name)
    prefix = m[1] if m else ""
    pipeline_path = Path(args["--pipe"] or parent_path / f"{prefix}pipe.py")
    if pipeline_path.is_file():
        try:
            commands = literal_eval(pipeline_path.read_text())
        except Exception:  # Too many possible exceptions
            print_exit(f"the pipeline '{pipeline_path}' is malformed: aborted.")
    elif args["--pipe"]:
        print_exit(f"no pipeline at '{pipeline_path}': aborted.")
    else:
        commands = []
    stdout_backup = sys.stdout
    if args["--output"].upper() == "STDOUT":
        sys.stdout = sys.stderr
    title_format = args["--format"]
    if title_format.lower() == "vscode":
        title_format = "[`{name}`](vscode://file/{absolute}/{prefix}/{path})"
    title_format = title_format.format(
        name="{name}",
        path="{path}",
        prefix=prefix.rstrip("_-"),
        absolute=parent_path.resolve(),
        relative=parent_path,
    )
    rec = Recommendations(
        db=json.loads(db_path.read_text()),
        base_path=Path(args["--base"] or parent_path),
        assessment_strategy=args["--cost"],
        title_format=title_format,
    )
    rec.run_pipeline(commands)
    if args["--output"].upper() == "STDOUT":
        sys.stdout = stdout_backup
        return print("\n".join(sorted(rec.selected_programs - rec.hidden_programs)))
    output_path = Path(args["--output"] or parent_path / f"{prefix}recommendations.md")
    output_path.write_text(rec.get_markdown())
    print_success(f"Dumped: {output_path.resolve()}\n")
