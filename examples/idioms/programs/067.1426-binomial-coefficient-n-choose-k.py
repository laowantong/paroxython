"""Binomial coefficient "n choose k".

Calculate _binom(_n, _k) = _n! / (_k! * (_n-_k)!). Use an integer type able to handle huge numbers.

Source: programming-idioms.org
"""

# Implementation author: TinyFawks
# Created on 2016-02-18T16:58:01.001157Z
# Last modified on 2019-06-13T17:13:14.289424Z
# Version 4

import math


def binom(n, k):
    return math.factorial(n) // math.factorial(k) // math.factorial(n - k)
