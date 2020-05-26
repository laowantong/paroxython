"""Create a bitset.

Create an object _x to store _n bits (_n being potentially large).

Source: programming-idioms.org
"""

# Implementation author: bukzor
# Created on 2018-04-08T06:56:50.980819Z
# Last modified on 2018-04-08T20:04:06.987067Z
# Version 2

from __future__ import division
import math

x = bytearray(int(math.ceil(n / 8.0)))
