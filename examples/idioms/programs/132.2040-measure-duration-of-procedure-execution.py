"""Measure duration of procedure execution.

Run procedure _f, and return the duration of the execution of _f.

Source: programming-idioms.org
"""

# Implementation author: Legron
# Created on 2017-07-10T14:58:55.028109Z
# Last modified on 2017-07-10T14:58:55.028109Z
# Version 1

# Setup makes the function _f accessible to timeit. Returned is the execution time in seconds

import timeit

duration = timeit.timeit("f()", setup="from __main__ import f")
