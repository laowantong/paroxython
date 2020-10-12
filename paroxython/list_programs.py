"""Scan a directory for Python programs and yield the corresponding `Program` objects."""

from pathlib import Path
from typing import Iterator

import regex  # type: ignore

from .preprocess_source import Cleanup, centrifugate_hints, collect_hints, remove_hints
from .user_types import Program, ProgramPath, Programs, Source


def list_programs(
    directory: Path,
    cleanup_strategy: str = "full",
    glob_pattern: str = "",
    skip_pattern: str = "",
    **kwargs,
) -> Programs:
    """List (by default recursively) all Python programs of a given directory.

    Args:
        directory (Path): The directory to search.
        cleanup_strategy (str, optional): Describes how to clean the source codes. Passed to
            `paroxython.preprocess_source.Cleanup`. Defaults to `"full"`.
        glob_pattern (str, optional): Describes which files to yield in `directory`. Passed to the
            standard library `pathlib`'s
            [`Path.glob()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.glob).
            If empty, replaced by `"**/*.py"`, which means “all Python source files in `directory`
            and all its subdirectories, recursively”. Defaults to `""`.
        skip_pattern (str, optional): Describes how to filter out the yielded files. If empty,
            skip any file whose name is `"__init__.py"`, `"setup.py"` or ends with `"-test.py"`,
            `"-tests.py"`, `"_test.py"` or `"_tests.py"`. Defaults to `""`.
        **kwargs: Ignored keyword arguments.

    Returns:
        Programs: A list of `Program` objects as constructed by `get_program`.
    """
    result: Programs = []
    cleanup = Cleanup(cleanup_strategy)
    glob_pattern = glob_pattern or "**/*.py"
    skip_pattern = skip_pattern or r"(__init__|setup|.*[-_]tests?)\.py"
    match_excluded = regex.compile(skip_pattern).fullmatch
    for path in sorted(directory.glob(glob_pattern)):
        if not match_excluded(path.name):
            source = cleanup.run(Source(path.read_text()))
            relative_path = path.relative_to(directory)
            result.append(get_program(source, relative_path))
    return result


def get_program(source: Source, relative_path: Path = None) -> Program:
    """Construct a fresh `Program` object from its source code and (optionally) relative path.

    Description:
        At this stage, the source code is already preprocessed by `paroxython.preprocess_source`,
        which among other things means it has been stripped from all its comments, except those
        consisting of one or several manual hints. The following operations are then carried out:

        1. Centrifugate the all-encompassing hints found in the source code (see
            `paroxython.preprocess_source.centrifugate_hints`).
        2. Collect all hints, determining whether they must be added to or removed from the
            labels which will later be found by `paroxython.label_programs.labelled_programs`.
        3. Remove all hints from the source code.
        4. Return a new `Program` (details below).

    Args:
        source (Source): A source code, already preprocessed.
        relative_path (Path, optional): A path relative to the directory passed to
            `list_programs()`. Can be omitted for testing purposes or when the source code is
            the contents of a Jupyter Notebook's cell. Defaults to None.

    Returns:
        Program: A `NamedTuple` consisting in the following fields:
        - `path` (type `ProgramPath`, derived from `str`): the program path, either empty or
            relative to the directory passed to `list_programs()`;
        - `source` (type `Source`, derived from `str`): its code source, fully cleaned up;
        - `addition` (type `Dict[LabelName, List[Span]]`): the manual hints scheduled for addition;
        - `deletion` (type `Dict[LabelName, List[Span]]`): the manual hints scheduled for deletion;
        - `labels` (type `List[Label]`, where each `Label` consists in a label name and a list of
            spans). This list is created empty here, to be later populated by
            `paroxython.label_programs.labelled_programs`.
        - `taxa` (type `List[Taxa]`, where each `Taxon` consists in a taxon name and a bag of
            spans). This list is created empty here, to be later calculated from the labels by
            `paroxython.map_taxonomy.Taxonomy`.
    """
    source = centrifugate_hints(source)
    (addition, deletion) = collect_hints(source)
    source = remove_hints(source)
    return Program(
        path=ProgramPath(str(relative_path or Path())),
        source=source,
        addition=addition,
        deletion=deletion,
        labels=[],
        taxa=[],
    )


def iterate_and_print_programs(programs: Programs) -> Iterator[Program]:
    """Iterate on a list of programs while printing their names as a side effect.

    Args:
        programs (Programs): A list of `Program` objects, as returned by `list_programs`.

    Yields:
        Iterator[Program]: The same `Program` objects in the same order.

    Note:
        This simple wrapper should print the name of each program over the previous one to avoid
        flooding the screen. Unfortunately, this may result in even more flood if your console
        does not support [ANSI escape codes](https://en.wikipedia.org/wiki/ANSI_escape_code).
    """
    blanks = ""
    for (i, program) in enumerate(programs, 1):
        print(end=f"\r{blanks}\r{i: 5} {program.path}", flush=True)
        blanks = " " * (len(program.path) + 7)
        if i == len(programs):  # Placed after the loop, the next line would not be executed.
            print(end=f"\r{blanks}\r", flush=True)
        yield program


if __name__ == "__main__":
    datetime = __import__("datetime").datetime
    directory = Path("../Algo/programs/")
    for program in list_programs(
        directory,
        skip_pattern=r"^(__init__|setup|.*[-_]tests?|quiz_.*)\.py$",
        cleanup_strategy="full",
    ):
        path = directory / program.path
        print(datetime.fromtimestamp(path.stat().st_mtime))
        print(program.source)
        print("-" * 80)
