"""Format decimal number.

From real value _x in [0,1], create its percentage string representation _s with one digit after decimal point. E.g. 0.15625 -> "15.6%"

Source: programming-idioms.org
"""

# Implementation author: nickname
# Created on 2016-02-18T16:58:00.875881Z
# Last modified on 2018-06-24T11:00:03.628976Z
# Version 2

# .1 means only one digit after decimal point.
# % handles the "multiplication" and shows the percentage sign.

s = "{:.1%}".format(x)
