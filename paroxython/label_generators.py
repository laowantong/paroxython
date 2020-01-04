from bisect import insort
from collections import defaultdict
from typing import Iterator, List, Set

from declarations import Label, LabelsSpans, Program, Source
from program_generator import generate_programs
from program_parser import ProgramParser


def generate_labeled_sources(directory: str, *args, **kargs) -> Iterator[Source]:
    """For each program, yield its source with its labels in comment."""
    parse = ProgramParser()
    separator = "-" * 88
    for program in generate_programs(directory, *args, **kargs):
        yield Source(f"# {separator}\n# {program.path}\n# {separator}")
        sloc = program.source.splitlines()
        comments: List[Set[str]] = [set() for _ in sloc]
        for (label_name, spans) in sorted(parse(program)):
            for span in spans:
                comments[span.start - 1].add(f"{label_name}{span.suffix}")
        for (i, comment) in enumerate(comments):
            if comment:
                sloc[i] += " # " + ", ".join(sorted(comment))
        yield Source("\n".join(sloc + [""]))


def generate_labeled_programs(directory: str, *args, **kargs) -> Iterator[Program]:
    """For each program, yield its label list, lexicographically sorted."""
    parse = ProgramParser()
    for program in generate_programs(directory, *args, **kargs):
        label_dict: LabelsSpans = defaultdict(list)
        for (label_name, spans) in sorted(parse(program)):
            for span in spans:
                insort(label_dict[label_name], span)
        labels = [Label(name, span) for (name, span) in label_dict.items()]
        yield Program(path=program.path, source=program.source, labels=labels)


if __name__ == "__main__":
    for result in generate_labeled_sources("../Python/project_euler"):
        print(result)
