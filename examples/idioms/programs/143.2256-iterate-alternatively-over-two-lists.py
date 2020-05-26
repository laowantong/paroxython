"""Iterate alternatively over two lists.

Iterate alternatively over the elements of the list _items1 and _items2. For each iteration, print the element.

Explain what happens if _items1 and _items2 have different size.

Source: BBaz
"""

# Implementation author: Xris
# Created on 2018-03-27T11:45:39.203775Z
# Last modified on 2018-03-27T11:56:30.155613Z
# Version 2

# This will print former min(len(item1), item(2)) pairs if len(item1) != len(item2).

for pair in zip(item1, item2):
    print(pair)
