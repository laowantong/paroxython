"""Pick uniformly a random floating point number in [a..b[.

Pick a random number greater than or equals to _a, strictly inferior to _b. Precondition : _a < _b.

Source: programming-idioms.org
"""

# Implementation author: programming-idioms.org
# Created on 2016-02-18T16:57:57.104352Z
# Last modified on 2016-02-18T16:57:57.104352Z
# Version 1

import random


def pick(a, b):
    return random.randrange(a, b)
