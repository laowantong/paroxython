from pathlib import Path
import regex

match_excluded = regex.compile(r"__init__\.py|setup\.py|.*[-_]tests?\.py").match


def generate_programs(directory, cleanup_strategy="minimize"):

    if cleanup_strategy == "minimize":
        minimize = __import__("minimizer").minimize
        main = regex.compile(r"(?ms)^if +__name__ *== *.__main__. *:.+").sub
        decorator = regex.compile(r"(?m)^\s*@.+\n").sub
        cleanup = lambda source: decorator("", main("", minimize(source)))
    else:
        cleanup = lambda source: source

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

