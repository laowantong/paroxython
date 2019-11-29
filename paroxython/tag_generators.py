import sys
from bisect import insort
from collections import defaultdict
from pathlib import Path

import regex

sys.path[0:0] = [str(Path(__file__).parent)]

from parser import Parser


def generate_tagged_sources(programs):
    """For each program (path, source-code), yield its tagged source-code."""
    parse = Parser()
    separator = "-" * 88
    for (path, source) in programs:
        yield f"# {separator}\n# {path}\n# {separator}"
        sloc = source.splitlines()
        comments = [set() for _ in sloc]
        for (label, spots) in sorted(parse(source)):
            for spot in spots:
                comments[spot.start - 1].add(f"{label}{spot.suffix}")
        for (i, comment) in enumerate(comments):
            if comment:
                sloc[i] += " # " + ", ".join(sorted(comment))
        yield "\n".join(sloc + [""])


def generate_lists_of_tags(programs):
    """For each program (path, source-code), yield its tag list."""
    parse = Parser()
    for (path, source) in programs:
        tags = defaultdict(list)
        for (label, spots) in sorted(parse(source)):
            for spot in spots:
                insort(tags[label], spot)
        yield (path, tags)


if __name__ == "__main__":
    generate_programs = __import__("program_generator").generate_programs
    programs = generate_programs("../Python/project_euler")
    for result in generate_tagged_sources(programs):
        print(result)
