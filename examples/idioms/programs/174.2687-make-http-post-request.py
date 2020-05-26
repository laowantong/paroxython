"""Make HTTP POST request.

Make a HTTP request with method POST to URL _u

Source: programming-idioms.org
"""

# Implementation author: random
# Created on 2019-09-26T13:28:18.453487Z
# Last modified on 2019-09-26T13:28:18.453487Z
# Version 1

# Explicit use of the "method" parameter, because "GET" is used when "data" is None

from urllib import request, parse

data = parse.urlencode("<your data dict>").encode()
req = request.Request(u, data=data, method="POST")
resp = request.urlopen(req)
