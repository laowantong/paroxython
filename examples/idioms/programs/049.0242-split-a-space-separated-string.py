"""Split a space-separated string.

Build list _chunks consisting in substrings of input string _s, separated by one or more space characters.

Source: programming-idioms.org
"""

# Implementation author: programming-idioms.org
# Created on 2016-02-18T16:57:59.856562Z
# Last modified on 2016-05-29T09:25:03.631065Z
# Version 2

# If sep is not specified or is None, a different splitting algorithm is applied: runs of consecutive ASCII whitespace are regarded as a single separator, and the result will contain no empty strings at the start or end if the sequence has leading or trailing whitespace. Consequently, splitting an empty sequence or a sequence consisting solely of ASCII whitespace without a specified separator returns [].

chunks = s.split()
