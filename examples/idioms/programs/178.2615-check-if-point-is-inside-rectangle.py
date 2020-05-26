"""Check if point is inside rectangle.

Set boolean _b to _true if if the point with coördinates (_x,_y) is inside the rectangle with coördinates (_x1,_y1,_x2,_y2) , or to _false otherwise.
Describe if the edges are considered to be inside the rectangle.

Source: Bart
"""

# Implementation author: Oldboy
# Created on 2019-02-11T20:04:55.444221Z
# Last modified on 2019-02-11T20:04:55.444221Z
# Version 1

# Edges NOT considered to be inside.

b = (x1 < x < x2) and (y1 < y < y2)
