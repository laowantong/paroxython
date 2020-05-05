"""Compute LCM.

Compute the least common multiple _x of big integers _a and _b. Use an integer type able to handle huge numbers.

Source: deleplace
"""

# Implementation author: cym13
# Created on 2016-02-18T16:58:01.374503Z
# Last modified on 2016-02-18T16:58:01.374503Z
# Version 1

from fractions import gcd

x = (a * b) // gcd(a, b)
