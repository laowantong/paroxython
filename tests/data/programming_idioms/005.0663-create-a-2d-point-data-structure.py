"""Create a 2D Point data structure.

Declare a container type for two floating-point numbers _x and _y

Source: programming-idioms.org
"""

# Implementation author: cym13
# Created on 2016-02-18T16:57:55.615021Z
# Last modified on 2019-09-26T14:09:14.093527Z
# Version 2

from dataclasses import dataclass


@dataclass
class Point:
    x: float
    y: float
