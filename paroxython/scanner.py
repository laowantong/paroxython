import regex
import sys
from pathlib import Path

sys.path[0:0] = [str(Path(__file__).parent)]

from parser import Parser
from minimizer import minimize

SEPARATOR = "-" * 88

match_exclude_file = regex.compile(r"__init__\.py|setup\.py|.*[-_]tests?\.py").match
sub_main = regex.compile(r"""(?ms)^if __name__ *== *[\"']__main__[\"'] *:.+""").sub


def scan(path, sloc_only=True):
    parse = Parser()
    paths = sorted(path.rglob("*.py"))
    for path in paths:
        if match_exclude_file(path.name):
            continue
        source = path.read_text()
        if sloc_only:
            source = minimize(source)
            source = sub_main("", source)
        yield f"# {SEPARATOR}\n# {path}\n# {SEPARATOR}"
        print(path)
        sloc = source.splitlines()
        comments = [[] for _ in sloc]
        for (label, lines) in sorted(parse(source)):
            for line in set(lines):
                (start, suffix) = line.partition("-")[::2]
                start = int(start)
                if suffix:
                    suffix = f" (-> +{int(suffix) - start})"
                comments[start - 1].append(f"{label}{suffix}")
        for (i, comment) in enumerate(comments):
            if comment:
                sloc[i] += " # " + ", ".join(comment)
        sloc.append("")
        yield "\n".join(sloc)


if __name__ == "__main__":
    Path = __import__("pathlib").Path
    for result in scan(Path("../Python/project_euler")):
        print(result)
