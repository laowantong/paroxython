"""Parallelize execution of 1000 independent tasks.

Launch the concurrent execution of procedure _f with parameter _i from 1 to 1000.
Tasks are independent and _f(_i) doesn't return any value.
Tasks need not run all at the same time, so you may use a pool.

Source: programming-idioms.org
"""

# Implementation author: programming-idioms.org
# Created on 2016-02-18T16:57:58.435578Z
# Last modified on 2016-02-18T16:57:58.435578Z
# Version 1

from multiprocessing import Pool

pool = Pool()
for i in range(1, 1001):
    pool.apply_async(f, [i])
