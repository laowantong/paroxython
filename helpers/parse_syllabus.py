import sys
from pathlib import Path

import regex  # type: ignore

raw_text = Path(sys.argv[1]).read_text()
useful_part = regex.search(r"(?sm)(.*)^ *# EOF\b", raw_text)[1]
pattern = r"\+ *(?:\[.+?\] *)?(\w+(?<![-_]tests?)\.py)\b"
for match in regex.finditer(pattern, useful_part):
    print(match[1])
