"""Matrix multiplication.

Perform matrix multiplication of a real matrix _a with _nx rows and _ny columns, a real matrix _b with _ny rows and _nz columns and assign the value to a real matrix _c with _nx rows and _nz columns.

Source: tkoenig
"""

# Implementation author: joshvm
# Created on 2019-09-27T03:20:12.88986Z
# Last modified on 2019-09-27T16:42:27.700845Z
# Version 4

# Python 3.5 (PEP465) introduced the @ operator for matrix multiplication.
# You can also use _np._matrix instead of _np._array. Be careful when using _array, because the * operator performs elementwise multiplication.

import numpy as np

c = a @ b
