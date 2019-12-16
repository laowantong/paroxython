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
           ^(.*)/_type='For'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/iter/_type='Call'
\n(?:\1.+\n)*?\1/iter/func/id='range'
\n(?:\1.+\n)*?\1/iter/args/length=1
\n(?:\1.+\n)*?\1/iter/args/0/_type='Call'
\n(?:\1.+\n)*?\1/iter/args/0/func/id='len'
\n(?:\1.+\n)*?\1/iter/keywords/length=0
>>>

<<< Capture and match a given value among ("name", "id", "_hash", "_ids")
/body/0/_type='Assign'
/body/0/lineno=1
/body/0/targets/0/_hash=0x5c36d5a0
/body/0/value/_type='UnaryOp'
/body/0/value/op/_type='USub'
/body/0/value/operand/_hash=0x5c36d5a0
---
           ^(.*)/_type='Assign'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/targets/0/_hash=(?P<HASH>.+) # capture _hash
\n(?:\1.+\n)*?\1/value/_type='UnaryOp'
\n(?:\1.+\n)*?\1/value/op/_type='USub'
\n(?:\1.+\n)*?\1/value/operand/_hash=(?P=HASH) # match _hash
>>>

<<< Abstract bodies
/body/0/_type='For'
/body/0/lineno=1
/body/0/iter/_hash=0x4a4b82fd
/body/0/body/0/_type='For'
/body/0/body/0/lineno=2
/body/0/body/0/iter/_hash=0x4a4b82fd
---
           ^(.*)/_type='For'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/iter/_hash=(?P<HASH>.+) # capture _hash
\n(?:\1.+\n)* \1/(?P<_1>body/\d+)/_type='For'
\n(?:\1.+\n)*?\1/(?P=_1)         /lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/(?P=_1)         /iter/_hash=(?P=HASH) # match _hash
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
