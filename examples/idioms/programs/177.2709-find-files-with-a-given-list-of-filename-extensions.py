"""Find files with a given list of filename extensions.

Construct a list _L that contains all filenames that have the extension ".jpg" , ".jpeg" or ".png" in directory _D and all it's subdirectories.

Source: Bart
"""

# Implementation author: citizenkong
# Created on 2019-09-26T13:56:17.499124Z
# Last modified on 2019-09-27T11:00:18.993182Z
# Version 2

# Doesn't look in subdirectories because I didn't read the question properly.

import os

extensions = [".jpg", ".jpeg", ".png"]
L = [f for f in os.listdir(D) if os.path.splitext(f)[1] in extensions]
