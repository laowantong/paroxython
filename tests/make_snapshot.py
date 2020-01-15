from pathlib import Path


def make_snapshot(path: str, result: str, capsys):
    expected = Path(path).exists() and Path(path).read_text()
    if result != expected:
        with capsys.disabled():
            print(f"\nWARNING: Use version control to check the changes of snapshot '{path}'.")
        Path(path).write_text(result)
