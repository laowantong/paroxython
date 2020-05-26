"""Count bits set in integer binary representation.

Count number _c of 1s in the integer _i in base 2.

E.g. _i=6 → _c=2

Source: deleplace
"""

# Implementation author: Maxlynch
# Created on 2017-03-02T13:06:25.168698Z
# Last modified on 2017-03-03T11:50:05.929281Z
# Version 2

c = bin(i).count("1")
