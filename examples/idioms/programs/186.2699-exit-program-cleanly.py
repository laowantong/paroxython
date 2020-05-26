"""Exit program cleanly.

Exit a program cleanly indicating no error to OS	

Source: jazz
"""

# Implementation author: random
# Created on 2019-09-26T13:49:49.970567Z
# Last modified on 2019-09-26T13:49:49.970567Z
# Version 1

# Since exit() ultimately “only” raises an exception, it will only exit the process when called from the main thread, and the exception is not intercepted.

import sys

sys.exit(0)
