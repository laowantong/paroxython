"""Print log line with datetime.

Print message _msg, prepended by current date and time.

Explain what behavior is idiomatic: to _stdout or _stderr, and what the date format is.

Source: programming-idioms.org
"""

# Implementation author: cons0l3
# Created on 2016-09-14T08:27:08.139734Z
# Last modified on 2016-09-17T21:34:16.405525Z
# Version 5

# Default output is stderr.
#
# Date format is ISO 8601.

import sys, logging

logging.basicConfig(
    stream=sys.stdout, level=logging.DEBUG, format="%(asctime)-15s %(message)s"
)
logger = logging.getLogger("NAME OF LOGGER")

logger.info(msg)
