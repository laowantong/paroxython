import pytest

import context
from helpers import suggest_regex

import regex

sources = r"""
<<< Abstract first longest prefix and one line number
/body/0/_type='For'
/body/0/lineno=1
/body/0/iter/_type='Call'
/body/0/iter/func/id='range'
/body/0/iter/args/length=1
/body/0/iter/args/0/_type='Call'
/body/0/iter/args/0/func/id='len'
/body/0/iter/keywords/length=0
---
          ^(.*?)/_type='For'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/iter/_type='Call'
\n(?:\1.+\n)*?\1/iter/func/id='range'
\n(?:\1.+\n)*?\1/iter/args/length=1
\n(?:\1.+\n)*?\1/iter/args/0/_type='Call'
\n(?:\1.+\n)*?\1/iter/args/0/func/id='len'
\n(?:\1.+\n)*?\1/iter/keywords/length=0
>>>
"""
source_rex = regex.compile(r"(?ms)^<<< ([^\n]+)\n(.+?\n)---\n(.+?\n)>>>")
examples = [m for m in source_rex.findall(sources)]  # [-1:]
suggestion = suggest_regex.Suggestion()


@pytest.mark.parametrize("title, original, expected", examples)
def test_strip_docs(title, original, expected):
    print(title)
    result = suggestion(original)
    print(result)
    assert result == expected


# pytest.main(args=["-q"])
