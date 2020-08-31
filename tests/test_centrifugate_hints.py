import pytest
from pathlib import Path

import regex  # type: ignore

import context
from paroxython.preprocess_source import centrifugate_hints

# This test suite is automatically injected into the docstring of `preprocess_source.py`.

sources = r"""
<<< Some isolated hints (`hint_3` and `hint_5` are centrifugated).
foo = bar # paroxython: hint_1 hint_2
# paroxython: hint_3
fizz = [
    "foo",
    "bar", # paroxython: hint_4
    # paroxython: hint_5
]
---
foo = bar # paroxython: hint_1 hint_2 hint_3... hint_5...
fizz = [
    "foo",
    "bar", # paroxython: hint_4
] # paroxython: ...hint_3 ...hint_5
>>>

<<< Some trailing isolated hints (`hint_5` and `hint_6` are centrifugated).
foo = bar # paroxython: hint_1 hint_2
fizz = [
    "foo",
    "bar", # paroxython: hint_3
] # paroxython: hint_4
# paroxython: hint_5
# paroxython: hint_6
---
foo = bar # paroxython: hint_1 hint_2 hint_5... hint_6...
fizz = [
    "foo",
    "bar", # paroxython: hint_3
] # paroxython: hint_4 ...hint_5 ...hint_6
>>>

<<< No isolated hints (no centrifugation of the existing hints).
foo = bar # paroxython: hint_1 hint_2
fizz = [
    "foo",
    "bar", # paroxython: hint_4
]
---
foo = bar # paroxython: hint_1 hint_2
fizz = [
    "foo",
    "bar", # paroxython: hint_4
]
>>>
"""
source_rex = regex.compile(r"(?ms)^<<< ([^\n]+)\n(.+?)\n---\n(.+?)\n>>>")
examples = [m for m in source_rex.findall(sources)]


@pytest.mark.parametrize("title, original, expected", examples)
def test_centrifugate_hints(title, original, expected):
    print(title)
    result = centrifugate_hints(original)
    print(result)
    assert result == expected


def test_update_docstring():
    indent = "\n        "
    result = []
    for (title, original, expected) in examples:
        original = original.replace("\n", indent)
        expected = expected.replace("\n", indent)
        result.append(f"- {title}")
        result.append(fr"```python{indent}{original}{indent}```")
        result.append(fr"```python{indent}{expected}{indent}```")
    result = indent.join(result)
    path = Path("paroxython/preprocess_source.py")
    source = path.read_text()
    (source, n) = regex.subn(
        r"(?sm)^(def centrifugate_hints.+?Examples:\n).+?^ *\n",
        fr"\1        {result}\n\n",
        source,
    )
    assert n == 1
    path.write_text(source)


if __name__ == "__main__":
    pytest.main(["-qq", __import__("sys").argv[0]])
