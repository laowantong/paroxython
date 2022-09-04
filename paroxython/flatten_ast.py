r"""
Return a non-recursive, multiline dump of the AST (with some tweaks).

## Motivation and purpose

[Static analysis](https://en.wikipedia.org/wiki/Static_program_analysis) tools like Paroxython
generally start with the [AST](https://en.wikipedia.org/wiki/Abstract_syntax_tree) (abstract syntax
tree) of the program to analyze. For instance, when the string:

```python
'print("hello, world")'
```

... is fed to the function `parse()` of the module [`ast`](https://docs.python.org/3/library/ast.html),
the following object is returned:

```plain
                           Module()
                              |
                              | body[0]
                              |
                            Expr()
                              |
                              | value
                              |
                            Call()
                             / \
                       func /   \ args[0]
                           /     \
Name(id='print', ctx=Load())     Str(s='hello, world', kind='')
```

The purpose of our function `flatten_ast()` is to transform this nested structure into a curated
pre-ordered sequence of text lines, each of which consisting in a key-value pair. A key is the
complete path from the root of the AST to either a node (e.g., `Name()`) or a node attribute
(e.g., `id`). The associated value comes after an equals sign (`=`):

```plain
/_type=Module
/body/_length=1
/body/1/_type=Expr
/body/1/_pos=1:1-
/body/1/value/_type=Call
/body/1/value/_hash=0x0001
/body/1/value/_pos=1:1-0-
/body/1/value/func/_type=Name
/body/1/value/func/_hash=0x0002
/body/1/value/func/_pos=1:1-0-0-
/body/1/value/func/id=print
/body/1/value/func/ctx/_type=Load
/body/1/value/args/_length=1
/body/1/value/args/1/_type=Str
/body/1/value/args/1/_hash=0x0003
/body/1/value/args/1/_pos=1:1-0-1-1-
/body/1/value/args/1/s=hello, world
/body/1/value/keywords/_length=0
/type_ignores/_length=0
```

Obviously, such a representation is quite verbose. But every single line encapsulates most of the
nesting information we need to understand its context. Since the recursion is linearly encoded,
requesting it does not require recursion any more. Thus,
[regular expressions](https://en.wikipedia.org/wiki/Regular_expression) become natural candidates
for the request language[^regex-recursion]. The current version of Paroxython explores this option.
The regular expression patterns are processed in `paroxython.parse_program` on the basis of the
definitions listed in `spec.md`.

[^regex-recursion]: Although nowadays, numerous flavours of regex engines support recursion,
the complexity of writing, reading and maintaining any pattern using it would quickly go through the
roof.

For instance, the following regular expression matches and localizes the nested function calls
(e.g., `foo(bar(42))`) without any recursion:

```re
           ^(.*)                    # Capture the path originating from the root...
                /_type=Call         #  ... to the nesting call.
\n(?:\1.+\n)*?\1                    # Skip any number of attributes of this call...
                /_pos=(?P<POS>.+)   # ... until we find and capture its line number.
\n(?:\1.+\n)* \1                    # Skip any number of...
                /args/.*            # ... arguments of this call...
                        /_type=Call # ... until we find a nested call.
```

When the first call is found, continuing in the subtree is a simple matter of restricting the search
to the block of lines that share the same prefix (referred by `\1`).

That's the general principle. In the next section, we enumerate the tweaks we make to the generation
of this text to make it more suitable for regular expression parsing.

## Implementation details

### On the fly: modification of the AST

#### Field reordering

Somewhat counterintuitively, in the original AST, several pieces of information pertaining to a
function signature or decoration are rejected _after_ the body of the function. As a result, we
lose the interesting property that the line numbers cannot decrease. We fix this by making `body`
the last field of a function or class definition
(see [issue #4](https://github.com/laowantong/paroxython/issues/4)).

#### Children numbering

A counter is inserted between each node and its children. Starting from 1 enables us to find the
last one by matching its number with the (previously captured) length of the list.

#### Field disambiguation

Accross the AST, the same fields are sometimes used in different contexts. To make it easier or
even possible to detect certain features, their usage is disambiguated by applying the following
renaming rules:

- `orelse`: used for both loop and conditional `else` branches. Replace the former with `loopelse`.
- `target`: used for assignment, comprehension, etc. Replace the former with `assigntarget`.
- `targets`: used for augmented assignment, deletion, etc. Replace the former with `assigntargets`.
- `value`: used for assignment (augmented or not), comprehension, assignment-expressions, etc.
  Replace the former ones with `assignvalue`.

Thus, in the output, there is no more need to search for the context of a field in the previous or
following lines.

#### Added fields

- `_type`: stores the name of the node (e.g., `Module`, `Expr`, `Call`).
- `_pos`: stores the line number (extracted from the attribute `lineno` of the node, if
  any[^lineno]), followed by a colon `:`, followed by the path from the root of the AST to this
  node. A path is coded as a sequence of positive integers, hyphen-separated and ended by a hyphen.
  Its fundamental property is: node \(n_2\) is nested within node \(n_1\) iff the path of \(n_1\)
  is a prefix of the path of \(n_2\).
- `_hash`: see next section.

[^lineno]: Numerous nodes, e.g. `Module`, `Store`, `Load`, `Lt`, `Add`, are not associated with a
    line number.

#### Expression decontextualization and hashing

In order to detect certain features, such as
[`swap`](https://repo/paroxython/resources/spec.md#feature-swap):

```python
(a[i], a[j]) = (a[j], a[i])
```
... we need to recognize a given expression accross its various occurrences. For this, we tweak the
output of the library function `ast.dump()`. For instance, in the following statement:

```python
a[i] = 42
```

... the expression `a[i]` is dumped as the string:

```python
"Subscript(value=Name(id='a', ctx=Load()), slice=Index(value=Name(id='i', ctx=Load())), ctx=Store())"
```

However, in:

```python
    return a[i]
```

... the same expression `a[i]` is dumped as the string:

```python
"Subscript(value=Name(id='a', ctx=Load()), slice=Index(value=Name(id='i', ctx=Load())), ctx=Load())"
```

As you can see, these two strings are not equal, due to the fact that the dump specifies not only
_which_ expressions are used, but _how_ they are used: this is the purpose of the field `ctx`. Once
this context is removed, both strings become:

```python
"Subscript(value=Name(id='a'), slice=Index(value=Name(id='i')))"
```

They can now be represented by the same hash value[^pseudo-hash], stored in the added field `_hash`.

[^pseudo-hash]:
    Actually, to avoid dealing with hash randomization in the unit tests, we use a function which
    merely increments a counter and associates it with any newly encountered string
    (see `PseudoHashFactory`).

### After the fact: modification of the flattened AST

#### Negative literal simplification

Normally, the AST structure of a numeric literal depends on its sign. For instance, 42 is parsed
as:
```python
Expr(value=Num(n=42))
```
... while -42 is parsed as:

```python
Expr(value=UnaryOp(op=USub(), operand=Num(n=42)))
```

To unify the further treatment of numbers, the function `simplify_negative_literals` post-processes
the generated flat representation to transform this kind of output:

```plain
/body/1/_type=Expr
/body/1/_pos=1:1-
/body/1/value/_type=UnaryOp
/body/1/value/_hash=0x0001
/body/1/value/_pos=1:1-0-
/body/1/value/op/_type=USub
/body/1/value/operand/_type=Num
/body/1/value/operand/_hash=0x0002
/body/1/value/operand/_pos=1:1-0-1-
/body/1/value/operand/n=42
```

into this one:

```plain
/body/1/_type=Expr
/body/1/_pos=1:1-
/body/1/value/_type=Num
/body/1/value/_hash=0x0001
/body/1/value/_pos=1:1-0-
/body/1/value/n=-42
```

#### Index simplification

Since Python 3.9, the class `ast.Index` is deprecated: simple indexes are represented by their value.

For instance, `a[42]` is parsed as:

```python
[...] slice=Constant(value=42) [...]
```

... instead of:

```python
[...] slice=Index(value=Constant(value=42))) [...]
```

To unify the further treatment of indexes, the function `simplify_indexes` post-processes the
generated flat representation to transform this kind of output:

```plain
/body/1/_type=Expr
/body/1/_pos=1:1-
/body/1/value/_type=Subscript
/body/1/value/_hash=0x0001
/body/1/value/_pos=1:1-0-
/body/1/value/value/_type=Name
/body/1/value/value/_hash=0x0002
/body/1/value/value/_pos=1:1-0-0-
/body/1/value/value/id=a
/body/1/value/value/ctx/_type=Load
/body/1/value/slice/_type=Index           # Line to be suppressed.
/body/1/value/slice/value/_type=Num       # Lines to be simplified...
/body/1/value/slice/value/_hash=0x0003    # ...
/body/1/value/slice/value/_pos=1:1-0-1-0- # ...
/body/1/value/slice/value/n=42            # ...
/body/1/value/ctx/_type=Load
```

into this one:

```plain
/body/1/_type=Expr
/body/1/_pos=1:1-
/body/1/value/_type=Subscript
/body/1/value/_hash=0x0001
/body/1/value/_pos=1:1-0-
/body/1/value/value/_type=Name
/body/1/value/value/_hash=0x0002
/body/1/value/value/_pos=1:1-0-0-
/body/1/value/value/id=a
/body/1/value/value/ctx/_type=Load
/body/1/value/slice/_type=Num        # Simplified lines...
/body/1/value/slice/_hash=0x0003     # ...
/body/1/value/slice/_pos=1:1-0-1-    # ... (the last segment of the path is dropped)
/body/1/value/slice/n=42             # ...
/body/1/value/ctx/_type=Load
```

#### Suppressing useless lines

- Starting with Python 3.8, `kind` is an attribute of a constant allowing tools to distinguish
certain flavors of the strings . Its possible values are `"rf"`, `"f"`, `"u"` and `""` in the
third-party library `typed_ast`, but `"u"` and `None` in the Python 3.8 standard library `ast`.
Since such details are of no interest to us, we don't bother making them consistent. The function
`suppress_kinds` deletes from the flat AST any line ending with `kind=.*`.
- Python 3.8 introduces [positional-only parameters](https://www.python.org/dev/peps/pep-0570/)
to respond to “certain challenges for library authors and users of APIs”. This is far beyond our
pedagogical scope: we are afraid we have no choice but to sell these lines for scientific
experiments (`suppress_posonlyargs`).

#### Reverting the representation of constants to the good ol' days

Probably for excellent reasons, Python 3.8 has decided that `Num(n)`, `Str(s)`, `Bytes(s)`,
`Ellipsis` and `NameConstant(value)` should all be unified under `Constant(value)`. As far as we
are concerned, this change makes the type of the constants much harder to determine. Until we
know more, we are restoring the previous representations with `backport_all_constants`.

#### Unquoting strings

`unquote()` suppress the single or double quotes delimiters after `=`. This makes for simpler regular
expressions in `spec.md`.

#### Correcting the span of decorated callable

`correct_all_decorated_callable_starts()` fixes a bug of `typed_ast` in which decorated functions
and classes would incorrectly be marked as starting from the line of their first decorator.
"""


import ast
import sys
from typing import Any, Callable, Match

import regex  # type: ignore


def select_ast_post_processing():
    """Customize the post-treatment of the AST depending on the parser used to create it."""

    if sys.version_info >= (3, 10):

        def post_process(flat_ast):
            flat_ast = suppress_kinds(flat_ast)
            flat_ast = suppress_alias_pos(flat_ast)
            flat_ast = suppress_posonlyargs(flat_ast)
            flat_ast = backport_all_constants(flat_ast)
            flat_ast = simplify_negative_literals(flat_ast)
            flat_ast = unquote(flat_ast)
            return flat_ast

    elif sys.version_info >= (3, 9):

        def post_process(flat_ast):
            flat_ast = suppress_kinds(flat_ast)
            flat_ast = suppress_posonlyargs(flat_ast)
            flat_ast = backport_all_constants(flat_ast)
            flat_ast = simplify_negative_literals(flat_ast)
            flat_ast = unquote(flat_ast)
            return flat_ast

    else:

        def post_process(flat_ast):
            flat_ast = suppress_kinds(flat_ast)
            flat_ast = suppress_posonlyargs(flat_ast)
            flat_ast = backport_all_constants(flat_ast)
            flat_ast = simplify_negative_literals(flat_ast)
            flat_ast = simplify_indexes(flat_ast)
            flat_ast = unquote(flat_ast)
            return flat_ast

    return post_process


post_process = select_ast_post_processing()


def flatten_ast(tree) -> str:
    """Return a non-recursive, multiline dump of the AST (with some tweaks).

    A simple wrapper around the recursive function `flatten_node`, with post-processing treatments
    depending on the AST library (either the standard `ast` module or the third-party `typed_ast`).
    """
    pseudo_hash.reset()
    flat_ast = flatten_node(tree)
    flat_ast = post_process(flat_ast)
    return flat_ast


def flatten_node(
    node: Any,
    prefix: str = "",
    path: str = "",
    remove_context: Callable = regex.compile(r", ctx=.+?\(\)").sub,
) -> str:
    r"""Traverse recursively (in pre-order) the given AST node and flatten its subtree.

    Args:
        node (Any): The node to traverse. Initially, the whole AST.
        prefix (str, optional): The prefix of the current line to dump. Defaults to `""`.
        path (str, optional): The path of the current node. Defaults to `""`.
        remove_context (Callable, optional): A function removing the node context encoded in the
            result of `ast.dump()`.
            [Not to be explicitly provided.](developer_manual/index.html#default-argument-trick)
            Defaults to `regex.compile(r", ctx=.+?\(\)").sub`.

    Returns:
        str: A flat representation of the given node.
    """
    if isinstance(node, ast.AST):
        acc = [f"{prefix}/_type={type(node).__name__}\n"]
        if isinstance(node, ast.expr):
            node_repr = remove_context("", ast.dump(node))
            acc.append(f"{prefix}/_hash={pseudo_hash(node_repr)}\n")
        if "lineno" in node._attributes:
            acc.append(f"{prefix}/_pos={node.lineno}:{path[2:]}\n")
        fields = ast.iter_fields(node)
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            # make `body` the last item of a `def` clause
            fields = iter(sorted(fields, key=lambda c: c[0] == "body"))
        for (i, (name, x)) in enumerate(fields):
            if name == "orelse" and isinstance(node, (ast.For, ast.While, ast.AsyncFor)):
                name = "loopelse"  # make the `orelse` clause specific to conditionals
            elif name == "targets" and isinstance(node, ast.Assign):
                name = "assigntargets"  # `targets` is also used for `Delete`, etc.
            elif name == "target" and isinstance(node, ast.AugAssign):
                name = "assigntarget"  # `target` is also used for comprehension, etc.
            elif name == "value" and isinstance(node, (ast.Assign, ast.AugAssign)):
                name = "assignvalue"  # `value` is also used for comprehension, etc.
            acc.append(flatten_node(x, f"{prefix}/{name}", f"{path}{i}-"))
        return "".join(acc)
    elif isinstance(node, list):
        acc = [f"{prefix}/_length={len(node)}\n"]
        for (i, x) in enumerate(node, 1):  # number the children from 1
            acc.append(flatten_node(x, f"{prefix}/{i}", f"{path}{i}-"))
        return "".join(acc)
    else:
        # If the node is a terminal value, dump it
        return f"""{prefix}={repr(node)}\n"""


def simplify_negative_literals(
    flat_ast: str,
    sub: Callable = regex.compile(
        r"""(?mx)
                      ^(.*?)/_type=UnaryOp
            (\n(?:.+\n)*?)\1/op/_type=USub
             \n(?:.+\n)*? \1/operand/n=(.+)
        """
    ).sub,
) -> str:
    """[Simplify the negative literals](#negative-literal-simplification) of a given flat AST.

    Argument `sub` [not to be explicitly provided.](developer_manual/index.html#default-argument-trick)
    """
    return sub(r"\1/_type=Num\2\1/n=-\3", flat_ast)


def simplify_indexes(
    flat_ast: str,
    subn_index: Callable = regex.compile(r"(?m)^(.*?)/_type=Index\n").subn,
    sub_slice_value_pos: Callable = regex.compile(r"(?m)^([^=]*/slice/value/_pos=.+)\d+-").sub,
    sub_slice_value: Callable = regex.compile(r"(?m)^([^=]*/slice)/value").sub,
) -> str:
    """[Simplify the indexes](#index-simplification) of a given flat AST.

    Argument `sub` [not to be explicitly provided.](developer_manual/index.html#default-argument-trick)
    """
    (flat_ast, n) = subn_index("", flat_ast)
    if n == 0:
        return flat_ast
    flat_ast = sub_slice_value_pos(r"\1", flat_ast)
    return sub_slice_value(r"\1", flat_ast)


def backport_all_constants(
    flat_ast: str,
    sub: Callable = regex.compile(
        r"""(?mx)
            ^(.*?)/_type=Constant
            ((?:\n.+)+)
              \n\1/value=(.+)
        """
    ).sub,
) -> str:
    """Restore the more detailed representation of constants used before Python 3.8.

    Argument `sub` [not to be explicitly provided.](developer_manual/index.html#default-argument-trick)
    """
    return sub(replace_one_constant, flat_ast)


def replace_one_constant(m: Match) -> str:
    """Define the replacement function used in `backport_all_constants`."""
    if m[3].startswith(("'", '"')):
        return f"{m[1]}/_type=Str{m[2]}\n{m[1]}/s={m[3]}"
    elif m[3] in ("True", "False", "None"):
        return f"{m[1]}/_type=NameConstant{m[2]}\n{m[1]}/value={m[3]}"
    if m[3].startswith("b'"):
        return f"{m[1]}/_type=Bytes{m[2]}\n{m[1]}/s={m[3]}"
    if m[3] == "Ellipsis":
        return f"{m[1]}/_type=Ellipsis{m[2]}"
    else:
        return f"{m[1]}/_type=Num{m[2]}\n{m[1]}/n={m[3]}"


def correct_all_decorated_callable_starts(
    flat_ast: str,
    sub: Callable = regex.compile(
        r"""(?mx)
                     ^(.*?)/_type=(FunctionDef|ClassDef)
            (\n(?:.+\n)*?\1/_pos=)\d+:(.*
            \n(?:.+\n)*?\1/decorator_list/_length=([^0]\d*)
            \n(?:.+\n)*?\1/decorator_list/1/_pos=(\d+))
        """
    ).sub,
) -> str:
    """Make the span of a decorated callable starting from `def`, not from the first decorator.

    ..note::
        The bug is present in the third-party module `typed_ast`, but fixed in Python 3.8's standard
        library `ast`.

    Argument `sub` [not to be explicitly provided.](developer_manual/index.html#default-argument-trick)
    """
    return sub(replace_one_decorated_callable_start, flat_ast)


def replace_one_decorated_callable_start(m: Match) -> str:
    """Define the replacement function used in `correct_all_decorated_callable_starts`."""
    start = int(m[5]) + int(m[6])  # number of decorators + line number of the first decorator
    return f"{m[1]}/_type={m[2]}{m[3]}{start}:{m[4]}"


def unquote(
    flat_ast: str,
    sub: Callable = regex.compile(r"""=["'](.*)['"]\n""").sub,
) -> str:
    """Suppress the quote delimiters after “=“ to simplify the regular expressions of `spec.md`.

    Argument `sub` [not to be explicitly provided.](developer_manual/index.html#default-argument-trick)
    """
    return sub(r"=\1\n", flat_ast)


def suppress_kinds(
    flat_ast: str,
    sub: Callable = regex.compile(r"(?m)^.+/kind=.*\n").sub,
) -> str:
    """Suppress all leaves containing `/kind=`. They are useless in the following.

    Argument `sub` [not to be explicitly provided.](developer_manual/index.html#default-argument-trick)
    """
    return sub("", flat_ast)


def suppress_alias_pos(
    flat_ast: str,
    sub: Callable = regex.compile(r"(?m)^(.+/_type=alias\n).+_pos=.+\n").sub,
) -> str:
    """Suppress the AST line following import aliases. Since Python 3.10, it contains a position,
    useless in the following.

    Argument `sub` [not to be explicitly provided.](developer_manual/index.html#default-argument-trick)
    """
    return sub(r"\1", flat_ast)


def suppress_posonlyargs(
    flat_ast: str,
    sub: Callable = regex.compile(r"(?m)^.+/args/posonlyargs/_length=\d+\n").sub,
) -> str:
    """Suppress positional-only parameters in function definitions.

    Argument `sub` [not to be explicitly provided.](developer_manual/index.html#default-argument-trick)
    """
    return sub("", flat_ast)


__pdoc__ = {"PseudoHashFactory.__call__": True}


class PseudoHashFactory:
    """A factory that creates a deterministic replacement for the `hash()` builtin function."""

    def __init__(self):
        self.reset()

    def reset(self):
        """Restart the global counter and empties the cache."""
        self.i = 0
        self.cache = {}

    def __call__(self, x):
        """Return a 4-digits hexadecimal identifier for the given immutable value."""
        if x not in self.cache:
            self.i += 1
            self.cache[x] = f"0x{self.i:04x}"
            # 4.294.967.296 distinct expressions per program ought to be enough for anybody.
        return self.cache[x]


pseudo_hash = PseudoHashFactory()

if __name__ == "__main__":
    Path = __import__("pathlib").Path
    source = Path("sandbox/source.py").read_text()
    print(flatten_ast(ast.parse(source)))
