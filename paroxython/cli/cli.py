#! /usr/bin/env python
"""Command line interface for the main functionalities of Paroxython.

USAGE:
    ```
    paroxython [--version] [--help] COMMAND [ARGS...]
    ```

COMMANDS:
    ```plain
    tag         Tag one Python file and output the table of its taxa or
                labels.
    collect     Walk a directory, tag its Python files and make a JSON
                database of the results.
    recommend   Read and execute a pipeline of commands and report the learning
                costs.
    ```

Type `paroxython COMMAND --help` for more information on a specific command.
"""
import sys
from importlib import import_module
from .. import PAROXYTHON_VERSION

from docopt import docopt  # type: ignore
import regex  # type: ignore

if sys.version < "3.6":  # pragma: no cover
    print(f"Paroxython requires Python 3.6 or later to run.\nThis version is {sys.version}.")
    sys.exit()


def main():
    global __doc__
    __doc__ = regex.sub(r"(?m)^ *```.*\n", "", __doc__)  # suppress Markdown code delimiters
    args = docopt(__doc__, version=f"paroxython version {PAROXYTHON_VERSION}", options_first=True)
    if not args.get("COMMAND"):  # pragma: no cover
        sys.exit(__doc__)
    command_name = args["COMMAND"].lower()
    command_args = [command_name] + args["ARGS"]
    if command_name not in ("tag", "recommend", "collect"):
        sys.exit(f"{command_name} is not a valid command. Type 'paroxython --help'.")
    command = import_module(f"paroxython.cli.cli_{command_name}", "cli_wrapper")
    command.__doc__ = regex.sub(r"(?m)^ *```.*\n", "", command.__doc__)
    command.cli_wrapper(docopt(command.__doc__, argv=command_args))


if __name__ == "__main__":
    main()
