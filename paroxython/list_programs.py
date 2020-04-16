from pathlib import Path

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


def list_programs(directory: Path, strategy="strip_docs") -> Programs:
    """List all Programs of a given directory.

    Each Program (cf. declaration) includes:
    - its Path, relative to the given directory
    - its Source,
    - the hints scheduled for addition or deletion.

    Its labels will later be populated by "generate_labels.py".
    """
    result = []
    cleanup = cleanup_factory(strategy)
    for program_path in sorted(directory.rglob("*.py")):
        if not match_excluded(program_path.name):
            print(program_path)
            source = cleanup(Source(program_path.read_text()))
            source = centrifugate_hints(source)
            (addition, deletion) = collect_hints(source)
            source = remove_hints(source)
            result.append(
                Program(
                    name=ProgramName(str(program_path.relative_to(directory))),
                    source=source,
                    addition=addition,
                    deletion=deletion,
                )
            )
    return result


if __name__ == "__main__":
    datetime = __import__("datetime").datetime
    directory = Path("../Algo/programs/")
    for program in list_programs(directory):
        path = directory / program.name
        print(datetime.fromtimestamp(path.stat().st_mtime))
        print(program.source)
        print("-" * 80)
