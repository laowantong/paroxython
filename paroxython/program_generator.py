from pathlib import Path

import regex

from cleanup_source import cleanup_factory


match_excluded = regex.compile(r"__init__\.py|setup\.py|.*[-_]tests?\.py").match


def generate_programs(directory, cleanup_strategy="strip_docs"):
    """Yield the path and the cleaned up source of all programs in a given directory.

    Input: a string or a pathlib.Path representing the directory path.

    Output: couples of Python programs' `pathlib.Path`s and their contents.
    """

    cleanup = cleanup_factory(cleanup_strategy)
    directory = Path(directory)
    for path in sorted(directory.rglob("*.py")):
        if not match_excluded(path.name):
            print(path)
            yield (path, cleanup(path.read_text()))


if __name__ == "__main__":
    datetime = __import__("datetime").datetime
    for (path, source) in generate_programs("../Algo/programs/"):
        print(datetime.fromtimestamp(path.stat().st_mtime))
        print(source)
        print("-" * 80)
