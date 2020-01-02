import pytest
import regex  # type: ignore

import context
from paroxython.cleanup_source import cleanup_factory

sources = r'''
<<< inline comments
foo = bar # lorem ipsum
fizz = [
    "foo", # lorem
    "bar", # ipsum
]
---
foo = bar
fizz = [
    "foo",
    "bar",
]
>>>

<<< commented lines
# lorem ipsum
# dolor amet
def foo(bar):
    # lorem
    # ipsum
    if foo == bar:
        # lorem
        return []
    # lorem
# ipsum
---
def foo(bar):
    if foo == bar:
        return []
>>>

<<< shebang
#!/usr/bin/env python
foobar()
---
foobar()
>>>

<<< encoding
# coding=utf8
foobar()
---
foobar()
>>>

<<< function and class docstrings
class Foo:
    """Lorem.

    Ipsum dolor.
    """
    def foo(self, bar):
        """Lorem ipsum."""
        return 1
def bar():
    """Ipsum dolor"""
    return 2
---
class Foo:
    def foo(self, bar):
        return 1
def bar():
    return 2
>>>

<<< module docstrings
"""Lorem.

Ipsum Dolor."""

"""Lorem ipsum dolor sic amet."""

a = """consectetur
adipiscing
elit.
"""
---
a = """consectetur
adipiscing
elit.
"""
>>>

<<< empty class
class Foo:
    """Lorem.

    Ipsum dolor.
    """
---
class Foo:
    pass
>>>

<<< pass statements
foo()
pass
if bar():
    pass
else:
    pass
    foobar()
    pass
---
foo()
if bar():
    pass
else:
    foobar()
    pass
>>> BUG: useless pass statements are kept when they are not followed
         by a line with a same indentation level.

<<< Comment followed by a docstring
# Lorem
# Ipsum
"""Dolor."""
foobar()
---
foobar()
>>>

<<< paroxython label hints
foo = bar # paroxython: hint_1 hint_2
# paroxython: hint_3
fizz = [
    "foo", # lorem
    "bar", # paroxython: hint_4
]
---
foo = bar # paroxython: hint_1 hint_2
# paroxython: hint_3
fizz = [
    "foo",
    "bar", # paroxython: hint_4
]
>>>
'''
source_rex = regex.compile(r"(?ms)^<<< ([^\n]+)\n(.+?)\n---\n(.+?)\n>>>")
examples = [m for m in source_rex.findall(sources)]
cleanup = cleanup_factory("strip_docs")


@pytest.mark.parametrize("title, original, expected", examples)
def test_strip_docs(title, original, expected):
    print(title)
    result = cleanup(original)
    print(result)
    assert result == expected
