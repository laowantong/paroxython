import sys
from bisect import insort
from collections import defaultdict
from pathlib import Path
import regex

sys.path[0:0] = [str(Path(__file__).parent)]

from parser import Parser


class Scanner:
    """Tag the Python programs of a given directory.

    For each program, produce its path and its tags. Here, a tag is intended
    as a label accompanied by a list of spots. A spot is currently defined as
    a couple of line numbers delimiting the start and the end of the construct.
    """

    def __init__(self, directory, cleanup_strategy="minimize"):
        self.parse = Parser()
        self.directory = Path(directory)
        self.set_cleanup_strategy(cleanup_strategy)

    def set_cleanup_strategy(self, strategy):
        """Select the pre-processing method to apply to the source-code."""
        if strategy == "minimize":
            minimize = __import__("minimizer").minimize
            main = regex.compile(r"(?ms)^if +__name__ *== *.__main__. *:.+").sub
            decorator = regex.compile(r"(?m)^\s*@.+\n").sub
            self.cleanup = lambda source: decorator("", main("", minimize(source)))
        else:
            self.cleanup = lambda source: source

    def generate_paths(self):
        """Find and yield the Python programs included in a given directory."""
        exclude_file = regex.compile(r"__init__\.py|setup\.py|.*[-_]tests?\.py")
        for path in sorted(self.directory.rglob("*.py")):
            if not exclude_file.match(path.name):
                print(path)
                yield path

    def generate_tagged_source_codes(self):
        """For each program of a given directory, yield its tagged source-code."""
        separator = "-" * 88
        for path in self.generate_paths():
            yield f"# {separator}\n# {path}\n# {separator}"
            source = self.cleanup(path.read_text())
            sloc = source.splitlines()
            comments = [set() for _ in sloc]
            for (label, spots) in sorted(self.parse(source)):
                for spot in spots:
                    comments[spot.start - 1].add(f"{label}{spot.suffix}")
            for (i, comment) in enumerate(comments):
                if comment:
                    sloc[i] += " # " + ", ".join(sorted(comment))
            yield "\n".join(sloc + [""])

    def generate_lists_of_tags(self):
        """For each program of a given directory, yield its tag list."""
        for path in self.generate_paths():
            source = self.cleanup(path.read_text())
            tags = defaultdict(list)
            for (label, spots) in sorted(self.parse(source)):
                for spot in spots:
                    insort(tags[label], spot)
            yield (str(path), tags)


if __name__ == "__main__":
    scan = Scanner("../Algo/programs/")
    for result in scan.generate_tagged_source_codes():
        print(result)
