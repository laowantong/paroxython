from datetime import datetime
from itertools import permutations, product
from pathlib import Path

result = [
    f"""\
# Generated by helpers/make_compare_spans.py on {datetime.now()}.
# Changes to this file may cause incorrect behavior and will be lost if the code is regenerated.
"""
]
result.append("compare_spans = {")
for (b1, b2, b3, b4) in sorted(set(permutations("xxyy", 4))):
    for (o1, o2, o3) in product("<≤=", repeat=3):
        septuplet = (b1, o1, b2, o2, b3, o3, b4)
        key = "".join(septuplet)
        expression = " ".join(septuplet)
        expression = expression.replace("=", "==")
        expression = expression.replace("≤", "<=")
        expression = expression.replace("x", "a[0]", 1).replace("x", "a[1]").replace("a", "x")
        expression = expression.replace("y", "b[0]", 1).replace("y", "b[1]").replace("b", "y")
        line = f'    "{key}": lambda x, y: {expression},'
        result.append(line)
result.append("}")
result.append(
    """
# Translate the 13 Allen's interval algebra relations, with all inequalities regarded as inclusive.
#
# Cf. Fig. 4 of Allen, James F. (26 Nov. 1983). "Maintaining knowledge about temporal intervals".
# Communications of the ACM. 26 (11): 832–843. doi:10.1145/182.358434
# http://cse.unl.edu/~choueiry/Documents/Allen-CACM1983.pdf

compare_spans.update(
    {  #                                              Allen's symbols
        "equals": compare_spans["x=y≤x=y"],  #             =
        "starts": compare_spans["x=y≤x≤y"],  #             s
        "during": compare_spans["y≤x≤x≤y"],  #             d
        "finishes": compare_spans["y≤x≤x=y"],  #           f
        "before": compare_spans["x≤x≤y≤y"],  #             <
        "meets": compare_spans["x≤x=y≤y"],  #              m
        "overlaps": compare_spans["x≤y≤x≤y"],  #           o
        "started by": compare_spans["y=x≤y≤x"],  #         si
        "contains": compare_spans["x≤y≤y≤x"],  #           di
        "finished by": compare_spans["x≤y≤y=x"],  #        fi
        "after": compare_spans["y≤y≤x≤x"],  #              >
        "met by": compare_spans["y≤y=x≤x"],  #             mi
        "overlapped by": compare_spans["y≤x≤y≤x"],  #      oi
    }
)

# Add some extra synonyms.

compare_spans.update(
    {
        "ended by": compare_spans["finished by"],
        "ends": compare_spans["finishes"],
        "equal": compare_spans["equals"],
        "in": compare_spans["during"],
        "inside": compare_spans["during"],
        "is": compare_spans["equals"],
    }
)
"""
)

Path("paroxython/compare_spans.py").write_text("\n".join(result))
