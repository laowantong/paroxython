from bisect import insort
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Set, Iterator

from goodies import iterate_and_print_programs
from list_programs import list_programs
from parse_program import ProgramParser
from user_types import Label, LabelsSpans, Program, ProgramName, Programs, Source, LabelName


def tweak_internal_import_labels(programs: Programs) -> None:
    """Modify the appropriate labels in-place to mark internal importations."""
    internal_program_names = {program.name for program in programs}
    for program in programs:
        for (i, label) in enumerate(program.labels):
            if label.name.startswith(("import:", "import_module:")):
                parts = label.name.split(":")
                imported_name = ProgramName(f"{parts[1]}.py")
                if imported_name in internal_program_names:
                    program.labels[i] = Label(
                        name=LabelName(f"{parts[0]}_internally:{':'.join(parts[1:])}"),
                        spans=label.spans,
                    )


def list_labelled_programs(directory: Path, *args, **kargs) -> Programs:
    """Return a list of programs with all their fields completed."""
    programs = list_programs(directory, *args, **kargs)
    print(f"Labelling {len(programs)} programs.")
    parse = ProgramParser()
    for program in iterate_and_print_programs(programs):
        label_dict: LabelsSpans = defaultdict(list)
        for (label_name, spans) in parse(program):
            for span in spans:
                insort(label_dict[label_name], span)
        labels = [Label(name, span) for (name, span) in label_dict.items()]
        program.labels[:] = labels
    tweak_internal_import_labels(programs)
    return programs


def generate_labelled_sources(directory: Path, *args, **kargs) -> Iterator:
    """For each program, yield its source with its labels in comment."""
    programs = list_labelled_programs(directory, *args, **kargs)
    separator = "-" * 88
    for program in programs:
        yield Source(f"# {separator}\n# {program.name}\n# {separator}")
        lines = program.source.splitlines()
        comments: List[Set[str]] = [set() for _ in lines]
        for label in program.labels:
            for span in label.spans:
                comments[span.start - 1].add(f"{label.name}{span.suffix}")
        for (i, comment) in enumerate(comments):
            if comment:
                lines[i] += " # " + ", ".join(sorted(comment))
        yield Source("\n".join(lines + [""]))


if __name__ == "__main__":
    for result in generate_labelled_sources(Path("../Python/project_euler")):
        print(result)
