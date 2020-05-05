"""Random sublist.

Create a new list _y from randomly picking exactly _k elements from list _x.

It is assumed that _x has at least _k elements. 
Each element must have same probability to be picked. 
Each element from _x must be picked _at _most _once.
Explain if the original ordering is preserved or not.

Source: programming-idioms.org
"""

# Implementation author: Oldboy
# Created on 2017-10-28T13:10:20.094421Z
# Last modified on 2018-06-24T13:08:32.325774Z
# Version 2

# The original ordering is not preserved.

import random

y = random.sample(x, k)
