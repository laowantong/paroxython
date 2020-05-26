from bisect import insort
from collections import defaultdict
from pathlib import Path
from typing import Iterator, List, Set

from .list_programs import list_programs, iterate_and_print_programs
from .parse_program import ProgramParser
from .user_types import Label, LabelName, LabelsSpans, Program, ProgramName, Source


class ProgramLabeller:
    """Populate the labels of one or more programs."""

    def __init__(self):
        self.parse = ProgramParser()

    def label_programs(self, directory: Path, *args, **kwargs) -> None:
        """Complete all fields of a list of programs."""
        self.directory = directory
        self.programs = list_programs(self.directory, *args, **kwargs)
        self.internal_program_names = {p.name for p in self.programs}
        print(f"Labelling {len(self.programs)} programs.")
        for program in iterate_and_print_programs(self.programs):
            self.label_program(program)
        for program in self.programs:
            self.tweak_internal_import_labels(program)

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

    def generate_labelled_sources(self, *args, **kwargs) -> Iterator:
        """For each program, yield its source with its labels in comment."""
        separator = "-" * 88
        for program in self.programs:
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
    labeller = ProgramLabeller()
    labeller.label_programs(Path("examples/simple/programs"))
    for result in labeller.generate_labelled_sources():
        print(result)
