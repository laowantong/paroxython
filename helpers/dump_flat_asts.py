"""Apply all AST-parsers on the regex-specified features, and dump the results for comparison."""

from pathlib import Path
import regex  # type: ignore

import context

from paroxython.flatten_ast import select_ast_post_processing, flatten_ast
from helpers.reformat_spec import reformat_spec

SPEC_PATH = Path("paroxython/resources/spec.md")

TEMPLATE = """
#### Feature `{label_name}`

##### Specification

```re
{spec}
```

##### Example

```python
{source}
```

#### Flat AST

```plain
{flat_ast}```
"""


def extract_specs(SPEC_PATH):
    text = SPEC_PATH.read_text()
    rex = r"""(?msx)
        ^\#{4}\s+Feature\s+`(.+?)` # capture the label's pattern
        .+?\#{5}\s+Specification # ensure the next code is in the Specification section
        .+?```(re|sql)\n+(.+?)\n``` # capture the language and the specification
        .+?\#{5}\s+Example # ensure the next code is in the Example section
        .+?```python\n+(.+?)\n``` # capture the source
    """
    return regex.finditer(rex, text)


import ast

reformat_spec(SPEC_PATH)
select_ast_post_processing()
specs = []
for match in extract_specs(SPEC_PATH):
    (label_name, language, spec, source) = match.groups()
    if language == "sql":
        continue
    source = regex.sub(r"(?m)^.{1,4}", "", source)
    try:
        parsed_source = ast.parse(source)
    except SyntaxError:
        continue
    flat_ast = flatten_ast(parsed_source)
    specs.append(
        TEMPLATE.format(
            label_name=label_name,
            spec=spec,
            source=source,
            flat_ast=flat_ast,
        )
    )
output_path = Path(f"sandbox/flat_asts.md")
output_path.write_text("\n".join(specs))
print(f"{len(specs)} ASTs dumped in '{output_path}'.")
