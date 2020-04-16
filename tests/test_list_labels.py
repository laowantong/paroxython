import json
from pathlib import Path

import pytest
import regex

import context
from make_snapshot import make_snapshot
from paroxython.list_labels import list_labelled_programs, list_labelled_sources
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


def test_list_labelled_programs(capsys):
    result = list_labelled_programs(Path("tests/data/simple"))
    text = json.dumps(result, cls=ProgramEncoder, indent=2)
    text = regex.sub(r"\s*\[\s+(\d+),\s+(\d+)\s+\](,?)\s+", r"[\1,\2]\3", text)
    make_snapshot(Path("tests/snapshots/simple_labelled_programs.json"), text, capsys)


def test_list_labelled_sources(capsys):
    chunks = list(list_labelled_sources(Path("tests/data/simple")))
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
    make_snapshot(Path("tests/snapshots/simple_labelled_sources.py"), "\n".join(result), capsys)
