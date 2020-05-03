import json
import subprocess
from pathlib import Path

import pytest
from paroxython.cli import cli

import context


def run(command_suffix):
    command = f"python -m paroxython.cli.cli {command_suffix}"
    print(command)
    result = subprocess.run(
        command,
        stdout=subprocess.PIPE,  # From Python 3.7, these two arguments can be
        stderr=subprocess.PIPE,  # ... replaced by: capture_output=True
        encoding="utf-8",
        shell=True,
        check=True,
    )
    print(f"STDERR: {result.stderr}")
    print(f"STDOUT: {result.stdout}")
    return str(result.stdout)


def test_help_messages():
    result = run("--help")
    assert "USAGE" in result
    assert "COMMANDS" in result
    result = run("collect -h")
    assert "USAGE" in result
    assert "OPTIONS" in result
    result = run("recommend -h")
    assert "USAGE" in result
    assert "OPTIONS" in result
    result = run("tag -h")
    assert "USAGE" in result
    assert "OPTIONS" in result


def test_tag():
    result = run("tag tests/data/simple/assignment.py")
    assert "| Taxon | Lines |" in result
    assert "| variable/assignment/single | 1 |" in result


def test_tag_options():
    result = run("tag --format tsv tests/data/simple/assignment.py")
    assert "Taxon\tLines" in result
    assert "variable/assignment/single\t1" in result

    result = run("tag --labels tests/data/simple/assignment.py")
    assert "| Label | Lines |" in result
    assert "| single_assignment:a | 1 |" in result

    result = run("tag --taxonomy tests/data/dummy/taxonomy.tsv tests/data/simple/fizzbuzz.py")
    assert "| flow/conditional | 4-11, 6-11, 8-11 |" in result


def test_collect():
    db_path = Path("tests/data/simple_db.json")
    expected_db = json.loads(db_path.read_text())
    result = run("collect tests/data/simple")
    assert "Labelling 4 programs." in result
    assert "Mapping taxonomy on 4 programs." in result
    assert f"Writing {db_path}." in result
    actual_db = json.loads(db_path.read_text())
    assert actual_db["programs"].keys() == expected_db["programs"].keys()
    assert actual_db["taxons"] == expected_db["taxons"]
    assert actual_db["labels"] == expected_db["labels"]
    assert (
        actual_db["programs"]["collatz_print.py"]["labels"]
        == expected_db["programs"]["collatz_print.py"]["labels"]
    )
    assert (
        actual_db["programs"]["collatz_print.py"]["taxons"]
        == expected_db["programs"]["collatz_print.py"]["taxons"]
    )


def test_collect_options():
    db_path = Path("tests/data/temp_db.json")

    result = run(f"collect -o {db_path} tests/data/simple")
    assert f"Writing {db_path}." in result
    db = json.loads(db_path.read_text())
    assert "\n\n" not in db["programs"]["fizzbuzz.py"]["source"]  # cleaned up

    result = run(f"collect -o {db_path} --cleanup none tests/data/simple")
    db = json.loads(db_path.read_text())
    assert "\n\n" in db["programs"]["fizzbuzz.py"]["source"]  # not cleaned up

    rex = r".+_.+"  # exclude collatz_print.py, is_even.py
    result = run(f'collect -o {db_path} --exclude "{rex}" tests/data/simple')
    assert "Labelling 2 programs." in result

    rex = r".+n.?\.py"  # exclude assignment.py, collatz_print.py, is_even.py
    result = run(f'collect -o {db_path} --exclude "{rex}" tests/data/simple')
    assert "Labelling 1 programs." in result

    glob = r"*n*.py"  # include assignment.py, collatz_print.py, is_even.py
    result = run(f'collect -o {db_path} --glob "{glob}" tests/data/simple')
    assert "Labelling 3 programs." in result

    result = run(f"collect -o {db_path} -t tests/data/dummy/taxonomy.tsv tests/data/simple")
    db = json.loads(db_path.read_text())
    assert db["taxons"] == {"flow/conditional": ["collatz_print.py", "fizzbuzz.py"]}

    db_path.unlink()


def test_recommend():
    pipe_path = Path("tests/data/dummy/pipe.py")
    db_path = Path("tests/data/dummy/db.json")
    result_path = Path("tests/data/dummy/temp_recommendations.md")
    _ = run(f"recommend -o {result_path} -p {pipe_path} {db_path}")
    result_text = result_path.read_text()
    assert result_text == Path("tests/data/dummy/recommendations.md").read_text()

    _ = run(f"recommend -o {result_path} -p {pipe_path} -c length {db_path}")
    result_text = result_path.read_text()
    assert "1 program of learning cost in [1, 2[" in result_text
    assert "1 program of learning cost in [4, 8[" in result_text
    result_path.unlink()


if __name__ == "__main__":
    pytest.main(["-qq", __import__("sys").argv[0]])
