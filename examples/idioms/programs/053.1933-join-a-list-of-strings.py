"""Join a list of strings.

Concatenate elements of string list _x joined by the separator ", " to create a single string _y.

Source: programming-idioms.org
"""

# Implementation author: programming-idioms.org
# Created on 2016-12-22T09:26:47.916166Z
# Last modified on 2019-05-12T19:56:56.476487Z
# Version 2

# This works even if some elements in _x are not strings.

y = ", ".join(map(str, x))
