"""Return two values.

Implement a function _search which looks for item _x in a 2D matrix _m.
Return indices _i, _j of the matching cell.
Think of the most idiomatic way in the language to return the two values at the same time.

Source: programming-idioms.org
"""

# Implementation author: JackStouffer
# Created on 2015-11-30T12:37:26.87247Z
# Last modified on 2015-11-30T12:37:26.87247Z
# Version 1


def search(m, x):
    for idx, item in enumerate(m):
        if x in item:
            return idx, item.index(x)
