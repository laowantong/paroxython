"""Successive conditions.

Execute _f1 if condition _c1 is true, or else _f2 if condition _c2 is true, or else _f3 if condition _c3 is true.
Don't evaluate a condition when a previous condition was true.

Source: programming-idioms.org
"""

# Implementation author: cpoulet_42
# Created on 2017-08-09T08:48:05.281879Z
# Last modified on 2017-08-09T22:28:27.724165Z
# Version 2

f1 if c1 else f2 if c2 else f3 if c3 else None
