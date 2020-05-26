"""Currying.

Transform a function that takes multiple arguments into a function for which some of the arguments are preset.

Source: Adrian
"""

# Implementation author: cym13
# Created on 2015-11-30T12:37:28.255934Z
# Last modified on 2019-09-26T16:59:21.413984Z
# Version 3

from functools import partial


def f(a):
    def add(b):
        return a + b

    return add


print(f(2)(1))

# add_to_two = partial(f, 2)
