import pytest

import context
from paroxython import label_generators
from paroxython import program_generator


def test_label_generator():
    programs = program_generator.generate_programs("tests/data/programs")
    result = label_generators.generate_labeled_sources(programs)

    assert "assignment.py" in next(result)
    assert next(result).strip() == "a = b # assignment, global_variable_definition"

    assert "function_definition.py" in next(result)
    assert next(result).strip() == "\n".join(
        [
            "def succ(n): # function_definition:succ (-> +1)",
            "    return n + 1 # binary_operator:Add, literal:Num",
        ]
    )

    assert "loop.py" in next(result)
    assert next(result).strip() == "\n".join(
        [
            "while input(): # function_call:input",
            '    print("foobar") # function_call:print, literal:Str',
        ]
    )


pytest.main(args=["-q"])
