"""Halfway between two hex color codes.

Find color _c, the average between colors _c1, _c2.

_c, _c1, _c2 are strings of hex color codes: 7 chars, beginning with a number sign # .
Assume linear computations, ignore gamma corrections.

Source: programming-idioms.org
"""

# Implementation author: Oldboy
# Created on 2017-10-28T12:06:58.817755Z
# Last modified on 2017-10-28T12:06:58.817755Z
# Version 1

r1, g1, b1 = [int(c1[p : p + 2], 16) for p in range(1, 6, 2)]
r2, g2, b2 = [int(c2[p : p + 2], 16) for p in range(1, 6, 2)]
c = "#{:02x}{:02x}{:02x}".format((r1 + r2) // 2, (g1 + g2) // 2, (b1 + b2) // 2)
