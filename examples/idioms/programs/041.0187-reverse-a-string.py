"""Reverse a string.

Create string _t containing the same characters as string _s, in reverse order.
Original string _s must remain unaltered. Each character must be handled correctly regardless its number of bytes in memory.

Source: programming-idioms.org
"""

# Implementation author: programming-idioms.org
# Created on 2016-02-18T16:57:59.271208Z
# Last modified on 2018-01-03T23:44:30.749232Z
# Version 2

t = s.decode("utf8")[::-1].encode("utf8")
