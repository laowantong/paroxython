"""Atomically read and update variable.

Assign variable _x the new value _f(_x), making sure that no other thread may modify _x between the read and the write. 

Source: programming-idioms.org
"""

# Implementation author: TinyFawks
# Created on 2016-02-18T16:57:58.598676Z
# Last modified on 2016-02-18T16:57:58.598676Z
# Version 1

import threading

lock = threading.Lock()

lock.acquire()
try:
    x = f(x)
finally:
    lock.release()
