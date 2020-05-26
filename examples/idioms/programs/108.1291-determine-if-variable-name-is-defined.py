"""Determine if variable name is defined.

Print the value of variable _x, but only if _x has been declared in this program.
This makes sense in some languages, not all of them. (Null values are not the point, rather the very existence of the variable.)

Note that this is (almost?) always an anti pattern. If you think you need this, look into appropriate data structures like maps/hashes instead.

Source: programming-idioms.org
"""

# Implementation author: alfred.p.bankwartz
# Created on 2016-02-18T16:58:03.13025Z
# Last modified on 2016-02-18T16:58:03.13025Z
# Version 1

# variable name must be quoted.

if "x" in locals():
    print(x)
