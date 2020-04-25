from bisect import insort
from collections import defaultdict
from pathlib import Path
from typing import Iterator, List, Set

from list_programs import generate_program_paths, list_programs, iterate_and_print_programs
from parse_program import ProgramParser
from user_types import Label, LabelName, LabelsSpans, Program, ProgramName, Programs, Source


class ProgramLabeller:
    """Populate the labels of one or more programs."""

    def __init__(self, directory: Path, *args, **kargs):
        self.directory = directory
        self.internal_program_names = {p.name for p in generate_program_paths(directory)}
        self.parse = ProgramParser()

    def list_labelled_programs(self, *args, **kargs) -> Programs:
        """Return a list of programs with all their fields completed."""
        print(self.directory, *args, **kargs)
        programs = list_programs(self.directory, *args, **kargs)
        print(f"Labelling {len(programs)} programs.")
        for program in iterate_and_print_programs(programs):
            self.label_program(program)
        for program in programs:
            self.tweak_internal_import_labels(program)
        return programs

    def label_program(self, program: Program) -> None:
        """Compute the labels of a given program and store the result in its `labels` field."""
        label_dict: LabelsSpans = defaultdict(list)
        for (label_name, spans) in self.parse(program):
            for span in spans:
                insort(label_dict[label_name], span)
        program.labels[:] = [Label(name, span) for (name, span) in label_dict.items()]

    def tweak_internal_import_labels(self, program: Program) -> None:
        """Modify the appropriate labels in-place to mark internal importations."""
        for (i, label) in enumerate(program.labels):
            if label.name.startswith(("import:", "import_module:")):
                parts = label.name.split(":")
                imported_name = ProgramName(f"{parts[1]}.py")
                if imported_name in self.internal_program_names:
                    program.labels[i] = Label(
                        name=LabelName(f"{parts[0]}_internally:{':'.join(parts[1:])}"),
                        spans=label.spans,
                    )

    def generate_labelled_sources(self, *args, **kargs) -> Iterator:
        """For each program, yield its source with its labels in comment."""
        programs = self.list_labelled_programs(*args, **kargs)
        separator = "-" * 88
        for program in programs:
            yield Source(f"# {separator}\n# {program.name}\n# {separator}")
            lines = program.source.splitlines()
            comments: List[Set[str]] = [set() for _ in lines]
            for label in program.labels:
                for span in label.spans:
                    span_length = span.end - span.start
                    span_suffix = f" (-> +{span_length})" if span_length else ""
                    comments[span.start - 1].add(f"{label.name}{span_suffix}")
            for (i, comment) in enumerate(comments):
                if comment:
                    lines[i] += " # " + ", ".join(sorted(comment))
            yield Source("\n".join(lines + [""]))


if __name__ == "__main__":
    labeller = ProgramLabeller(Path("../Python/project_euler"))
    for result in labeller.generate_labelled_sources():
        print(result)
