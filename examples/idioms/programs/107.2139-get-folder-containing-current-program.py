"""Get folder containing current program.

Assign to string _dir the path of the folder containing the currently running executable.
(This is not necessarily the working directory, though.)

Source: programming-idioms.org
"""

# Implementation author: Oldboy
# Created on 2017-10-28T09:56:04.557618Z
# Last modified on 2017-10-28T09:56:04.557618Z
# Version 1

import os

dir = os.path.dirname(os.path.abspath(__file__))
