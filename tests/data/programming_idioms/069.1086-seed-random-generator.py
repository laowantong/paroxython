"""Seed random generator.

Use seed _s to initialize a random generator.

If _s is constant, the generator output will be the same each time the program runs. If _s is based on the current value of the system clock, the generator output will be different each time.

Source: programming-idioms.org
"""

# Implementation author: nickname
# Created on 2016-02-18T16:58:01.100654Z
# Last modified on 2016-02-18T16:58:01.100654Z
# Version 1

# this creates a new random generator _rand

import random

rand = random.Random(s)
