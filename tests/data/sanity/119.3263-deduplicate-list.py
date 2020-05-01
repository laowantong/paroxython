"""Deduplicate list.

Remove duplicates from list _x.
Explain if original order is preserved.

Source: programming-idioms.org
"""

# Implementation author: Fazel94
# Created on 2019-09-27T14:12:17.335663Z
# Last modified on 2019-09-27T14:12:17.335663Z
# Version 1

# This snippet preserves the original order of the list
elements = ["b", "a", "b", "c"]
unique_set = set()
elements_unique = []
for i in elements:
    if i not in unique_set:
        unique_set.add(i)
        elements_unique.append(i)
print(elements_unique)  # outputs ["b", "a", "c"]
