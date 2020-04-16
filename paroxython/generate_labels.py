from bisect import insort
from collections import defaultdict
from pathlib import Path
from typing import List, Set

from user_types import Label, LabelsSpans, Program, Programs, Source
from list_programs import list_programs
from parse_program import ProgramParser
from mark_internal_imports import InternalImportsMarker


def generate_labelled_sources(directory: Path, *args, **kargs) -> List[Source]:
    """For each program, yield its source with its labels in comment."""
    result = []
    programs = list_programs(directory, *args, **kargs)
    may_mark_as_internal = InternalImportsMarker(programs)
    parse = ProgramParser()
    separator = "-" * 88
    for program in programs:
        may_mark_as_internal.reset()
        result.append(Source(f"# {separator}\n# {program.name}\n# {separator}"))
        lines = program.source.splitlines()
        comments: List[Set[str]] = [set() for _ in lines]
        for (label_name, spans) in parse(program):
            label_name = may_mark_as_internal(label_name)
            for span in spans:
                comments[span.start - 1].add(f"{label_name}{span.suffix}")
        for (i, comment) in enumerate(comments):
            if comment:
                lines[i] += " # " + ", ".join(sorted(comment))
        result.append(Source("\n".join(lines + [""])))
    return result


def generate_labelled_programs(directory: Path, *args, **kargs) -> Programs:
    """For each program, yield its label list, lexicographically sorted."""
    result = []
    programs = list_programs(directory, *args, **kargs)
    may_mark_as_internal = InternalImportsMarker(programs)
    parse = ProgramParser()
    for program in programs:
        may_mark_as_internal.reset()
        label_dict: LabelsSpans = defaultdict(list)
        for (label_name, spans) in parse(program):
            label_name = may_mark_as_internal(label_name)
            for span in spans:
                insort(label_dict[label_name], span)
        labels = [Label(name, span) for (name, span) in label_dict.items()]
        result.append(
            Program(
                name=program.name,
                source=program.source,
                labels=labels,
                links=list(may_mark_as_internal.internal_imports),
            )
        )
    return result


if __name__ == "__main__":
    for result in generate_labelled_sources(Path("../Python/project_euler")):
        print(result)
