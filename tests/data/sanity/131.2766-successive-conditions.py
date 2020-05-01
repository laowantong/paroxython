"""Successive conditions.

Execute _f1 if condition _c1 is true, or else _f2 if condition _c2 is true, or else _f3 if condition _c3 is true.
Don't evaluate a condition when a previous condition was true.

Source: programming-idioms.org
"""

# Implementation author: koltrast
# Created on 2019-09-26T14:49:24.58635Z
# Last modified on 2019-09-26T14:49:24.58635Z
# Version 1

if c1:
    f1()
elif c2:
    f2()
elif c3:
    f3()
