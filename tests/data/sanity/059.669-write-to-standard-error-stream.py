"""Write to standard error stream.

Print the message "_x is negative" to standard error (stderr), with integer _x value substitution (e.g. "-2 is negative").

Source: programming-idioms.org
"""

# Implementation author: cym13
# Created on 2015-11-30T12:37:29.950568Z
# Last modified on 2015-11-30T12:37:29.950568Z
# Version 1

# Python2
#
# If possible, use the python3 with "from __future__ import print_function"

import sys

print >>sys.stderr, "%s is negative" % x
