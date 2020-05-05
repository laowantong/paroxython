"""Continue outer loop.

Print each item _v of list _a which in not contained in list _b.
For this, write an outer loop to iterate on _a and an inner loop to iterate on _b.

Source: programming-idioms.org
"""

# Implementation author: cym13
# Created on 2016-02-18T16:57:59.339267Z
# Last modified on 2016-02-18T16:57:59.339267Z
# Version 1

# Note that using two loops like this in python is by itself _very un-idiomatic. Also one would be wise to define a custom exception to avoid hiding "real" exceptions.

for v in a:
    try:
        for u in b:
            if v == u:
                raise Exception()
        print(v)
    except Exception:
        continue
