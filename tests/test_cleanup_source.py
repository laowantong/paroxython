import pytest
import regex  # type: ignore
from pathlib import Path

import context
from paroxython.preprocess_source import Cleanup

# This test suite is automatically injected into the docstring of `preprocess_source.py`.

sources = r'''
<<< Empty or blank lines are suppressed.
foo = bar


bar = buzz

---
foo = bar
bar = buzz
>>>

<<< Normal inline comments are suppressed.
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

<<< Commented lines are suppressed.
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

<<< Shebang is suppressed.
#!/usr/bin/env python
foobar()
---
foobar()
>>>

<<< Encoding declaration is suppressed.
# coding=utf8
foobar()
---
foobar()
>>>

<<< Docstrings of classes and functions are suppressed.
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

<<< Docstrings of modules are suppressed.
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

<<< A `pass` statement is added to empty classes if needed.
class Foo:
    """Lorem.

    Ipsum dolor.
    """
---
class Foo:
    pass
>>>

<<< Useless `pass` statements are suppressed.
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
>>>

<<< Mixes of comments and docstrings are suppressed.
# Lorem
# Ipsum
"""Dolor."""
foobar()
---
foobar()
>>>

<<< Paroxython's label hints are **preserved** and **normalized**.
foo = bar #   Paroxython   :   hint_1   hint_2
#paroxython: hint_3
fizz = [
    "foo", # lorem
    "bar", # paroxython: hint_4
]
---
foo = bar # paroxython: hint_1   hint_2
# paroxython: hint_3
fizz = [
    "foo",
    "bar", # paroxython: hint_4
]
>>>

<<< `if __name__ == "__main__":` part is suppressed.
foo = bar
if __name__ == "__main__":
    bar = foo
---
foo = bar
>>>

<<< `sys.path` injections are suppressed.
__import__("sys").path[0:0] = ["programs"]
(28433 * 2**7830457 + 1) % 10**10
---
(28433 * 2**7830457 + 1) % 10**10
>>>
'''

source_rex = regex.compile(r"(?ms)^<<< ([^\n]+)\n(.+?)\n---\n(.+?)\n>>>")
examples = [m for m in source_rex.findall(sources)]
cleanup = Cleanup("full").run


@pytest.mark.parametrize("title, original, expected", examples)
def test_full_cleaning(title, original, expected):
    print(title)
    result = cleanup(original)
    print(result)
    assert result == expected


def test_update_docstring():
    indent = "\n            "
    result = []
    for (title, original, expected) in examples:
        original = original.replace("\n", indent)
        expected = expected.replace("\n", indent)
        result.append(f"- {title}")
        result.append(fr"```python{indent}{original}{indent}```")
        result.append(fr"```python{indent}{expected}{indent}```")
    result = regex.sub(f"(?m){indent}$", "\n", indent.join(result))
    path = Path("paroxython/preprocess_source.py")
    source = path.read_text()
    (source, n) = regex.subn(
        r"(?sm)^(\s*def full_cleaning.+?Examples:\n).+?^\n(?= +All examples)",
        fr"\1            {result}\n\n",
        source,
    )
    assert n == 1
    path.write_text(source)


if __name__ == "__main__":
    pytest.main(["-qq", __import__("sys").argv[0]])
