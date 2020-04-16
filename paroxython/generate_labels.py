from bisect import insort
from collections import defaultdict
from pathlib import Path
from typing import Iterator, List, Set

from user_types import Label, LabelsSpans, Program, Source
from list_programs import list_programs
from parse_program import ProgramParser


def generate_labelled_sources(directory: Path, *args, **kargs) -> Iterator[Source]:
    """For each program, yield its source with its labels in comment."""
    parse = ProgramParser()
    separator = "-" * 88
    for program in list_programs(directory, *args, **kargs):
        yield Source(f"# {separator}\n# {program.name}\n# {separator}")
        lines = program.source.splitlines()
        comments: List[Set[str]] = [set() for _ in lines]
        for (label_name, spans) in parse(program):
            for span in spans:
                comments[span.start - 1].add(f"{label_name}{span.suffix}")
        for (i, comment) in enumerate(comments):
            if comment:
                lines[i] += " # " + ", ".join(sorted(comment))
        yield Source("\n".join(lines + [""]))


def generate_labelled_programs(directory: Path, *args, **kargs) -> Iterator[Program]:
    """For each program, yield its label list, lexicographically sorted."""
    parse = ProgramParser()
    for program in list_programs(directory, *args, **kargs):
        label_dict: LabelsSpans = defaultdict(list)
        for (label_name, spans) in parse(program):
            for span in spans:
                insort(label_dict[label_name], span)
        labels = [Label(name, span) for (name, span) in label_dict.items()]
        yield Program(name=program.name, source=program.source, labels=labels)


if __name__ == "__main__":
    for result in generate_labelled_sources(Path("../Python/project_euler")):
        print(result)
