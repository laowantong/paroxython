"""Send a value to another thread.

Share the string value "Alan" with an existing running process which will then display "Hello, Alan"

Source: programming-idioms.org
"""

# Implementation author: programming-idioms.org
# Created on 2016-02-18T16:57:58.135862Z
# Last modified on 2016-02-18T16:57:58.135862Z
# Version 1

# The _Queue module has been renamed to _queue in Python 3.

import Queue

q = Queue()

t = Thread(target=worker)
t.daemon = True
t.start()

q.put("Alan")
