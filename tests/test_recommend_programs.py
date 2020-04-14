from pathlib import Path

import pytest

import context


from paroxython.recommend_programs import recommend_programs


def test_recommend_program():
    result = recommend_programs(Path("tests/data/dummy/pipe.py"))
    print(result)
    assert (
        "\n".join(
            [
                "# Quantitative summary",
                "-   9 programs initially.",
                "-   1 program removed by impart/programs/name.",
                "-   2 programs removed by exclude/programs/name.",
                "-   3 programs removed by exclude/taxons/pattern.",
                "-   1 program removed by include/taxons/pattern.",
                "-   2 programs remaining.",
            ]
        )
        in result
    )
