"""Create a factory.

Create a factory named _fact for any sub class of _Parent and taking exactly one string _str as constructor parameter.

Source: bbtemp
"""

# Implementation author: cym13
# Created on 2015-11-30T12:37:30.750423Z
# Last modified on 2017-05-12T12:10:42.285428Z
# Version 3

# You can use the class like a function.


def fact(a_class, str_):
    if issubclass(a_class, Parent):
        return a_class(str_)
