from pathlib import Path
from typing import Iterator

import regex  # type: ignore

from preprocess_source import cleanup_factory, centrifugate_hints, collect_hints, remove_hints
from user_types import Program, ProgramName, Programs, Source

match_excluded = regex.compile(
    r"""(?x)
    __init__\.py
    |
    setup\.py
    |
    .*[-_]tests?\.py
    |
    quiz_.*\.py
"""
).match


def list_programs(directory: Path, cleanup_strategy: str = "strip_docs") -> Programs:
    """List recursively all Python `Programs` of a given directory."""
    result: Programs = []
    cleanup = cleanup_factory(cleanup_strategy)
    for program_path in generate_program_paths(directory):
        source = cleanup(Source(program_path.read_text()))
        relative_path = program_path.relative_to(directory)
        result.append(get_program(source, relative_path))
    return result


def generate_program_paths(directory: Path) -> Iterator[Path]:
    """Generate recursively the paths of all Python files of a given directory."""
    for program_path in sorted(directory.rglob("*.py")):
        if not match_excluded(program_path.name):
            yield program_path


def get_program(source: Source, relative_path: Path = None) -> Program:
    """Construct a `Program` of its `Source` and relative `Path`.

    The result consists in:
    - the program `Path`, empty or relative to the directory passed to list_programs()
    - its centrifugated `Source`,
    - the hints scheduled for addition or deletion.
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
        labels=[],  # necessary, since the default value is mutable.
    )


if __name__ == "__main__":
    datetime = __import__("datetime").datetime
    directory = Path("../Algo/programs/")
    for program in list_programs(directory):
        path = directory / program.name
        print(datetime.fromtimestamp(path.stat().st_mtime))
        print(program.source)
        print("-" * 80)
