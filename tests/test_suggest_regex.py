import pytest
import regex  # type: ignore

import context
from helpers.suggest_regex import Suggestion

sources = r"""
<<< Abstract first longest prefix and one line number
/body/0/_type='For'
/body/0/_pos=1
/body/0/iter/_type='Call'
/body/0/iter/func/id='range'
/body/0/iter/args/_length=1
/body/0/iter/args/0/_type='Call'
/body/0/iter/args/0/func/id='len'
/body/0/iter/keywords/_length=0
---
           ^(.*)/_type='For'
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/iter/_type='Call'
\n(?:\1.+\n)*?\1/iter/func/id='range'
\n(?:\1.+\n)*?\1/iter/args/_length=1
\n(?:\1.+\n)*?\1/iter/args/0/_type='Call'
\n(?:\1.+\n)*?\1/iter/args/0/func/id='len'
\n(?:\1.+\n)*?\1/iter/keywords/_length=0
>>>

<<< Capture and match a given value among ("name", "id", "_hash", "_ids")
/body/0/_type='Assign'
/body/0/_pos=1
/body/0/targets/0/_hash=0x5c36d5a0
/body/0/value/_type='UnaryOp'
/body/0/value/op/_type='USub'
/body/0/value/operand/_hash=0x5c36d5a0
---
           ^(.*)/_type='Assign'
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/targets/0/_hash=(?P<HASH>.+) # capture _hash
\n(?:\1.+\n)*?\1/value/_type='UnaryOp'
\n(?:\1.+\n)*?\1/value/op/_type='USub'
\n(?:\1.+\n)*?\1/value/operand/_hash=(?P=HASH) # match _hash
>>>

<<< Abstract bodies (one)
/body/0/_type='For'
/body/0/_pos=1
/body/0/iter/_hash=0x4a4b82fd
/body/0/body/0/_type='For'
/body/0/body/0/_pos=2
/body/0/body/0/iter/_hash=0x4a4b82fd
---
           ^(.*)/_type='For'
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/iter/_hash=(?P<HASH>.+) # capture _hash
\n(?:\1.+\n)* \1/(?P<_1>(?:body|orelse)/\d+)/_type='For'
\n(?:\1.+\n)*?\1/(?P=_1)                    /_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/(?P=_1)                    /iter/_hash=(?P=HASH) # match _hash
>>>

<<< Abstract bodies (several)
/body/0/_type='For'
/body/0/_pos=1
/body/0/target/id='element'
/body/0/body/1/_type='If'
/body/0/body/1/test/args/0/id='element'
/body/0/body/1/body/1/_pos=5
/body/0/body/1/body/1/value/_type='Call'
/body/0/body/1/body/1/value/func/attr='append'
/body/0/body/1/body/1/value/args/0/id='element'
---
           ^(.*)/_type='For'
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/target/id=(?P<ID>.+) # capture id
\n(?:\1.+\n)* \1/(?P<_1>(?:body|orelse)/\d+)/_type='If'
\n(?:\1.+\n)*?\1/(?P=_1)                    /test/args/0/id=(?P=ID) # match id
\n(?:\1.+\n)* \1/(?P=_1)                    /(?P<_2>(?:body|orelse)/\d+)/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/(?P=_1)                    /(?P=_2)                    /value/_type='Call'
\n(?:\1.+\n)*?\1/(?P=_1)                    /(?P=_2)                    /value/func/attr='append'
\n(?:\1.+\n)*?\1/(?P=_1)                    /(?P=_2)                    /value/args/0/id=(?P=ID) # match id
>>>

<<< Abstract bodies (sequence)
/body/0/body/0/_type='Assign'
/body/0/body/0/targets/0/id='candidate'
/body/0/body/1/_type='For'
/body/0/body/1/_pos=3
/body/0/body/1/target/id='element'
/body/0/body/1/body/0/_type='If'
/body/0/body/1/body/0/test/_ids='is_better''candidate''element'
/body/0/body/1/body/0/test/args/1/id='candidate'
/body/0/body/1/body/0/body/0/_type='Assign'
/body/0/body/1/body/0/body/0/_pos=5
/body/0/body/1/body/0/body/0/targets/0/id='candidate'
/body/0/body/1/body/0/body/0/value/id='element'
---
           ^(.*)/(?P<_1>(?:body|orelse)/\d+)/_type='Assign'
\n(?:\1.+\n)*?\1/(?P=_1)                    /targets/0/id=(?P<ID_1>.+) # capture id #1
\n(?:\1.+\n)* \1/(?P<_2>(?:body|orelse)/\d+)/_type='For'
\n(?:\1.+\n)*?\1/(?P=_2)                    /_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/(?P=_2)                    /target/id=(?P<ID_2>.+) # capture id #2
\n(?:\1.+\n)* \1/(?P=_2)                    /(?P<_3>(?:body|orelse)/\d+)/_type='If'
\n(?:\1.+\n)*?\1/(?P=_2)                    /(?P=_3)                    /test/_ids='is_better''candidate''element'
\n(?:\1.+\n)*?\1/(?P=_2)                    /(?P=_3)                    /test/args/1/id=(?P=ID_1) # match id #1
\n(?:\1.+\n)* \1/(?P=_2)                    /(?P=_3)                    /(?P<_4>(?:body|orelse)/\d+)/_type='Assign'
\n(?:\1.+\n)*?\1/(?P=_2)                    /(?P=_3)                    /(?P=_4)                    /_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/(?P=_2)                    /(?P=_3)                    /(?P=_4)                    /targets/0/id=(?P=ID_1) # match id #1
\n(?:\1.+\n)*?\1/(?P=_2)                    /(?P=_3)                    /(?P=_4)                    /value/id=(?P=ID_2) # match id #2
>>>
"""

source_rex = regex.compile(r"(?ms)^<<< ([^\n]+)\n(.+?\n)---\n(.+?\n)>>>")
examples = [m for m in source_rex.findall(sources)]  # [-1:]
suggestion = Suggestion()


@pytest.mark.parametrize("title, original, expected", examples)
def test_suggest_regex(title, original, expected):
    print(title)
    result = suggestion(original)
    print(result)
    assert result == expected


if __name__ == "__main__":
    pytest.main(["-qq", __import__("sys").argv[0]])
