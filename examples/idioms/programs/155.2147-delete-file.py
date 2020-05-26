"""Delete file.

Delete from filesystem the file having path _filepath.

Source: programming-idioms.org
"""

# Implementation author: Oldboy
# Created on 2017-10-28T10:56:11.056208Z
# Last modified on 2019-09-26T15:16:25.002814Z
# Version 2

import pathlib

path = pathlib.Path(_filepath)
path.unlink()
