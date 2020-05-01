"""List files in directory.

Create list _x containing the contents of directory _d.

_x may contain files and subfolders.
No recursive subfolder listing.

Source: programming-idioms.org
"""

# Implementation author: Oldboy
# Created on 2019-02-11T19:56:22.781171Z
# Last modified on 2019-03-26T21:25:46.969143Z
# Version 2

import os

x = os.listdir(d)
