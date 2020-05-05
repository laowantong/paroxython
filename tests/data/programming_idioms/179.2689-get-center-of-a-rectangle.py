"""Get center of a rectangle.

Return the center _c of the rectangle with coördinates(_x1,_y1,_x2,_y2)

Source: Bart
"""

# Implementation author: random
# Created on 2019-09-26T13:37:07.573535Z
# Last modified on 2019-09-26T13:37:07.573535Z
# Version 1

# center is a namedtuple, that can be accessed either using x and y or an index (0,1)
#
# e.g. center.x or center[0]

from collections import namedtuple

Point = namedtuple("Point", "x y")
center = Point((x1 + x2) / 2, (y1 + y2) / 2)
