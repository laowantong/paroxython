"""Load from HTTP GET request into a file.

Make an HTTP request with method GET to URL _u, then store the body of the response in file _result._txt. Try to save the data as it arrives if possible, without having all its content in memory at once.

Source: programming-idioms.org
"""

# Implementation author: Oldboy
# Created on 2017-10-29T10:09:43.586786Z
# Last modified on 2017-10-29T10:09:43.586786Z
# Version 1

import urllib

filename, headers = urllib.request.urlretrieve(u, "result.txt")
