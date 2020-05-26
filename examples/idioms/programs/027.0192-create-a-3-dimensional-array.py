"""Create a 3-dimensional array.

Declare and initialize a 3D array _x, having dimensions boundaries _m, _n, _p, and containing real numbers.

Source: programming-idioms.org
"""

# Implementation author: programming-idioms.org
# Created on 2015-11-30T12:37:27.593658Z
# Last modified on 2015-11-30T12:37:27.593658Z
# Version 1

x = [[[0 for k in xrange(p)] for j in xrange(n)] for i in xrange(m)]
