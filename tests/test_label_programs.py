import json
from pathlib import Path

import pytest
import regex

from make_snapshot import make_snapshot

import context
from paroxython.label_programs import labelled_programs, generate_labelled_sources
from paroxython.user_types import Span, ProgramPath


class ProgramEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, type(ProgramPath)):
            return str(obj)
        if isinstance(obj, Span):
            return obj.to_couple()
        if isinstance(obj, set):
            return sorted(obj)
        return json.JSONEncoder.default(self, obj)


programs = labelled_programs(Path("examples/mini/programs"))


def test_label_programs(capsys):
    result = programs
    text = json.dumps(result, cls=ProgramEncoder, indent=2)
    text = regex.sub(r'\s*\[\s+(\d+),\s+(\d+),\s+(".*?")\s+\](,?)\s*', r"[\1,\2,\3]\4", text)
    make_snapshot(Path("examples/mini/labelled_programs.json"), text, capsys)


def test_generate_labelled_sources(capsys):
    chunks = list(generate_labelled_sources(programs))
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
    directories = [
        "examples/idioms/programs",
        "examples/mini/programs",
        "examples/simple/programs",
        # "../algo/programs",
    ]
    for directory in directories:
        path = Path(directory)
        if not path.is_dir():
            continue
        acc = [result for result in generate_labelled_sources(labelled_programs(path))]
        output_path = Path(path.parent, path.parts[-1] + "_with_labels.py")
        make_snapshot(output_path, "\n".join(acc), capsys)


if __name__ == "__main__":
    pytest.main(["-qq", __import__("sys").argv[0]])
