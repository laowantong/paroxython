from pathlib import Path

import pytest

import context
from make_snapshot import make_snapshot
from paroxython.generate_labels import generate_labelled_sources


def test_update_snapshots(capsys):
    # fmt: off
    DIRECTORIES = [
        "../Python/project_euler",
        "../Python/maths",
        "../Algo/programs",
    ]
    # fmt: on
    for directory in DIRECTORIES:
        path = Path(directory)
        if (path / "__is_private_directory").exists():
            output_path = Path(path.parent, "snapshot_" + path.parts[-1] + ".py")
        else:
            output_path = Path("tests/snapshots", "-".join(path.parts[-2:]) + ".py")
        acc = [result for result in generate_labelled_sources(path)]
        make_snapshot(output_path, "\n".join(acc), capsys)
