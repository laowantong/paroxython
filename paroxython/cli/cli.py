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

DESCRIPTION:
    Paroxython is a command-line tool which finds and tags algorithmic features
    (such as assignments, nested loops, tail-recursive functions, etc.) in a
    collection of small Python programs, typically gathered for educational
    purposes (e.g., examples, patterns, exercise corrections). Each tag consists
    in a free-form label associated with its spanning lines. These labels are
    then mapped onto a knowledge taxonomy designed by the teacher with basic
    order constraints in mind (e.g., the fact that the introduction of the
    concept of early exit must come after that of loop, which itself requires
    that of control flow, is expressed with the following taxon:
    flow/loop/exit/early). Source codes, labels and taxons are stored in a
    database, which can finally be filtered through a pipeline of inclusion,
    exclusion and impartment commands on programs or taxons.

SEE ALSO:
    Repository  https://github.com/laowantong/paroxython
    Packaging   https://pypi.org/project/paroxython/

LICENSE:
    MIT License

CONTACT:
    Author      Aristide Grange
    Mail        <first_name>.<last_name>@univ-<region>.<country_code>
    Address     Université de Lorraine
                Laboratoire LCOMS - UFR MIM
                3 rue Augustin Fresnel
                Metz, 57000, FRANCE
"""
import sys
from importlib import import_module

from docopt import docopt  # type: ignore

if sys.version < "3.6":  # pragma: no cover
    print(f"Paroxython requires Python 3.6 or later to run.\nThis version is {sys.version}.")
    sys.exit()


def main():
    args = docopt(__doc__, version="paroxython version 0.1.0", options_first=True)
    command_name = args["COMMAND"].lower()
    command_args = [command_name] + args["ARGS"]
    if command_name not in ("tag", "recommend", "collect"):
        sys.exit(f"{command_name} is not a valid command. Type 'paroxython --help'.")
    command = import_module(f"paroxython.cli.cli_{command_name}", "cli_wrapper")
    command.cli_wrapper(docopt(command.__doc__, argv=command_args))


if __name__ == "__main__":
    main()
