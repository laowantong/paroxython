"""Print list elements by group of 2.

Print all the _list elements, two by two, assuming _list length is even.

Source: Bzzzzzzzzzz
"""

# Implementation author: sgdpk
# Created on 2019-09-27T04:00:54.357549Z
# Last modified on 2019-09-27T04:00:54.357549Z
# Version 1

# Official documentation suggestion. Works for any iterable

from itertools import tee


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


for a, b in pairwise(list):
    print(a, b)
