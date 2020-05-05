"""Load from HTTP GET request into a string.

Make an HTTP request with method GET to URL _u, then store the body of the response in string _s.

Source: programming-idioms.org
"""

# Implementation author: Oldboy
# Created on 2017-10-29T09:59:08.181801Z
# Last modified on 2017-10-29T10:10:54.980586Z
# Version 2

import urllib.request

with urllib.request.urlopen(u) as f:
    s = f.read()
