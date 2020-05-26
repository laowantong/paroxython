"""Break outer loop.

Look for a negative value _v in 2D integer matrix _m. Print it and stop searching. 

Source: programming-idioms.org
"""

# Implementation author: cym13
# Created on 2016-02-18T16:57:59.387368Z
# Last modified on 2016-02-18T16:57:59.387368Z
# Version 1

# This is ugly because the pythonic way to solve this problem would be to refactor so that one doesn't have to break out of multiple loops. See PEP3136


class BreakOuterLoop(Exception):
    pass


try:
    position = None
    for row in m:
        for column in m[row]:
            if m[row][column] == v:
                position = (row, column)
                raise BreakOuterLoop
except BreakOuterLoop:
    pass
