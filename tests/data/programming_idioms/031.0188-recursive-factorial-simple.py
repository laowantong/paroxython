"""Recursive factorial (simple).

Create recursive function _f which returns the factorial of non-negative integer _i, calculated from _f(_i-1)

Source: programming-idioms.org
"""

# Implementation author: programming-idioms.org
# Created on 2015-11-30T12:37:27.869482Z
# Last modified on 2015-11-30T12:37:27.869482Z
# Version 1


def f(i):
    if i == 0:
        return 1
    else:
        return i * f(i - 1)
