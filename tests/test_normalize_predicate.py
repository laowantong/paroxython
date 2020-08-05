import pytest

import context
from paroxython.normalize_predicate import normalize_predicate
from paroxython.compare_spans import compare_spans

NEGATED = True
POSITIVE = False

working_examples = [
    ("is after", "y≤y≤x≤x", POSITIVE),
    ("is after", "after", POSITIVE),
    ("!is after", "after", NEGATED),
    ("! is after", "after", NEGATED),
    ("not is after", "after", NEGATED),
    ("is not after", "after", NEGATED),
    ("is after not", "after", NEGATED),
    ("IS AFTER", "after", POSITIVE),
    ("  IS AFTER  ", "after", POSITIVE),
    ("is", "x=y≤x=y", POSITIVE),
    ("is not", "x=y≤x=y", NEGATED),
    ("x=y", "x=y≤x=y", POSITIVE),
    ("x=y≤y", "x≤x=y≤y", POSITIVE),
    ("x≤x=y", "x≤x=y≤y", POSITIVE),
    ("y≤x", "y≤y≤x≤x", POSITIVE),
    ("x<=x=y<=y", "x≤x=y≤y", POSITIVE),
    ("x≤x==y≤y", "x≤x=y≤y", POSITIVE),
    ("x<=x==y<=y", "x≤x=y≤y", POSITIVE),
    ("(x ≤ x) == (y ≤ y)", "x≤x=y≤y", POSITIVE),
    ("(x1 ≤ x2) == (y1 ≤ y2)", "x≤x=y≤y", POSITIVE),
    ("(x2 ≤ x1) == (y2 ≤ y1)", "x≤x=y≤y", POSITIVE),
]


@pytest.mark.parametrize("original, normalized, negated", working_examples)
def test_normalize_predicate(original, normalized, negated):
    assert normalize_predicate(original) == (compare_spans[normalized], negated)


non_working_examples = [
    "is  after",
    "notis after",
    "foobar",
    "is after_not",
    "x≤x≤x=y",  # three x's
    "x>y",  # write "x<y" instead
]


@pytest.mark.parametrize("original", non_working_examples)
def test_fail_to_normalize_predicate(original):
    with pytest.raises(ValueError):
        normalize_predicate(original)


if __name__ == "__main__":
    pytest.main(["-qq", __import__("sys").argv[0]])
