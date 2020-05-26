"""Find files with a given list of filename extensions.

Construct a list _L that contains all filenames that have the extension ".jpg" , ".jpeg" or ".png" in directory _D and all it's subdirectories.

Source: Bart
"""

# Implementation author: âne O' nym
# Created on 2019-09-26T14:12:32.0025Z
# Last modified on 2019-09-26T14:13:11.52677Z
# Version 2

# * list comprehension
# * iterate over all files and all directories in tree under _D (os module)
# * iterate over all files found
# * filter with regex matching the end of the filename (re module)
# * regex is cached, but may be compiled beforehands

import re
import os

filtered_files = [
    "{}/{}".format(dirpath, filename)
    for dirpath, _, filenames in os.walk(D)
    for filename in filenames
    if re.match(r"^.*\.(?:jpg|jpeg|png)$", filename)
]
