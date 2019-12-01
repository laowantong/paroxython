import sys
from bisect import insort
from collections import defaultdict
from pathlib import Path

import regex

sys.path[0:0] = [str(Path(__file__).parent)]

from parser import Parser


def generate_labeled_sources(programs):
    """For each program (path, source-code), yield its labeled source-code."""
    parse = Parser()
    separator = "-" * 88
    for (path, source) in programs:
        yield f"# {separator}\n# {path}\n# {separator}"
        sloc = source.splitlines()
        comments = [set() for _ in sloc]
        for (label_name, spots) in sorted(parse(source)):
            for spot in spots:
                comments[spot.start - 1].add(f"{label_name}{spot.suffix}")
        for (i, comment) in enumerate(comments):
            if comment:
                sloc[i] += " # " + ", ".join(sorted(comment))
        yield "\n".join(sloc + [""])


def generate_paths_and_labels(programs):
    """For each program, yield its label list, lexicographically sorted.
    
    Input: an iterator on programs:
        (path_1, source_1), (path_2, source_2), ...
    
    Output: an iterator on label lists: 
        (path_1, [
            (label_name_1, label_spots_1),
            (label_name_2, label_spots_2),
            ...
        ]), ...
    """
    parse = Parser()
    for (path, source) in programs:
        labels = defaultdict(list)
        for (label_name, spots) in sorted(parse(source)):
            for spot in spots:
                insort(labels[label_name], spot)
        yield (path, labels)


if __name__ == "__main__":
    generate_programs = __import__("program_generator").generate_programs
    programs = generate_programs("../Python/project_euler")
    for result in generate_labeled_sources(programs):
        print(result)
