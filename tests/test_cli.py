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


def test_cli():
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
    with pytest.raises(subprocess.CalledProcessError):
        run("foobar")


def test_tag():
    result = run("tag examples/mini/programs/assignment.py")
    assert "| Taxon | Lines |" in result
    assert "| variable/assignment/single | 1 |" in result


def test_tag_options():
    result = run("tag --format tsv examples/mini/programs/assignment.py")
    assert "Taxon\tLines" in result
    assert "variable/assignment/single\t1" in result

    result = run("tag --labels examples/mini/programs/assignment.py")
    assert "| Label | Lines |" in result
    assert "| single_assignment:a | 1 |" in result

    result = run("tag --taxonomy examples/dummy/taxonomy.tsv examples/mini/programs/fizzbuzz.py")
    assert "| flow/conditional | 4-11, 6-11, 8-11 |" in result


def test_collect():
    db_path = Path("examples/mini/programs_db.json")
    result = run("collect examples/mini/programs")
    assert "Labelling 4 programs." in result
    assert "Mapping taxonomy on 4 programs." in result
    assert f"Writing {db_path}." in result


def test_collect_options():
    db_path = Path("examples/mini/temp_db.json")

    result = run(f"collect -o {db_path} examples/mini/programs")
    assert f"Writing {db_path}." in result
    db = json.loads(db_path.read_text())
    assert "\n\n" not in db["programs"]["fizzbuzz.py"]["source"]  # cleaned up

    result = run(f"collect -o {db_path} --cleanup none examples/mini/programs")
    db = json.loads(db_path.read_text())
    assert "\n\n" in db["programs"]["fizzbuzz.py"]["source"]  # not cleaned up

    rex = r".+_.+"  # exclude is_even.py
    result = run(f'collect -o {db_path} --exclude "{rex}" examples/mini/programs')
    assert "Labelling 3 programs." in result

    rex = r".+n.?\.py"  # exclude assignment.py, is_even.py
    result = run(f'collect -o {db_path} --exclude "{rex}" examples/mini/programs')
    assert "Labelling 2 programs." in result

    glob = r"*n*.py"  # include assignment.py, is_even.py
    result = run(f'collect -o {db_path} --glob "{glob}" examples/mini/programs')
    assert "Labelling 2 programs." in result

    result = run(f"collect -o {db_path} -t examples/dummy/taxonomy.tsv examples/mini/programs")
    db = json.loads(db_path.read_text())
    assert db["taxons"] == {"flow/conditional": ["collatz.py", "fizzbuzz.py"]}

    db_path.unlink()

    db_path = Path("examples/mini/programs_db.sqlite")
    result = run(f"collect -o {db_path} examples/mini/programs")
    assert f"Writing {db_path}." in result
    assert db_path.is_file()
    db_path.unlink()


def test_recommend():
    pipe_path = Path("examples/dummy/pipe.py")
    db_path = Path("examples/dummy/programs_db.json")
    result_path = Path("examples/dummy/temp_recommendations.md")
    run(f"recommend -o {result_path} -p {pipe_path} {db_path}")
    result_text = result_path.read_text()
    assert result_text == Path("examples/dummy/programs_recommendations.md").read_text()

    run(f"recommend -o {result_path} -p {pipe_path} -c linear {db_path}")
    result_text = result_path.read_text()
    assert "1 program of learning cost in [1, 2[" in result_text
    assert "1 program of learning cost in [4, 8[" in result_text

    result = run(f"recommend -o {result_path} {db_path}")  # implicit empty pipeline
    assert "Processing 0 commands on 9 programs" in result

    result_path.unlink()

    with pytest.raises(subprocess.CalledProcessError):
        run(f"recommend -p foobar.py {db_path}")  # non existing

    with pytest.raises(subprocess.CalledProcessError):
        run(f"recommend -p paroxython/goodies.py {db_path}")  # malformed


if __name__ == "__main__":
    pytest.main(["-qq", __import__("sys").argv[0]])
