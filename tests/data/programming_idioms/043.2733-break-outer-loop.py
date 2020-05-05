"""Break outer loop.

Look for a negative value _v in 2D integer matrix _m. Print it and stop searching. 

Source: programming-idioms.org
"""

# Implementation author: Rochelimit
# Created on 2019-09-26T14:22:03.939368Z
# Last modified on 2019-09-27T03:20:25.894658Z
# Version 2

# Rather than set break flags, it is better to refactor into a function, then use return to break from all nested loops.


def loop_breaking(m, v):
    for i, row in enumerate(m):
        for j, value in enumerate(row):
            if value == v:
                return (i, j)
    return None


print(loop_breaking(([1, 2, 3], [4, 5, 6], [7, 8, 9]), 6))
