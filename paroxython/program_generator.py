from pathlib import Path
from typing import Iterator

import regex  # type: ignore

from preprocess_source import cleanup_factory, centrifugate_hints, collect_hints, remove_hints
from declarations import Program, Source

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


def generate_programs(directory: str, strategy="strip_docs") -> Iterator[Program]:
    """Yield all Programs of a given directory.

    Each Program (cf. declaration) includes:
    - its Path,
    - its Source,
    - the hints scheduled for addition or deletion.

    Its labels will later be populated by "label_generators.py".
    """
    cleanup = cleanup_factory(strategy)
    for path in sorted(Path(directory).rglob("*.py")):
        if not match_excluded(path.name):
            print(path)
            source = cleanup(Source(path.read_text()))
            source = centrifugate_hints(source)
            (addition, deletion) = collect_hints(source)
            source = remove_hints(source)
            yield Program(path=path, source=source, addition=addition, deletion=deletion)


if __name__ == "__main__":
    datetime = __import__("datetime").datetime
    for program in generate_programs("../Algo/programs/"):
        print(datetime.fromtimestamp(program.path.stat().st_mtime))
        print(program.source)
        print("-" * 80)
