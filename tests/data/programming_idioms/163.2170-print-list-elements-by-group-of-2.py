"""Print list elements by group of 2.

Print all the _list elements, two by two, assuming _list length is even.

Source: Bzzzzzzzzzz
"""

# Implementation author: Oldboy
# Created on 2017-10-28T14:00:36.671699Z
# Last modified on 2017-11-18T23:17:29.372798Z
# Version 2

# original list is called _list

for x in zip(list[::2], list[1::2]):
    print(x)
