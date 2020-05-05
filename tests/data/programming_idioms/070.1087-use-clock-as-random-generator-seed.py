"""Use clock as random generator seed.

Get the current datetime and provide it as a seed to a random generator. The generator sequence will be different at each run.

Source: deleplace
"""

# Implementation author: nickname
# Created on 2016-02-18T16:58:01.15413Z
# Last modified on 2016-02-18T16:58:01.15413Z
# Version 1

# the constructor uses the current time if used without arguments.
# you could also use the functions of the random module (they are using a shared ``Random`` object which is constructed the first time random is imported

import random

rand = random.Random()
