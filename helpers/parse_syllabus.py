import sys
from pathlib import Path

import regex  # type: ignore

raw_text = Path(sys.argv[1]).read_text()
useful_part = regex.search(r"(?sm)(.*)^ *# EOF\b", raw_text)[1]
for match in regex.finditer(r"\+ *(?:\[.+?\] *)?(\w+\.py)\b", useful_part):
    print(match[1])
