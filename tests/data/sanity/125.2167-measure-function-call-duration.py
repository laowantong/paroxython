"""Measure function call duration.

measure the duration _t, in nano seconds, of a call to the function _foo. Print this duration.

Source: JPSII
"""

# Implementation author: Oldboy
# Created on 2017-10-28T13:42:06.259364Z
# Last modified on 2017-10-28T13:42:06.259364Z
# Version 1

# _t1 and _t2 are 64bit _float

import time

t1 = time.perf_counter()
foo()
t2 = time.perf_counter()
print("Seconds:", t2 - t1)
