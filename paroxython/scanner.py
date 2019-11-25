import regex
import sys
from pathlib import Path
from collections import defaultdict

sys.path[0:0] = [str(Path(__file__).parent)]

from parser import Parser


class AbstractScanner:
    """Tag the Python programs of a given directory.

    For each program, produce its path and its tags, each one of the latter being
    accompanied by its spots. A spot is currently defined as a couple of
    line numbers delimiting the start and the end of the construct.
    """

    def __init__(self, cleanup_strategy="minimize"):
        self.parse = Parser()
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

    def generate_paths(self, directory: Path):
        """Find and yield the Python programs included in a given directory."""
        exclude_file = regex.compile(r"__init__\.py|setup\.py|.*[-_]tests?\.py")
        for path in sorted(directory.rglob("*.py")):
            if not exclude_file.match(path.name):
                print(path)
                yield path

    def generate_parse_results(self, source):
        for (tag, spots) in sorted(self.parse(source)):
            for spot in spots:
                yield (tag, spot)

    def __call__(self, path):
        raise NotImplementedError("Subclasses must override __call__()!")


class ScannerForStrings(AbstractScanner):
    def __call__(self, path):
        separator = "-" * 88
        for path in self.generate_paths(path):
            source = self.cleanup(path.read_text())
            yield f"# {separator}\n# {path}\n# {separator}"
            sloc = source.splitlines()
            comments = [set() for _ in sloc]
            for (tag, spot) in self.generate_parse_results(source):
                comments[spot.start - 1].add(f"{tag}{spot.suffix}")
            for (i, comment) in enumerate(comments):
                if comment:
                    sloc[i] += " # " + ", ".join(sorted(comment))
            sloc.append("")
            yield "\n".join(sloc)


class ScannerForDatabase(AbstractScanner):
    def __call__(self, path):
        tag_labels = set()
        algos = {}
        for path in self.generate_paths(path):
            source = self.cleanup(path.read_text())
            tags = defaultdict(list)
            for (tag_label, spot) in self.generate_parse_results(source):
                tags[tag_label].append(spot)
                tag_labels.add(tag_label)
            for (tag_label, spots) in tags.items():
                tags[tag_label] = sorted(spots)
            tag_labels.update(tags.keys())
            algos[str(path)] = {"source": source, "tags": tags}
        return {"tag_labels": sorted(tag_labels), "algos": algos}


if __name__ == "__main__":
    Path = __import__("pathlib").Path
    scan = ScannerForStrings()
    for result in scan(Path("../Algo/programs/")):
        print(result)
