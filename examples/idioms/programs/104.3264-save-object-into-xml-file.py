"""Save object into XML file.

Write content of object _x into file _data._xml. 

Source: programming-idioms.org
"""

# Implementation author: Fazel94
# Created on 2019-09-27T14:19:13.327701Z
# Last modified on 2019-09-27T14:19:13.327701Z
# Version 1

import pyxser as pyx

# Python 2.5 to 2.7
# Use pickle or marshall module
class TestClass(object):
    a = None
    b = None
    c = None

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


tst = TestClass("var_a", "var_b", "var_c")
ser = pyx.serialize(obj=tst, enc="utf-8")
print(ser)
