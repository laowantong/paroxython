from pathlib import Path
from typing import Iterator, NamedTuple

import regex

from cleanup_source import cleanup_factory


class Program(NamedTuple):
    path: Path
    source: str


match_excluded = regex.compile(r"__init__\.py|setup\.py|.*[-_]tests?\.py").match


def generate_programs(directory: str, strategy="strip_docs") -> Iterator[Program]:
    """Yield the path and the cleaned up source of all programs in a given directory."""

    cleanup = cleanup_factory(strategy)
    directory_path = Path(directory)
    for path in sorted(directory_path.rglob("*.py")):
        if not match_excluded(path.name):
            print(path)
            yield Program(path, cleanup(path.read_text()))


if __name__ == "__main__":
    datetime = __import__("datetime").datetime
    for (path, source) in generate_programs("../Algo/programs/"):
        print(datetime.fromtimestamp(path.stat().st_mtime))
        print(source)
        print("-" * 80)
