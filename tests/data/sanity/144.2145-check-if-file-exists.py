"""Check if file exists.

Set boolean _b to _true if file at path _fp exists on filesystem; _false otherwise.

Beware that you should never do this and then in the next instruction assume the result is still valid, this is a race condition on any multitasking OS.

Source: programming-idioms.org
"""

# Implementation author: Oldboy
# Created on 2017-10-28T10:44:48.697654Z
# Last modified on 2017-10-28T10:44:48.697654Z
# Version 1

import os

b = os.path.exists(fp)
