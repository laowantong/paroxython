from pathlib import Path

import pytest

import context
from make_snapshot import make_snapshot
from paroxython.label_programs import ProgramLabeller


def test_update_snapshots(capsys):
    # fmt: off
    directories = [
        "../Python/project_euler",
        "../Python/maths",
        "../Algo/programs",
    ]
    # fmt: on
    labeller = ProgramLabeller()
    for directory in directories:
        path = Path(directory)
        if not path.is_dir():
            continue
        labeller.label_programs(path)
        if (path / "__is_private_directory").exists():
            output_path = Path(path.parent, "snapshot_" + path.parts[-1] + ".py")
        else:
            output_path = Path("tests/snapshots", "-".join(path.parts[-2:]) + ".py")
        acc = [result for result in labeller.generate_labelled_sources()]
        make_snapshot(output_path, "\n".join(acc), capsys)


if __name__ == "__main__":
    pytest.main(["-qq", __import__("sys").argv[0]])
