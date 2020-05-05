"""Remove string trailing path separator.

Remove last character from string _p, if this character is the file path separator of current platform.

Note that this also transforms unix root path "/" into empty string!

Source: programming-idioms.org
"""

# Implementation author: Oldboy
# Created on 2017-10-28T13:33:02.066456Z
# Last modified on 2017-10-28T13:33:02.066456Z
# Version 1

import os

if p.endswith(os.sep):
    p = p[:-1]
