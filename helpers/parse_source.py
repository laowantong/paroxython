from pathlib import Path

import regex  # type: ignore

import context
from paroxython.goodies import couple_to_string
from paroxython.parse_program import ProgramParser
from paroxython.user_types import Program, Source

path = Path("sandbox/source.py")
source = path.read_text().strip()
if source.startswith("1   "):
    source = regex.sub(r"(?m)^.{1,4}", "", source)
for (i, line) in enumerate(source.split("\n"), 1):
    print(f"{i:<4}{line}")
program = Program(source=Source(source), labels=[], taxa=[], addition={}, deletion={})
print()
parse = ProgramParser()
acc = []
for (name, spans) in sorted(parse(program, yield_failed_matches=False)):
    spans_as_string = ", ".join(map(couple_to_string, spans))
    acc.append(f"| `{name}` | {spans_as_string} |")
    # acc[-1] += " %s |" % ", ".join(f"{span.path}" for span in spans)
print("\n".join(acc))
Path("sandbox/flat_ast.txt").write_text(parse.flat_ast)
