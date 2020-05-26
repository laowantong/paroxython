"""Sort by a property.

Sort elements of array-like collection _items in ascending order of _x._p, where _p is a field of the type _Item of the objects in _items.

Source: programming-idioms.org
"""

# Implementation author: Roboticus
# Created on 2015-11-30T12:37:27.658885Z
# Last modified on 2015-11-30T12:37:27.658885Z
# Version 1

# The lambda expression pulls out the field you want to sort by.  If you want to sort in reverse order, add reverse=True to the argument list.

items = sorted(items, key=lambda x: x.p)
