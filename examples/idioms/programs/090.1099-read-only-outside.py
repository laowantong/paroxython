"""Read-only outside.

Expose a read-only integer _x to the outside world while being writable inside a structure or a class _Foo.

Source: bbtemp
"""

# Implementation author: nickname
# Created on 2016-02-18T16:58:02.219893Z
# Last modified on 2016-02-18T16:58:02.219893Z
# Version 1


class Foo(object):
    def __init__(self):
        self._x = 0

    @property
    def x(self):
        """
        Doc for x
        """
        return self._x
