"""Filter and transform list.

Produce a new list _y containing the result of function _T applied to all elements _e of list _x that match the predicate _P.

Source: beltiras
"""

# Implementation author: beltiras
# Created on 2019-09-27T11:23:50.196486Z
# Last modified on 2019-09-27T13:26:07.008541Z
# Version 3

y = [T(e) for e in x if P(e)]
