import regex
import sys
from pathlib import Path

sys.path[0:0] = [str(Path(__file__).parent)]

from parser import Parser

EXCLUDE_NAMES = {"__init__.py", "setup.py"}
SEPARATOR = "-" * 88

sub_docstrings = regex.compile(r'(?ms)^ *r?""".+?""" *\n').sub
sub_comment_lines = regex.compile(r"(?m)^ *#.*\n").sub
sub_main = regex.compile(r"""(?ms)^if __name__ *== *[\"']__main__[\"'] *:.+""").sub
sub_blank_lines = regex.compile(r"( *\n)( *\n)+").sub


def scan(path, sloc_only=True):
    parse = Parser()
    paths = sorted(path.rglob("*.py"))
    for path in paths:
        if path.name in EXCLUDE_NAMES:
            continue
        source = path.read_text()
        if sloc_only:
            source = sub_docstrings("", source)
            source = sub_comment_lines("", source)
            source = sub_main("", source)
            source = sub_blank_lines("\n", source.strip())
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
    from pathlib import Path

    for result in scan(Path("../Python/project_euler")):
        print(result)
