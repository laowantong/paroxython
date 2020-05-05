"""Pick uniformly a random integer in [a..b].

Pick a random integer greater than or equals to _a, inferior or equals to _b. Precondition : _a < _b.

Source: programming-idioms.org
"""

# Implementation author: programming-idioms.org
# Created on 2016-02-18T16:57:57.20109Z
# Last modified on 2016-02-18T16:57:57.20109Z
# Version 1

# Upper bound _b is included.

import random

random.randint(a, b)
