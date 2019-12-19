import sys
from bisect import insort
from collections import defaultdict
from pathlib import Path
from typing import List, NamedTuple, Iterator, Dict, Set

from program_generator import Program
from source_parser import SourceParser
from span import Span


class Label(NamedTuple):
    name: str
    span: List[Span]


class ProgramLabels(NamedTuple):
    path: Path
    labels: List[Label]


def generate_labeled_sources(programs: List[Program]) -> Iterator[str]:
    """For each program, yield its labeled source-code."""
    parse = SourceParser()
    separator = "-" * 88
    for (path, source) in programs:
        yield f"# {separator}\n# {path}\n# {separator}"
        sloc = source.splitlines()
        comments: List[Set[str]] = [set() for _ in sloc]
        for (label_name, spans) in sorted(parse(source)):
            for span in spans:
                comments[span.start - 1].add(f"{label_name}{span.suffix}")
        for (i, comment) in enumerate(comments):
            if comment:
                sloc[i] += " # " + ", ".join(sorted(comment))
        yield "\n".join(sloc + [""])


def generate_programs_labels(programs: List[Program]) -> Iterator[ProgramLabels]:
    """For each program, yield its label list, lexicographically sorted.

    Input: an iterator on programs:
        (path_1, source_1), (path_2, source_2), ...

    Output: an iterator on label lists:
        (path_1, [label_1, label_2, ...]),
        (path_2, [label_1, label_2, ...]),
        ...
    """
    parse = SourceParser()
    for (path, source) in programs:
        label_dict: Dict[str, List[Span]] = defaultdict(list)
        for (label_name, spans) in sorted(parse(source)):
            for span in spans:
                insort(label_dict[label_name], span)
        labels = [Label(name, span) for (name, span) in label_dict.items()]
        yield ProgramLabels(path, labels)


if __name__ == "__main__":
    generate_programs = __import__("program_generator").generate_programs
    programs = generate_programs("../Python/project_euler")
    for result in generate_labeled_sources(programs):
        print(result)
