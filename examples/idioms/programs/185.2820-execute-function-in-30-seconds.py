"""Execute function in 30 seconds.

Schedule the execution of _f(42) in 30 seconds.

Source: programming-idioms.org
"""

# Implementation author: Baxter
# Created on 2019-09-26T15:37:59.347514Z
# Last modified on 2019-09-27T07:54:09.096921Z
# Version 3

import threading

timer = threading.Timer(30.0, f, args=(42,))
timer.start()
