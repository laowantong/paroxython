"""Iterate over map entries, ordered by keys.

Print each key _k with its value _x from an associative array _mymap, in ascending order of _k.

Source: programming-idioms.org
"""

# Implementation author: Oldboy
# Created on 2017-10-28T10:33:16.415371Z
# Last modified on 2019-09-26T16:13:29.479393Z
# Version 3

# dictionaries iterate over their keys by default

for k in sorted(mymap):
    print(mymap[k])
