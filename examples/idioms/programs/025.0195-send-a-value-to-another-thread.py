"""Send a value to another thread.

Share the string value "Alan" with an existing running process which will then display "Hello, Alan"

Source: programming-idioms.org
"""

# Implementation author: Aristide
# Created on 2016-02-18T16:57:58.135862Z
# Last modified on 2022-09-04
# Version 2

from queue import Queue
from threading import Thread

q = Queue()

def worker():
    while True:
        print(f"Hello, {q.get()}")
        q.task_done()

Thread(target=worker, daemon=True).start()

q.put("Alan")
q.join()