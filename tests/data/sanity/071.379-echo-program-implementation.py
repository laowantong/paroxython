"""Echo program implementation.

Basic implementation of the Echo program: Print all arguments except the program name, separated by space, followed by newline.
The idiom demonstrates how to skip the first argument if necessary, concatenate arguments as strings, append newline and print it to stdout.

Source: christianhujer
"""

# Implementation author: christianhujer
# Created on 2016-02-18T16:58:01.212065Z
# Last modified on 2016-02-18T16:58:01.212065Z
# Version 1

import sys

print " ".join(sys.argv[1:])
