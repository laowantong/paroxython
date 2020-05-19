from pathlib import Path
from typing import Iterator

import regex  # type: ignore

from .preprocess_source import Cleanup, centrifugate_hints, collect_hints, remove_hints
from .user_types import Program, ProgramName, Programs, Source


def list_programs(
    directory: Path,
    cleanup_strategy: str = "full",
    glob_pattern: str = "",
    exclude_pattern: str = "",
    *args,
    **kwargs,
) -> Programs:
    """List recursively all Python `Program`s of a given directory."""
    result: Programs = []
    cleanup = Cleanup(cleanup_strategy)
    glob_pattern = glob_pattern or "**/*.py"
    exclude_pattern = exclude_pattern or r"^(__init__|setup|.*[-_]tests?)\.py$"
    match_excluded = regex.compile(exclude_pattern).fullmatch
    for program_path in sorted(directory.rglob(glob_pattern)):
        if not match_excluded(program_path.name):
            source = cleanup.run(Source(program_path.read_text()))
            relative_path = program_path.relative_to(directory)
            result.append(get_program(source, relative_path))
    return result


def get_program(source: Source, relative_path: Path = None) -> Program:
    """Construct a `Program` of its `Source` and relative `Path`.

    The result consists in:

    - the program `Path`, empty or relative to the directory passed to `list_programs()`;
    - its centrifugated `Source`;
    - the hints scheduled for addition or deletion;
    - its `labels`, currently empty, to be later populated by label_programs.py.
    """
    source = centrifugate_hints(source)
    (addition, deletion) = collect_hints(source)
    source = remove_hints(source)
    return Program(
        name=ProgramName(str(relative_path or Path())),
        source=source,
        addition=addition,
        deletion=deletion,
        labels=[],
        taxons=[],
    )


def iterate_and_print_programs(programs: Programs) -> Iterator[Program]:
    """Wrap the iteration of programs into a logger."""
    blanks = ""
    for (i, program) in enumerate(programs, 1):
        print(f"\r{blanks}\r{i: 5} {program.name}", end="", flush=True)
        blanks = " " * (len(program.name) + 7)
        if i == len(programs):  # Placed after the loop, the next line would not be executed.
            print(f"\r{blanks}\r", end="", flush=True)
        yield program


if __name__ == "__main__":
    datetime = __import__("datetime").datetime
    directory = Path("../Algo/programs/")
    for program in list_programs(
        directory,
        exclude_pattern=r"^(__init__|setup|.*[-_]tests?|quiz_.*)\.py$",
        cleanup_strategy="full",
    ):
        path = directory / program.name
        print(datetime.fromtimestamp(path.stat().st_mtime))
        print(program.source)
        print("-" * 80)
