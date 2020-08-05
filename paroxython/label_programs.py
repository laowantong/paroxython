"""List all the programs of a given directory, with their field `labels` populated."""

from pathlib import Path
from typing import Callable, Iterator, List, Set

import regex  # type: ignore

from .list_programs import iterate_and_print_programs, list_programs
from .parse_program import ProgramParser
from .user_types import Label, LabelName, Programs, Source


def labelled_programs(
    directory: Path,
    search_imported_program_name: Callable = regex.compile(r"import(?:_module)?:([^:]+)").search,
    **kwargs,
) -> Programs:
    """Walk a given directory, label all its programs, and return a list of them.

    Args:
        directory (Path): The directory to walk, containing some Python programs.
        search_imported_program_name (Callable, optional): A function taking a label name and, in
            the case it starts with `"import:"` or `"import_module:"`, returns a match object
            whose first group is the name of the imported program.
            [Not to be explicitly provided.](docs_developer_manual/index.html#default-argument-trick)
        **kwargs: May include the keyword arguments `cleanup_strategy`, `skip_pattern`,
            `glob_pattern`, transmitted to `paroxython.list_programs.list_programs`.
    Note:
        In addition to creating a list of programs with a populated `labels` field, tweak all of
        those which mark an importation of an “internal” module, _i.e_, a program belonging to
        this very list. For instance, a label `"import:my_program"` would be transformed into
        `"import_internally:my_program"`, while `"import:itertools"` would be left untouched.
    """
    programs: Programs = list_programs(directory, **kwargs)
    internal_program_names = {p.name for p in programs}
    parse = ProgramParser()
    print(f"Labelling {len(programs)} programs.")
    for program in iterate_and_print_programs(programs):
        program.labels[:] = parse(program)  # populate this field in place with [:]
        for (i, label) in enumerate(program.labels):
            m = search_imported_program_name(label.name)
            if m and f"{m[1]}.py" in internal_program_names:
                tweaked_label_name = LabelName(label.name.replace(":", "_internally:", 1))
                program.labels[i] = Label(name=tweaked_label_name, spans=label.spans)
    return programs


def generate_labelled_sources(programs: Programs) -> Iterator:
    """For each program, yield its source with its labels in comment.

    Args:
        programs (Programs): A list of labelled programs.

    Yields:
        Iterator: The lines of the given programs, with their labels in comment.

    Note:
        This function is for testing purposes only. See an example of the result in
        [labelled_sources.py](https://repo/examples/mini/labelled_sources.py).
    """
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
    programs = labelled_programs(Path("docs/resources"))
    for result in generate_labelled_sources(programs):
        print(result)
