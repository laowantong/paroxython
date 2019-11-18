from pathlib import Path

import context
from paroxython import scanner

DIRECTORIES = [
    "../Python/project_euler",
    "../Python/maths",
    # "../Algo/programs",
]

for directory in DIRECTORIES:
    path = Path(directory)
    if (path / "__is_private_directory").exists():
        output_path = Path(path.parent, "snapshot_" + path.parts[-1] + ".py")
    else:
        output_path = Path("snapshots", "-".join(path.parts[-2:]) + ".py")
    acc = [result for result in scanner.scan(path)]
    output_path.write_text("\n".join(acc))
