"""Check if any value in a list is larger than a limit.

Given a one-dimensional array _a, check if any value is larger than _x, and execute the procedure f if that is the case

Source: tkoenig
"""

# Implementation author: Grismar
# Created on 2019-09-28T02:31:20.114991Z
# Last modified on 2019-09-28T02:31:52.368863Z
# Version 2

if any(v > x for v in a):
    f()
