#! /usr/bin/env python
"""
USAGE:
    paroxython [--version] [--help] COMMAND [ARGS...]

COMMANDS:
    tag         Tag one Python file and output the table of its taxons or
                labels.
    collect     Walk a directory, tag its Python files and make a JSON
                database of the results.
    recommend   Read and execute a pipeline of commands and report the learning
                costs.

Type 'paroxython COMMAND --help' for more information on a specific command.
"""
import sys
from importlib import import_module
import pkg_resources

from docopt import docopt  # type: ignore

if sys.version < "3.6":  # pragma: no cover
    print(f"Paroxython requires Python 3.6 or later to run.\nThis version is {sys.version}.")
    sys.exit()


def main():
    version = pkg_resources.get_distribution("paroxython").version
    args = docopt(__doc__, version=f"paroxython version {version}", options_first=True)
    command_name = args["COMMAND"].lower()
    command_args = [command_name] + args["ARGS"]
    if command_name not in ("tag", "recommend", "collect"):
        sys.exit(f"{command_name} is not a valid command. Type 'paroxython --help'.")
    command = import_module(f"paroxython.cli.cli_{command_name}", "cli_wrapper")
    command.cli_wrapper(docopt(command.__doc__, argv=command_args))


if __name__ == "__main__":
    main()
