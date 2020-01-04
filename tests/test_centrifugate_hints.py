import pytest

import regex  # type: ignore

import context
from paroxython.preprocess_source import centrifugate_hints

sources = r"""
<<< some isolated hints
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

<<< some trailing isolated hints
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

<<< no isolated hints
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
