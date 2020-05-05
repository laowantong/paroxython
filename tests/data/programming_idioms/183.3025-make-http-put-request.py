"""Make HTTP PUT request.

Make a HTTP request with method PUT to URL _u

Source: programming-idioms.org
"""

# Implementation author: awesmubarak
# Created on 2019-09-26T19:06:19.150608Z
# Last modified on 2019-09-27T19:11:23.885446Z
# Version 2

requests

import requests

content_type = "text/plain"
headers = {"Content-Type": content_type}
data = {}

r = requests.put(url, headers=headers, data=data)
status_code, content = r.status_code, r.content
