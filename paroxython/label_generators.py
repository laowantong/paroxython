from bisect import insort
from collections import defaultdict
from typing import Iterator, List, Set

import regex  # type: ignore

from declarations import Label, LabelsSpans, PathLabels, Programs, Source
from manual_hints import retrieve_manual_hints
from source_parser import SourceParser

replace_paroxython_hints = regex.compile(r"\s*# paroxython: .*").sub


def generate_labeled_sources(programs: Programs) -> Iterator[Source]:
    """For each program, yield its labeled source-code."""
    parse = SourceParser()
    separator = "-" * 88
    for (path, source) in programs:
        yield Source(f"# {separator}\n# {path}\n# {separator}")
        manual_hints = retrieve_manual_hints(source)
        source = replace_paroxython_hints("", source)
        sloc = source.splitlines()
        comments: List[Set[str]] = [set() for _ in sloc]
        for (label_name, spans) in sorted(parse(source, manual_hints)):
            for span in spans:
                comments[span.start - 1].add(f"{label_name}{span.suffix}")
        for (i, comment) in enumerate(comments):
            if comment:
                sloc[i] += " # " + ", ".join(sorted(comment))
        yield Source("\n".join(sloc + [""]))


def generate_programs_labels(programs: Programs) -> Iterator[PathLabels]:
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
        label_dict: LabelsSpans = defaultdict(list)
        manual_hints = retrieve_manual_hints(source)
        for (label_name, spans) in sorted(parse(source, manual_hints)):
            for span in spans:
                insort(label_dict[label_name], span)
        labels = [Label(name, span) for (name, span) in label_dict.items()]
        yield PathLabels(path, labels)


if __name__ == "__main__":
    generate_programs = __import__("program_generator").generate_programs
    programs = generate_programs("../Python/project_euler")
    for result in generate_labeled_sources(programs):
        print(result)
