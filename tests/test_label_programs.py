import json
from pathlib import Path

import pytest
import regex

import context
from make_snapshot import make_snapshot
from paroxython.label_programs import ProgramLabeller
from paroxython.user_types import Span, ProgramName


class ProgramEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, type(ProgramName)):
            return str(obj)
        if isinstance(obj, Span):
            return obj.to_couple()
        if isinstance(obj, set):
            return sorted(obj)
        return json.JSONEncoder.default(self, obj)


labeller = ProgramLabeller()
labeller.label_programs(Path("examples/mini/programs"))


def test_label_programs(capsys):
    result = labeller.programs
    text = json.dumps(result, cls=ProgramEncoder, indent=2)
    text = regex.sub(r"\s*\[\s+(\d+),\s+(\d+)\s+\](,?)\s+", r"[\1,\2]\3", text)
    make_snapshot(Path("examples/mini/labelled_programs.json"), text, capsys)


def test_generate_labelled_sources(capsys):
    chunks = list(labeller.generate_labelled_sources())
    result = []
    for chunk in chunks:
        if chunk.startswith("#"):
            result.append(chunk)
        else:
            for line in chunk.split("\n"):
                if not line:
                    continue
                (source, _, comment) = line.partition(" # ")
                for label in comment.split(", "):
                    result.append(f"{source} # {label}")
                    source = " " * len(source)
            result.append("")
    make_snapshot(Path("examples/mini/labelled_sources.py"), "\n".join(result), capsys)


def test_update_snapshots(capsys):
    # fmt: off
    directories = [
        "examples/idioms/programs",
        "examples/mini/programs",
        "examples/simple/programs",
        "../algo/programs",
    ]
    # fmt: on
    labeller = ProgramLabeller()
    for directory in directories:
        path = Path(directory)
        if not path.is_dir():
            continue
        labeller.label_programs(path)
        output_path = Path(path.parent, path.parts[-1] + "_with_labels.py")
        acc = [result for result in labeller.generate_labelled_sources()]
        make_snapshot(output_path, "\n".join(acc), capsys)


if __name__ == "__main__":
    pytest.main(["-qq", __import__("sys").argv[0]])
