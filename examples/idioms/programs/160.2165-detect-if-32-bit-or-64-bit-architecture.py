"""Detect if 32-bit or 64-bit architecture.

Execute _f32() if platform is 32-bit, or _f64() if platform is 64-bit.
This can be either a compile-time condition (depending on target) or a runtime detection.

Source: programming-idioms.org
"""

# Implementation author: Oldboy
# Created on 2017-10-28T13:28:42.005738Z
# Last modified on 2017-10-28T13:28:42.005738Z
# Version 1

# runtime check

import sys

if sys.maxsize > 2 ** 32:
    f64()
else:
    f32()
