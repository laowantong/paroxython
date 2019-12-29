import sys
from collections import defaultdict
from pathlib import Path
from typing import Iterator, List, Set

import regex  # type: ignore

from cleanup_source import cleanup_factory
from source_parser import SourceParser


class Scanner:
    """Tag the Python programs of a given directory.

    For each program, produce its path and its tags. Here, a tag is intended
    as a label accompanied by a list of spots. A spot is currently defined as
    a couple of line numbers delimiting the start and the end of the construct.
    """

    def __init__(self, directory, cleanup_strategy="strip_docs"):
        self.parse = SourceParser()
        self.directory = Path(directory)
        self.cleanup = cleanup_factory(cleanup_strategy)

    def generate_paths(self) -> Iterator[Path]:
        """Find and yield the Python programs included in a given directory."""
        exclude_file = regex.compile(r"__init__\.py|setup\.py|.*[-_]tests?\.py")
        for path in sorted(self.directory.rglob("*.py")):
            if not exclude_file.match(path.name):
                print(path)
                yield path

    def generate_tagged_source_codes(self) -> Iterator[str]:
        """For each program of a given directory, yield its tagged source-code."""
        separator = "-" * 88
        for path in self.generate_paths():
            yield f"# {separator}\n# {path}\n# {separator}"
            source = self.cleanup(path.read_text())
            sloc = source.splitlines()
            comments: List[Set[str]] = [set() for _ in sloc]
            for (label, spots) in sorted(self.parse(source)):
                for spot in spots:
                    comments[spot.start - 1].add(f"{label}{spot.suffix}")
            for (i, comment) in enumerate(comments):
                if comment:
                    sloc[i] += " # " + ", ".join(sorted(comment))
            yield "\n".join(sloc + [""])


if __name__ == "__main__":
    scan = Scanner("../Algo/programs/")
    for result in scan.generate_tagged_source_codes():
        print(result)
