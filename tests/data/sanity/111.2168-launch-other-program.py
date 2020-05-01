"""Launch other program.

From current process, run program _x with command-line parameters "a", "b".

Source: programming-idioms.org
"""

# Implementation author: Oldboy
# Created on 2017-10-28T13:48:41.476134Z
# Last modified on 2017-10-28T13:48:41.476134Z
# Version 1

import subprocess

subprocess.call(["x", "a", "b"])
