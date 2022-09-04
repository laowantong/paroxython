from ast import literal_eval
import json
from pathlib import Path

import pytest

from make_snapshot import make_snapshot

import context
from paroxython.recommend_programs import Recommendations


def test_recommend_program(capsys):
    rec = Recommendations(
        db=json.loads(Path("examples/dummy/programs_db.json").read_text()),
        base_path=Path("examples/dummy/"),
    )
    rec.run_pipeline(literal_eval(Path("examples/dummy/pipe.py").read_text()))
    print(rec.selected_programs)
    assert rec.selected_programs == {
        "prg2.py",
        # "O/N/P",
        # "Y/T/Q",
        # "Y",
        # "X/S/M/L/R/D",
        # "O",
        # "O/C/H/B",
        # "X/S/M",
        # "X/S/M/L/R",
        # "Y/T",
        # "O/C",
        # "X/G",
        # "X/S/M/L/V",
        # "O/C/H/B/I",
        "prg3.py",
        # "O/N/P",
        # "X/K",
        # "Y/T",
        # "X/S/M/L/V",
        # "O/C/H/B",
        # "X/S/M/L/R",
        # "O/J",
        # "X/S/M",
        # "O/C/F/U",
        # "O/C/H",
        # "X/S",
        # "Y",
        # "O",
        # "X/S/M/L",
        # "Y/E",
    }
    print(rec.result)
    assert rec.result == [
        (5, "impart", ["prg8.py"]),
        (6, "exclude", ["prg7.py", "prg9.py"]),
        (7, "exclude", ["prg4.py", "prg5.py", "prg6.py"]),
        (8, "include", ["prg1.py"]),
        (9, "hide", []),
    ]
    costs = {taxon: rec.assess.taxon_cost(taxon) for taxon in rec.db_programs["prg2.py"]["taxa"]}
    print(costs)
    assert costs == {
        "O/N/P": 0,
        "Y/T/Q": 0.375,
        "Y": 0,
        "X/S/M/L/R/D": 0,
        "O": 0,
        "O/C/H/B": 0,
        "X/S/M": 0,
        "X/S/M/L/R": 0,
        "Y/T": 0.25,
        "O/C": 0,
        "X/G": 0.25,
        "X/S/M/L/V": 0,
        "O/C/H/B/I": 0.03125,
    }
    text = rec.get_markdown(span_column_width=10)
    make_snapshot(Path("examples/dummy/programs_recommendations.md"), text, capsys)


def test_recommend_programming_idioms(capsys):
    path = Path("examples/idioms/programs_db.json")
    rec = Recommendations(db=json.loads(path.read_text()))
    rec.run_pipeline()
    output_path = path.parent / "programs_recommendations.md"
    rec.get_markdown()  # for coverage
    make_snapshot(
        output_path,
        rec.get_markdown(sorting_strategy="lexicographic", grouping_strategy="no_group"),
        capsys,
    )


def test_recommend_mini_programs():
    db = json.loads(Path("examples/mini/programs_db.json").read_text())
    proper_taxa = {}
    for program in ["assignment.py", "collatz.py", "fizzbuzz.py", "is_even.py"]:
        proper_taxa[program] = set(db["programs"][program]["taxa"])

    rec = Recommendations(db)
    original = proper_taxa["fizzbuzz.py"] | proper_taxa["collatz.py"]
    assert all(
        taxon.startswith("meta")
        for taxon in original.difference(db["programs"]["fizzbuzz.py"]["taxa"])
    )

    commands = [
        {
            "operation": "exclude",
            "data": [
                "assignment.py",
                "fizzbuzz.py",  # imported by is_even.py, consequently excluded
            ],
        }
    ]
    rec = Recommendations(db)
    rec.run_pipeline(commands)
    assert rec.selected_programs == {"collatz.py"}
    assert not rec.imparted_knowledge

    # A command excluding a sequence is equivalent to a sequence of excluding commands
    commands = [
        {"operation": "exclude", "data": ["assignment.py"]},
        {"operation": "exclude", "data": ["fizzbuzz.py"]},
    ]
    rec = Recommendations(db)
    rec.run_pipeline(commands)
    assert rec.selected_programs == {"collatz.py"}
    assert not rec.imparted_knowledge

    commands = [{"operation": "include", "data": ["this_program_does_not_exist.py"]}]
    rec = Recommendations(db)
    rec.run_pipeline(commands)
    assert not rec.selected_programs
    assert not rec.imparted_knowledge

    commands = [
        {
            "operation": "include",
            "data": [
                "assignment.py",
                "fizzbuzz.py",  # imported by is_even.py, which nevertheless will not be included
            ],
        }
    ]
    rec = Recommendations(db)
    rec.run_pipeline(commands)
    assert rec.selected_programs == {"assignment.py", "fizzbuzz.py"}
    assert not rec.imparted_knowledge

    # A command including a sequence is not equivalent to a sequence of including commands
    commands = [
        {"operation": "include", "data": ["assignment.py"]},
        {"operation": "include", "data": ["fizzbuzz.py"]},
    ]
    rec = Recommendations(db)
    rec.run_pipeline(commands)
    assert not rec.selected_programs
    assert not rec.imparted_knowledge

    commands = [
        {
            "operation": "impart",
            "data": [
                "assignment.py",  # exclude it, and impart its taxa
                "fizzbuzz.py",  # idem, but ignore its imports or exports
            ],
        }
    ]
    rec = Recommendations(db)
    rec.run_pipeline(commands)
    assert rec.selected_programs == {"collatz.py", "is_even.py"}
    assert proper_taxa["assignment.py"].issubset(rec.imparted_knowledge)
    assert proper_taxa["fizzbuzz.py"].issubset(rec.imparted_knowledge)
    assert not proper_taxa["is_even.py"].issubset(rec.imparted_knowledge)
    assert not proper_taxa["collatz.py"].issubset(rec.imparted_knowledge)

    commands = [{"operation": "impart", "data": ["operator/arithmetic"]}]
    rec = Recommendations(db)
    rec.run_pipeline(commands)
    assert rec.selected_programs == {"assignment.py", "collatz.py", "fizzbuzz.py", "is_even.py"}
    print(rec.imparted_knowledge)
    assert rec.imparted_knowledge == {
        "operator/arithmetic/multiplication",
        "operator/arithmetic/modulo",
        "operator",
        "operator/arithmetic",
        "operator/arithmetic/addition",
    }

    commands = [
        {
            "operation": "exclude",
            "data": [
                "var/assignment/explicit/single",  # featured directly by assignment.py
                # and collatz.py, which is imported by fizzbuzz.py and is_even.py
            ],
        }
    ]
    rec = Recommendations(db)
    rec.run_pipeline(commands)
    assert not rec.selected_programs
    assert not rec.imparted_knowledge

    commands = [
        {
            "operation": "exclude",
            "data": [
                "flow/conditional/else/if",  # featured directly by fizzbuzz.py,
                # which is imported by is_even.py
            ],
        }
    ]
    rec = Recommendations(db)
    rec.run_pipeline(commands)
    assert rec.selected_programs == {"assignment.py", "collatz.py"}

    commands = [
        {
            "operation": "include",
            "data": [
                ("meta/program", "not contains", "flow/conditional/else/if"),
                # There is a subtle difference with the previous one, since "exclude" follows the
                # importations, while "include" does not.
            ],
        }
    ]
    rec = Recommendations(db)
    rec.run_pipeline(commands)
    assert rec.selected_programs == {"assignment.py", "collatz.py", "is_even.py"}

    commands = [
        {
            "operation": "include",
            "data": [
                "flow/conditional/else/if",
            ],
        }
    ]
    rec = Recommendations(db)
    rec.run_pipeline(commands)
    assert rec.selected_programs == {"fizzbuzz.py"}

    commands = [
        {
            "operation": "exclude",
            "data": [
                ("meta/program", "not contains", "flow/conditional/else/if"),
                # "assignment.py", "is_even.py", "collatz.py" are excluded since they don't feature
                # an `elif`. "fizzbuzz.py" features an `elif`, but is excluded since it imports an
                # excluded program ("collatz.py").
            ],
        }
    ]
    rec = Recommendations(db)
    rec.run_pipeline(commands)
    assert not rec.selected_programs

    commands = [
        {
            "operation": "exclude",
            "data": [
                "flow/conditional/else/if",  # Although not recommended, it is possible to mix
                "assignment.py"  # taxa and programs (ending with ".py") in a same command.
                # Crucially, this avoids to specify whether the command should be applied on
                # taxa or programs.
            ],
        }
    ]
    rec = Recommendations(db)
    rec.run_pipeline(commands)
    assert rec.selected_programs == {"collatz.py"}
    assert not rec.imparted_knowledge

    commands = [
        {
            "operation": "include",
            "data": [
                "var/assignment/explicit/single",  # featured by assignment.py and collatz.py
                # Although the latter is imported by both fizzbuzz.py and is_even.py, they are
                # not included in the result
            ],
        }
    ]
    rec = Recommendations(db)
    rec.run_pipeline(commands)
    assert rec.selected_programs == {"assignment.py", "collatz.py"}
    assert not rec.imparted_knowledge

    commands = [{"operation": "include", "data": ["this_taxon_does_not_exist"]}]
    rec = Recommendations(db)
    rec.run_pipeline(commands)
    assert not rec.selected_programs
    assert not rec.imparted_knowledge

    commands = [
        {
            "operation": "include",
            "data": [
                ("var/assignment/explicit", "inside", "flow/loop"),
            ],  # featured by collatz.py only
        }
    ]
    rec = Recommendations(db)
    rec.run_pipeline(commands)
    assert rec.selected_programs == {"collatz.py"}
    assert not rec.imparted_knowledge

    commands = [
        {
            "operation": "exclude",
            "data": [
                ("var/assignment/explicit", "inside", "flow/loop"),  # featured by collatz.py,
                # and indirectly by fizzbuzz.py and is_even.py
            ],
        }
    ]
    rec = Recommendations(db)
    rec.run_pipeline(commands)
    assert rec.selected_programs == {"assignment.py"}
    assert not rec.imparted_knowledge

    commands = [
        {
            "operation": "include",
            "data": [
                ("var/assignment/explicit", "not inside", "flow/loop"),  # Must read as:
                # Include all programs featuring an assignment, except those where this assignment
                # is inside a loop. Hence, this includes assignment.py, even if it does not feature
                # a loop.
            ],
        }
    ]
    rec = Recommendations(db)
    rec.run_pipeline(commands)
    assert rec.selected_programs == {"assignment.py"}
    assert not rec.imparted_knowledge

    commands = [
        {
            "operation": "include",
            "data": [
                ("var/assignment/explicit", "inside", "meta/program"),  # This comes down to
                # including all programs featuring an assignment.
            ],
        }
    ]
    rec = Recommendations(db)
    rec.run_pipeline(commands)
    print(rec.selected_programs)
    assert rec.selected_programs == {"assignment.py", "collatz.py"}
    assert not rec.imparted_knowledge

    commands = [
        {
            "operation": "include",
            "data": [
                ("var/assignment/explicit", "not inside", "meta/program"),  # This comes down to
                # exclude all programs either featuring or not featuring an assignment!
            ],
        }
    ]
    rec = Recommendations(db)
    rec.run_pipeline(commands)
    print(rec.selected_programs)
    assert not rec.selected_programs
    assert not rec.imparted_knowledge

    commands = [
        {
            "operation": "impart",  # Imparting triples is currently not supported (ignored).
            "data": [("var/assignment/explicit", "inside", "flow/loop")],
        }
    ]
    rec = Recommendations(db)
    rec.run_pipeline(commands)
    assert rec.selected_programs == {
        "assignment.py",
        "collatz.py",
        "fizzbuzz.py",
        "is_even.py",
    }
    assert not rec.imparted_knowledge

    commands = [{"operation": "include", "data": 42}]  # malformed source => ignored command
    rec = Recommendations(db)
    rec.run_pipeline(commands)
    assert rec.selected_programs == {
        "assignment.py",
        "collatz.py",
        "fizzbuzz.py",
        "is_even.py",
    }
    assert not rec.imparted_knowledge

    commands = [{"operation": "include", "data": [42]}]  # malformed pattern => ignored pattern
    rec = Recommendations(db)
    rec.run_pipeline(commands)
    assert rec.selected_programs == set()
    assert not rec.imparted_knowledge

    commands = [{"data": []}]  # a command without operation is ignored
    rec = Recommendations(db)
    rec.run_pipeline(commands)
    assert rec.selected_programs == {
        "assignment.py",
        "collatz.py",
        "fizzbuzz.py",
        "is_even.py",
    }
    assert not rec.imparted_knowledge

    commands = [
        {
            "operation": "undefined_command",  # an undefined command is ignored
            "data": "assignment.py",
        }
    ]
    rec = Recommendations(db)
    rec.run_pipeline(commands)
    assert rec.selected_programs == {
        "assignment.py",
        "collatz.py",
        "fizzbuzz.py",
        "is_even.py",
    }
    assert not rec.imparted_knowledge

    commands = [
        {
            "operation": "exclude",
            "data": [
                ("var/assignment/explicit/single", "after", "call/subroutine/builtin/print"),
                # collatz.py and fizzbuzz.py have an assignment after a print.
                # is_even.py imports fizzbuzz.py.
                # Consequently, these three programs are excluded.
            ],
        }
    ]
    rec = Recommendations(db)
    rec.run_pipeline(commands)
    assert rec.selected_programs == {"assignment.py"}
    assert not rec.imparted_knowledge

    commands = [
        {
            "operation": "exclude",
            "data": [
                ("operator/arithmetic/addition", "equals", "operator/arithmetic/multiplication"),
                # "operator/arithmetic/addition" and "operator/arithmetic/multiplication" are both
                # featured on the same line of collatz.py, and indirectly by fizzbuzz.py and
                # is_even.py. Therefore, excluding this taxon keeps only assignment.py.
            ],
        }
    ]
    rec = Recommendations(db)
    rec.run_pipeline(commands)
    assert rec.selected_programs == {"assignment.py"}
    assert not rec.imparted_knowledge

    commands = [
        {
            "operation": "exclude",
            "data": [
                ("condition/equality", "inside", "def/subroutine/function"),
                # "condition/equality" is inside "def/subroutine/function" in is_even.py, which is not
                # imported anywhere.
            ],
        }
    ]
    rec = Recommendations(db)
    rec.run_pipeline(commands)
    assert rec.selected_programs == {"collatz.py", "assignment.py", "fizzbuzz.py"}
    assert not rec.imparted_knowledge

    commands = [
        {
            "operation": "exclude",
            "data": [
                ("call/subroutine/builtin/range", "inside", "flow/conditional"),
                # "call/subroutine/builtin/range" is not inside "flow/conditional" anywhere.
            ],
        }
    ]
    rec = Recommendations(db)
    rec.run_pipeline(commands)
    assert rec.selected_programs == {
        "is_even.py",
        "fizzbuzz.py",
        "assignment.py",
        "collatz.py",
    }
    assert not rec.imparted_knowledge

    commands = [
        {
            "operation": "include",
            "data": [
                ("var/assignment/explicit/single", "after", "call/subroutine/builtin/print"),
                # The taxon "var/assignment/explicit/single" is featured by assignment.py and
                # collatz.py. In collatz.py, it appears after a taxon "call/subroutine/builtin/print".
                # Consequently, it should be included in the results, but not the programs which
                # import it: fizzbuzz.py and is_even.py.
            ],
        }
    ]
    rec = Recommendations(db)
    rec.run_pipeline(commands)
    assert rec.selected_programs == {"collatz.py"}
    assert not rec.imparted_knowledge

    commands = [
        {
            "operation": "include",
            "data": [
                ("operator/arithmetic/modulo", "equals", "type/number/integer/literal"),
                # "operator/arithmetic/modulo" and "type/number/integer/literal" are both featured
                # on the same line in all programs except assignment.py
            ],
        }
    ]
    rec = Recommendations(db)
    rec.run_pipeline(commands)
    assert rec.selected_programs == {"collatz.py", "is_even.py", "fizzbuzz.py"}
    assert not rec.imparted_knowledge

    commands = [
        {
            "operation": "include",
            "data": [
                ("operator/arithmetic/modulo", "x == y", "type/number/integer/literal"),
                # The same with "x == y" instead of "equals"
            ],
        }
    ]
    rec = Recommendations(db)
    rec.run_pipeline(commands)
    assert rec.selected_programs == {"collatz.py", "is_even.py", "fizzbuzz.py"}
    assert not rec.imparted_knowledge

    commands = [
        {
            "operation": "include",
            "data": [
                ("condition/equality", "inside", "def/subroutine/function"),
                # "condition/equality" is inside "def/subroutine/function" in is_even.py, which is not
                # imported anywhere.
            ],
        }
    ]
    rec = Recommendations(db)
    rec.run_pipeline(commands)
    assert rec.selected_programs == {"is_even.py"}
    assert not rec.imparted_knowledge

    commands = [
        {
            "operation": "include",
            "data": [
                ("condition/equality$", "inside", "def"),
                # "condition/equality" (strictly, note the dollar sign) is inside "def/subroutine/function"
                # in is_even.py and inside "def/subroutine/procedure" in collatz.py. Both will be
                # included.
            ],
        }
    ]
    rec = Recommendations(db)
    rec.run_pipeline(commands)
    assert rec.selected_programs == {"collatz.py", "is_even.py"}
    assert not rec.imparted_knowledge

    commands = [
        {
            "operation": "include",
            "data": [
                ("call/subroutine/builtin/range", "inside", "flow/conditional"),
                # "call/subroutine/builtin/range" is not inside "flow/conditional" anywhere.
            ],
        }
    ]
    rec = Recommendations(db)
    rec.run_pipeline(commands)
    assert not rec.selected_programs
    assert not rec.imparted_knowledge

    commands = [
        {
            "operation": "include",
            "data": [
                ("call/subroutine/builtin/print", "is", "call/subroutine/builtin/print"),
                # "call/subroutine/builtin/print" may appear several times in the same program, but
                # never on the same line.
            ],
        }
    ]
    rec = Recommendations(db)
    rec.run_pipeline(commands)
    assert not rec.selected_programs
    assert not rec.imparted_knowledge

    commands = [
        {
            "operation": "include",
            "data": [
                ("type/number/integer/literal$", "is", "type/number/integer/literal$"),
                # "type/number/integer/literal" appears twice on the same line in fizzbuzz.py and
                # collatz.py
            ],
        }
    ]
    rec = Recommendations(db)
    rec.run_pipeline(commands)
    assert rec.selected_programs == {"fizzbuzz.py", "collatz.py"}
    assert not rec.imparted_knowledge

    commands = [
        {
            "operation": "include",
            "data": [
                ("type/number/integer/literal$", "is", "type/number/integer/literal$"),
                # "type/number/integer/literal" appears twice on the same line in fizzbuzz.py and
                # collatz.py
            ],
        }
    ]
    rec = Recommendations(db)
    rec.run_pipeline(commands)
    assert rec.selected_programs == {"fizzbuzz.py", "collatz.py"}
    assert not rec.imparted_knowledge

    commands = [
        {
            "operation": "include",
            "data": [
                ("call/subroutine/builtin/print", "not inside", "flow/loop/exit/late"),
                # A print statement is featured inside a loop by both collatz.py and fizzbuzz.py.
                # However, in collatz.py, there exists a print statement which is not inside the
                # loop. This makes it satisfy the predicate. Note that assignment.py and is_even.py
                # are not included in the result, since they don't feature (at least directly)
                # "call/subroutine/builtin/print".
            ],
        }
    ]
    rec = Recommendations(db)
    rec.run_pipeline(commands)
    assert rec.selected_programs == {"collatz.py"}
    assert not rec.imparted_knowledge

    commands = [
        {
            "operation": "exclude",
            "data": [
                ("call/subroutine/builtin/print", "not inside", "flow/loop"),
                # Exclude the programs which feature a print statement outside a loop. This does
                # not exclude assignment.py, which does not feature a print statement. This
                # excludes collatz, which features a print statement outside a loop, even if it
                # also features a print statement inside a loop. fizzbuzz.py and is_even.py are
                # excluded too, since they import collatz.py
            ],
        }
    ]
    rec = Recommendations(db)
    rec.run_pipeline(commands)
    print(rec.selected_programs)
    assert rec.selected_programs == {"assignment.py"}
    assert not rec.imparted_knowledge


db = json.loads(Path("examples/simple/programs_db.json").read_text())

# extract_1 (start)
a = "flow/conditional"
b = "flow/loop"
_a = ("meta/program", "not contains", "flow/conditional")
_b = ("meta/program", "not contains", "flow/loop")
p0 = "01_hello_world.py"  # [ ] loop [ ] conditional
p1 = "03_friends.py"  #     [X] loop [ ] conditional
p2 = "14_median.py"  #      [ ] loop [X] conditional
p3 = "06_regex.py"  #       [X] loop [X] conditional
base_1 = [p0, p1, p2, p3]

# fmt: off
pipelines_1 = [
    (set()           , [("include", [a]), ("include", [_a])]), # a & ~a
    ({        p2, p3}, [("include", [a])]), # a
    ({p0, p1,       }, [("include", [_a])]), # ~a
    ({    p1,     p3}, [("include", [b])]), # b
    ({p0,     p2,   }, [("include", [_b])]), # ~b
    ({    p1, p2, p3}, [("include", [a, b])]), #  a | b
    ({p0,           }, [("include", [_a]), ("include", [_b])]), #  ~a & ~b
    ({            p3}, [("include", [a]), ("include", [b])]), #  a & b
    ({p0, p1, p2,   }, [("include", [_a, _b])]), #  ~a | ~b
    ({p0, p1,     p3}, [("include", [_a, b])]), # ~a | b
    ({        p2,   }, [("include", [a]), ("include", [_b])]), # a & ~b
    ({    p1,       }, [("include", [_a]), ("include", [b])]), # ~a & b
    ({p0,     p2, p3}, [("include", [a, _b])]), # a | ~b
    ({p0,         p3}, [("include", [_a, b]), ("include", [a, _b])]), # (~a | b) & (a | ~b)
    ({    p1, p2,   }, [("include", [a, b]), ("include", [_a, _b])]), # (a | b) & (~a | ~b)
    ({p0, p1, p2, p3}, [("include", [a, _a]), ("include", [b, _b])]), # (a | ~a) & (b | ~b)
]
# fmt: on
# extract_1 (stop)


@pytest.mark.parametrize("expected_programs, commands", pipelines_1)
def test_recommend_simple_programs_1(expected_programs, commands):
    rec = Recommendations(db)
    rec.run_pipeline(
        [{"operation": operation, "data": data} for (operation, data) in commands]
        + [{"operation": "include", "data": base_1}]
    )
    print(rec.selected_programs)
    assert rec.selected_programs == expected_programs


holds_abstr = "def"
holds_assignment = "var/assignment/explicit"
holds_asg_in_sub = ("var/assignment/explicit", "inside", "def")
lacks_assignment = ("meta/program", "not contains", "var/assignment/explicit")
lacks_abstr = ("meta/program", "not contains", "def")
lacks_asg_or_sub = ("meta/program", "not contains", "def|var/assignment/explicit")
lacks_asg_in_sub = ("def", "not contains", "var/assignment/explicit")
p0 = "01_hello_world.py"  # [ ] def [ ] assignment [ ] inside *
p1 = "05_greet.py"  #       [X] def [ ] assignment [ ] inside
p2 = "02_input_name.py"  #  [ ] def [X] assignment [ ] inside
p3 = "16_csv.py"  #         [X] def [X] assignment [ ] inside *
p4 = "12_classes.py"  #     [X] def [X] assignment [X] inside
base_2 = [p0, p1, p2, p3, p4]

# fmt: off
pipelines_2 = [
    ({    p1, p2, p3, p4}, [("include",     [holds_abstr, holds_assignment])]),
    ({p0,               }, [("exclude",     [holds_abstr, holds_assignment])]),
    ({    p1,           }, [("include all", [holds_abstr, lacks_assignment])]),
    ({p0,     p2, p3, p4}, [("exclude all", [holds_abstr, lacks_assignment])]),
    ({p0, p1,     p3, p4}, [("include",     [holds_abstr, lacks_assignment])]),
    ({        p2,       }, [("exclude",     [holds_abstr, lacks_assignment])]),
    ({p0, p1, p2,     p4}, [("include",     [holds_asg_in_sub, lacks_abstr, lacks_assignment])]),
    ({            p3    }, [("exclude",     [holds_asg_in_sub, lacks_abstr, lacks_assignment])]),
    ({                p4}, [("include",     [holds_asg_in_sub])]),
    ({p0, p1, p2, p3    }, [("exclude",     [holds_asg_in_sub])]),
    ({        p2, p3, p4}, [("include",     [holds_assignment])]),
    ({p0, p1,           }, [("exclude",     [holds_assignment])]),
    ({    p1,     p3, p4}, [("include",     [holds_abstr])]),
    ({p0,     p2,       }, [("exclude",     [holds_abstr])]),
    ({p0, p1,         p4}, [("include",     [holds_asg_in_sub, lacks_assignment])]),
    ({        p2, p3    }, [("exclude",     [holds_asg_in_sub, lacks_assignment])]),
    ({            p3, p4}, [("include all", [holds_abstr, holds_assignment])]),
    ({p0, p1, p2,       }, [("exclude all", [holds_abstr, holds_assignment])]),
    ({p0,             p4}, [("include",     [lacks_asg_or_sub, holds_asg_in_sub])]),
    ({    p1, p2, p3    }, [("exclude",     [lacks_asg_or_sub, holds_asg_in_sub])]),
    ({p0,     p2,     p4}, [("include",     [holds_asg_in_sub, lacks_abstr])]),
    ({    p1,     p3,   }, [("exclude",     [holds_asg_in_sub, lacks_abstr])]),
    ({        p2,     p4}, [("include",     [holds_asg_in_sub, lacks_abstr]),
                            ("exclude",     [lacks_asg_or_sub])]),
    ({p0, p1,     p3    }, [("include",     [holds_abstr, lacks_assignment]),
                            ("exclude",     [holds_asg_in_sub])]),
    ({    p1,         p4}, [("include",     [holds_asg_in_sub, lacks_assignment]),
                            ("exclude",     [lacks_asg_or_sub])]),
    ({p0,     p2, p3    }, [("include",     [holds_assignment, lacks_abstr]),
                            ("exclude",     [holds_asg_in_sub])]),
    ({    p1, p2,       }, [("include",     [holds_abstr, holds_assignment]),
                            ("exclude all", [holds_abstr, holds_assignment])]),
    ({p0,         p3, p4}, [("include",     [holds_abstr, lacks_assignment]),
                            ("exclude all", [holds_abstr, lacks_assignment])]),
    ({p0,         p3    }, [("include",     [holds_abstr, lacks_assignment]),
                            ("exclude all", [holds_abstr, lacks_assignment]),
                            ("exclude",     [holds_asg_in_sub])]),
    ({    p1, p2,     p4}, [("include",     [holds_asg_in_sub, lacks_abstr, lacks_assignment]),
                            ("exclude",     [lacks_asg_or_sub])]),
    ({p0, p1, p2, p3, p4}, []),
]
# fmt: on


@pytest.mark.parametrize("expected_programs, commands", pipelines_2)
def test_recommend_simple_programs_2(expected_programs, commands):
    rec = Recommendations(db)
    rec.run_pipeline(
        [{"operation": operation, "data": data} for (operation, data) in commands]
        + [{"operation": "include", "data": base_2}]
    )
    print(rec.selected_programs)
    assert rec.selected_programs == expected_programs


# extract_2 (start)
holds_parallel_tuple = "var/assignment/explicit/parallel"
holds_ordinary_tuple = ("type/sequence/tuple", "is not", "var/assignment/explicit/parallel")
lacks_parallel_tuple = ("meta/program", "not contains", "var/assignment/explicit/parallel")
p0 = "01_hello_world.py"  # [ ] ordinary tuple [ ] parallel tuple
p1 = "11_bottles.py"  #     [X] ordinary tuple [ ] parallel tuple
p2 = "04_fibonacci.py"  #   [ ] ordinary tuple [X] parallel tuple
p3 = "18_queens.py"  #      [X] ordinary tuple [X] parallel tuple
base_3 = [p0, p1, p2, p3]

# fmt: off
pipelines_3 = [
    ({        p2, p3}, [("include",     [holds_parallel_tuple])]),
    ({p0, p1,       }, [("exclude",     [holds_parallel_tuple])]),
    ({    p1,     p3}, [("include",     [holds_ordinary_tuple])]),
    ({p0,     p2,   }, [("exclude",     [holds_ordinary_tuple])]),
    ({    p1, p2, p3}, [("include",     [holds_parallel_tuple, holds_ordinary_tuple])]),
    ({p0,           }, [("exclude",     [holds_parallel_tuple, holds_ordinary_tuple])]),
    ({            p3}, [("include all", [holds_parallel_tuple, holds_ordinary_tuple])]),
    ({p0, p1, p2,   }, [("exclude all", [holds_parallel_tuple, holds_ordinary_tuple])]),
    ({p0, p1,     p3}, [("include",     [lacks_parallel_tuple, holds_ordinary_tuple])]),
    ({        p2,   }, [("exclude",     [lacks_parallel_tuple, holds_ordinary_tuple])]),
    ({    p1,       }, [("include all", [lacks_parallel_tuple, holds_ordinary_tuple])]),
    ({p0,     p2, p3}, [("exclude all", [lacks_parallel_tuple, holds_ordinary_tuple])]),
    ({p0,         p3}, [("include",     [lacks_parallel_tuple, holds_ordinary_tuple]),
                        ("exclude all", [lacks_parallel_tuple, holds_ordinary_tuple])]),
    ({    p1, p2,   }, [("include",     [holds_parallel_tuple, holds_ordinary_tuple]),
                        ("exclude all", [holds_parallel_tuple, holds_ordinary_tuple])]),
    ({p0, p1, p2, p3}, []),
]
# fmt: on
# extract_2 (stop)


@pytest.mark.parametrize("expected_programs, commands", pipelines_3)
def test_recommend_simple_programs_3(expected_programs, commands):
    rec = Recommendations(db)
    rec.run_pipeline(
        [{"operation": operation, "data": data} for (operation, data) in commands]
        + [{"operation": "include", "data": base_3}]
    )
    print(rec.selected_programs)
    assert rec.selected_programs == expected_programs


if __name__ == "__main__":
    pytest.main(["-qq", __import__("sys").argv[0]])
