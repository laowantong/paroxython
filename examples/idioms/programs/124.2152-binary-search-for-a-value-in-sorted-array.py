"""Binary search for a value in sorted array.

Write function _binarySearch which returns the index of an element having value _x in sorted array _a, or -1 if no such element.

Source: programming-idioms.org
"""

# Implementation author: Oldboy
# Created on 2017-10-28T11:30:06.348956Z
# Last modified on 2017-10-28T11:30:06.348956Z
# Version 1

import bisect


def binarySearch(a, x):
    i = bisect.bisect_left(a, x)
    return i if i != len(a) and a[i] == x else -1
