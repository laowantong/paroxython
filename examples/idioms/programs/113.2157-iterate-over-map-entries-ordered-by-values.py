"""Iterate over map entries, ordered by values.

Print each key _k with its value _x from an associative array _mymap, in ascending order of _x.
Note that multiple entries may exist for the same value _x.

Source: programming-idioms.org
"""

# Implementation author: Oldboy
# Created on 2017-10-28T12:30:49.249241Z
# Last modified on 2017-10-28T12:30:49.249241Z
# Version 1

for x, k in sorted((x, k) for k, x in mymap.items()):
    print(k, x)
