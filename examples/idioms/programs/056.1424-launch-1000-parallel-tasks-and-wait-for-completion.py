"""Launch 1000 parallel tasks and wait for completion.

Fork-join : launch the concurrent execution of procedure _f with parameter _i from 1 to 1000.
Tasks are independent and _f(_i) doesn't return any value.
Tasks need not run all at the same time, so you may use a pool.
Wait for the completion of the 1000 tasks and then print "Finished".

Source: deleplace
"""

# Implementation author: TinyFawks
# Created on 2016-02-18T16:58:00.323333Z
# Last modified on 2016-02-18T16:58:00.323333Z
# Version 1

from multiprocessing import Pool


def f(i):
    i * i


with Pool(processes) as p:
    p.map(func=f, iterable=range(1, 1001))

print("Finished")
