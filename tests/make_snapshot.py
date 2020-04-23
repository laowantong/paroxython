from pathlib import Path

import pytest


def make_snapshot(path: Path, result: str, capsys):
    expected = path.exists() and path.read_text()
    if result != expected:
        with capsys.disabled():
            print(f"\nWARNING: Use version control to check the changes of snapshot '{path}'.")
        path.write_text(result)


if __name__ == "__main__":
    pytest.main(["-qq", __import__("sys").argv[0]])
