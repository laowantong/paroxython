"""Filter list.

Create list _y containing items from list _x satisfying predicate _p. Respect original ordering. Don't modify _x in-place.

Source: programming-idioms.org
"""

# Implementation author: alexis
# Created on 2015-11-30T12:37:29.796657Z
# Last modified on 2019-09-27T03:31:27.393465Z
# Version 2

# In Python 3, returns filter object, not a list, following a lazy evaluation approach.

y = filter(p, x)
