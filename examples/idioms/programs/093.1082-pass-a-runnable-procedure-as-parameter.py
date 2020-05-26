"""Pass a runnable procedure as parameter.

Implement procedure _control which receives one parameter _f, and runs _f.

Source: programming-idioms.org
"""

# Implementation author: nickname
# Created on 2016-02-18T16:58:02.348116Z
# Last modified on 2016-02-18T16:58:02.348116Z
# Version 1

from __future__ import print_function


def control(f):
    return f()
