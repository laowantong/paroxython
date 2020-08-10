import pytest

import regex  # type: ignore

import context
from paroxython.goodies import couple_to_string
from paroxython.preprocess_source import collect_hints, HINT_COMMENT


def wrapper(numbered_hints):
    lines = [f"statement {i}" for i in range(1, 11)]
    for (i, hint) in numbered_hints:
        i -= 1  # lines start from 1, but indexes from 0
        if "paroxython" not in lines[i]:
            lines[i] += f" {HINT_COMMENT}"
        lines[i] += f" {hint}"
    (addition, deletion) = collect_hints("\n".join(lines))
    for operation in (addition, deletion):
        for (name, spans) in operation.items():
            operation[name] = ", ".join(map(couple_to_string, spans))
    return (addition, deletion)


def test_single_line_addition_hints():
    numbered_hints = [
        (3, "hint_on_2_and_3"),
        (2, "hint_on_2_and_3"),
        (3, "hint_on_3"),
        (4, "+hint_twice_on_4"),
        (4, "hint_twice_on_4"),
        (5, "looks/like/a/taxon"),
        (6, "_"),
        (6, "a"),
    ]
    (addition, deletion) = wrapper(numbered_hints)
    assert addition == {
        "hint_on_2_and_3": "2, 3",  # the spans are sorted
        "hint_on_3": "3",
        "hint_twice_on_4": "4, 4",  # duplicates are kept
        "looks/like/a/taxon": "5",  # taxons are kept
        "_": "6",
        "a": "6",
    }
    assert deletion == {}


def test_single_line_deletion_hints():
    numbered_hints = [
        (2, "-hint_on_2_and_3"),
        (3, "-hint_on_2_and_3"),
        (3, "-hint_on_3"),
        (4, "-hint_twice_on_4"),
        (4, "-hint_twice_on_4"),
    ]
    (addition, deletion) = wrapper(numbered_hints)
    assert addition == {}
    assert deletion == {
        "hint_on_2_and_3": "2, 3",
        "hint_on_3": "3",
        "hint_twice_on_4": "4, 4",  # the span is duplicated
    }


def test_single_line_addition_and_deletion_hints():
    numbered_hints = [
        (2, "hint_on_2"),
        (3, "+hint_on_3"),
        (3, "-hint_on_3"),
        (4, "-hint_on_4"),
        (5, "+hint_on_5"),
    ]
    (addition, deletion) = wrapper(numbered_hints)
    assert addition == {
        "hint_on_2": "2",
        "hint_on_3": "3",  # this label is both scheduled for addition
        "hint_on_5": "5",
    }
    assert deletion == {
        "hint_on_3": "3",  # ... and deletion
        "hint_on_4": "4",
    }


def test_multi_line_addition_hints():
    numbered_hints = [
        (2, "hint_from_2_to_8..."),
        (8, "...hint_from_2_to_8"),
        (3, "hint_from_3_to_8..."),
        (8, "...hint_from_3_to_8"),
        (5, "hint_from_5_to_9..."),
        (9, "...hint_from_5_to_9"),
    ]
    (addition, deletion) = wrapper(numbered_hints)
    print(addition)
    assert addition == {
        "hint_from_2_to_8": "2-8",
        "hint_from_3_to_8": "3-8",
        "hint_from_5_to_9": "5-9",
    }
    print(deletion)
    assert deletion == {}


def test_multi_line_nested_addition_hints():
    numbered_hints = [
        (2, "hint..."),  #       (
        (3, "hint..."),  #           (
        (4, "hint... ...hint"),  #       ()
        (5, "hint..."),  #               (
        (6, "...hint"),  #               )
        (7, "...hint"),  #           )
        (8, "...hint"),  #       )
    ]
    (addition, deletion) = wrapper(numbered_hints)
    print(addition)
    assert addition == {"hint": "2-8, 3-7, 4, 5-6"}
    print(deletion)
    assert deletion == {}


def test_multi_line_nested_deletion_hints():
    numbered_hints = [
        (2, "-hint..."),  #       (
        (3, "-hint..."),  #           (
        (4, "-hint... ...hint"),  #       ()
        (5, "-hint..."),  #               (
        (6, "...hint"),  #                )
        (7, "...hint"),  #            )
        (8, "...hint"),  #        )
    ]
    (addition, deletion) = wrapper(numbered_hints)
    print(addition)
    assert addition == {}
    print(deletion)
    assert deletion == {"hint": "2-8, 3-7, 4, 5-6"}


def test_multi_line_nested_addition_and_deletion_hints():
    numbered_hints = [
        (2, "-hint..."),  #       (-
        (3, "+hint..."),  #           (+
        (4, "-hint... ...hint"),  #       (-)-
        (5, "+hint..."),  #               (+
        (6, "...hint"),  #                )+
        (7, "...hint"),  #            )+
        (8, "...hint"),  #        )-
    ]
    (addition, deletion) = wrapper(numbered_hints)
    print(addition)
    assert addition == {"hint": "3-7, 5-6"}
    print(deletion)
    assert deletion == {"hint": "2-8, 4"}


def test_malformed_hints():
    hints = ["...", "..hint", ".hint", "@foobar"]
    for hint in hints:
        numbered_hints = [(2, hint)]
        with pytest.raises(ValueError, match=f"Malformed hint '{hint}' on line 2."):
            wrapper(numbered_hints)


def test_illegal_double_ellipsis():
    numbered_hints = [(2, "...hint...")]
    with pytest.raises(
        ValueError,
        match=regex.escape("Illegal last part for hint ('...', 'hint', '...') on line 2."),
    ):
        wrapper(numbered_hints)


def test_closing_without_opening():
    numbered_hints = [(2, "...hint")]
    with pytest.raises(
        ValueError, match=regex.escape("Unmatched closing hint ('...', 'hint', '') on line 2.")
    ):
        wrapper(numbered_hints)


def test_opening_without_closing():
    numbered_hints = [(2, "hint...")]
    with pytest.raises(ValueError, match=r"Unmatched opening hints for addition: .+'hint'.+2"):
        wrapper(numbered_hints)


if __name__ == "__main__":
    pytest.main(["-qq", __import__("sys").argv[0]])
