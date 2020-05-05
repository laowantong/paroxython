"""Number of bytes of a type.

Set _n to the number of bytes of a variable _t (of type _T).

Source: programming-idioms.org
"""

# Implementation author: bukzor
# Created on 2018-04-08T19:02:43.323249Z
# Last modified on 2018-04-08T19:02:43.323249Z
# Version 1

# `pip install pympler` to get this third-party library. `sys.getsizeof` is built-in, but has many common failure modes.

import pympler.asizeof

n = pympler.asizeof.asizeof(t)
