"""Test deep equality.

Set boolean _b to true if objects _x and _y contain the same values, recursively comparing all referenced elements in _x and _y.
Tell if the code correctly handles recursive types.

Source: programming-idioms.org
"""

# Implementation author: bukzor
# Created on 2018-04-08T07:01:32.293233Z
# Last modified on 2018-04-08T20:07:29.581057Z
# Version 2

# The classes of _x and _y need to delegate to any contained objects' __eq__ implementation.
# All objects in the standard library do so.

b = x == y
