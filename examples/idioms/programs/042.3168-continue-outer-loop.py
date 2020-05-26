"""Continue outer loop.

Print each item _v of list _a which in not contained in list _b.
For this, write an outer loop to iterate on _a and an inner loop to iterate on _b.

Source: programming-idioms.org
"""

# Implementation author: sgdpk
# Created on 2019-09-27T03:11:50.496862Z
# Last modified on 2019-09-27T03:13:07.422569Z
# Version 2

for v in a:
    for v_ in b:
        if v == v_:
            continue
        print(v)

# More idiomatic solution for this specific problem
#
# for v in a:
#     if v not in b:
#        print(v)
