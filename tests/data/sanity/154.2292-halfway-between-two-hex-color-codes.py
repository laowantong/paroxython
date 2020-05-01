"""Halfway between two hex color codes.

Find color _c, the average between colors _c1, _c2.

_c, _c1, _c2 are strings of hex color codes: 7 chars, beginning with a number sign # .
Assume linear computations, ignore gamma corrections.

Source: programming-idioms.org
"""

# Implementation author: bukzor
# Created on 2018-04-14T05:28:36.956894Z
# Last modified on 2018-04-14T16:12:35.539002Z
# Version 2

# numpy is standard for array numerics, and works nicely for this problem. We can  represent a RGB value as a special numpy array.

import numpy


class RGB(numpy.ndarray):
    @classmethod
    def from_str(cls, rgbstr):
        return numpy.array(
            [int(rgbstr[i : i + 2], 16) for i in range(1, len(rgbstr), 2)]
        ).view(cls)

    def __str__(self):
        self = self.astype(numpy.uint8)
        return "#" + "".join(format(n, "x") for n in self)


c1 = RGB.from_str("#a1b1c1")
print(c1)
c2 = RGB.from_str("#1A1B1C")
print(c2)

print((c1 + c2) / 2)
