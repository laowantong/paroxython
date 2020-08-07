# Type hierarchy (https://python.readthedocs.io/en/stable/reference/datamodel.html)
#

from functools import reduce

type_hierarchy = """
number/integral/int
number/integral/bool
number/float
number/complex
sequence/immutable/string/str
sequence/immutable/string/bytes
sequence/immutable/tuple
sequence/mutable/list
sequence/mutable/bytearray
set_type/set
set_type/frozenset
dict
""".split()

type_names = "int bool float complex str tuple bytes list bytearray set frozenset dict".split(" ")
type_methods = {
    name: {s for s in dir(getattr(__builtins__, name)) if not s.startswith("__")}
    for name in type_names
}
print()

print(f"appli/function/builtin/casting/\\1<tab>free_call:({'|'.join(type_names)})")


def compute(suffix, names_1, names_2):
    set_1 = reduce(set.union, map(type_methods.get, names_1.split()))
    set_2 = set().union(*map(type_methods.get, names_2.split()))
    label_pattern = "|".join(sorted(set_1 - set_2))
    print(f"appli/method/{suffix}/\\1<tab>member_call:({label_pattern})")


compute("number", "int bool float complex", "str tuple bytes list bytearray set frozenset dict")
compute("sequence/string", "str", "tuple int bool float complex list set frozenset dict")
compute("sequence/list", "list", "str int bool float complex set frozenset dict")
compute("dict", "dict", "int bool float complex str tuple bytes list bytearray set frozenset")
compute("set", "set frozenset", "int bool float complex str tuple bytes list bytearray dict")
compute("sequence/list", "list str", "int bool float complex set frozenset dict")
