"""Matrix multiplication.

Perform matrix multiplication of a real matrix _a with _nx rows and _ny columns, a real matrix _b with _ny rows and _nz columns and assign the value to a real matrix _c with _nx rows and _nz columns.

Source: tkoenig
"""

# Implementation author: programming-idioms.org
# Created on 2019-09-27T16:40:03.906529Z
# Last modified on 2019-09-27T16:40:03.906529Z
# Version 1

# You can also use _np._matrix instead of _np._array. Be careful when using _array, because the * operator performs elementwise multiplication.

import numpy as np

c = np.matmul(a, b)
