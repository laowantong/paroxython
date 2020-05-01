""" Remove all occurrences of a value from a list.

Remove all occurrences of value _x from list _items.
This will alter the original list or return a new list, depending on which is more idiomatic.

Source: programming-idioms.org
"""

# Implementation author: Oldboy
# Created on 2017-10-28T10:22:48.548691Z
# Last modified on 2017-10-28T10:22:48.548691Z
# Version 1

newlist = [item for item in items if item != x]
