"""Current executable name.

Assign to string _s the name of the currently executing program (but not its full path).

Source: programming-idioms.org
"""

# Implementation author: iLoveTux
# Created on 2016-08-24T02:50:46.124706Z
# Last modified on 2016-08-24T02:50:46.124706Z
# Version 1

# sys.argv[0] holds the name of the currently running script, you might use ___file__, but if called from within a module you would then get the module's ___file__ attribute.

import sys

s = sys.argv[0]
