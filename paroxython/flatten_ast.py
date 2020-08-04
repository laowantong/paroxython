r"""
Return a non-recursive, multiline dump of the AST (with some tweaks).

## Motivation and purpose

[Static analysis](https://en.wikipedia.org/wiki/Static_program_analysis) tools like Paroxython
generally start with the [AST](https://en.wikipedia.org/wiki/Abstract_syntax_tree) (abstract syntax
tree) of the program to analyze. For instance, when the string:

```python
'print("hello, world")'
```

... is fed to the function `ast3.parse()` of the module
[`typed_ast`](https://github.com/python/typed_ast), the following object is returned:

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

The purpose of the function `flatten_ast()` is to transform this nested structure into a
pre-ordered sequence of text lines, each of which consisting in a key-value pair. A key is the
complete path from the root of the AST to either a node (e.g., `Name()`) or a node attribute
(e.g., `id`). The associated value comes after an equals sign (`=`):

```plain
/_type=Module
/body/_length=1
/body/1/_type=Expr
/body/1/_pos=1:1-
/body/1/value/_type=Call
/body/1/value/_hash=0x00000001
/body/1/value/_pos=1:1-0-
/body/1/value/func/_type=Name
/body/1/value/func/_hash=0x00000002
/body/1/value/func/_pos=1:1-0-0-
/body/1/value/func/id=print
/body/1/value/func/ctx/_type=Load
/body/1/value/args/_length=1
/body/1/value/args/1/_type=Str
/body/1/value/args/1/_hash=0x00000003
/body/1/value/args/1/_pos=1:1-0-1-1-
/body/1/value/args/1/s=hello, world
/body/1/value/args/1/kind=
/body/1/value/keywords/_length=0
/type_ignores/_length=0
```

Obviously, such a representation is quite verbose. But it encapsulates in every single line the
whole nesting information we need to understand its context. Since the recursion is linearly
encoded, requesting it does not require recursion any more. This makes [regular
expressions](https://en.wikipedia.org/wiki/Regular_expression) a natural candidate for the request
language[^regex-recursion]. This is the choice we made for the present version of Paroxython. The
regular expression patterns are processed in `paroxython.parse_program` on the basis of the
definitions listed in
[`spec.md`](https://repo/paroxython/resources/spec.md).

[^regex-recursion]: Although nowadays, numerous flavours of regex engines support recursion,
the complexity of writing, reading and maintaining any pattern using it would quickly go through the
roof.

For instance, the following regular expression matches and localizes nested function calls (e.g.,
`foo(bar(42))`) without any recursion:

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

### Field reordering

Somewhat counterintuitively, in the original AST, several pieces of information pertaining to a
function signature or decoration are rejected _after_ the body of the function. As a result, we
lose the interesting property that the line numbers cannot decrease. We fix this by making `body`
the last field of a function definition
(see [issue #4](https://github.com/laowantong/paroxython/issues/4)).

### Children numbering

A counter is inserted between each node and its children. Starting from 1 makes possible to find
the last one by matching its number with the (previously captured) length of the list.

### Field disambiguation

Accross the AST, the same fields are sometimes used in different contexts. To make it easier or
even possible to detect certain features, their usage is disambiguated by applying the following
renaming rules:

- `orelse`: used for both loop and conditional `else` branches. Replace the former with `loopelse`.
- `target`: used for assignment, comprehension, etc. Replace the former with `assigntarget`.
- `targets`: used for augmented assignment, deletion, etc. Replace the former with `assigntargets`.
- `value`: used for assignment (augmented or not), comprehension, etc. Replace the former ones with
  `assignvalue`.

Thus, in the output, there is no more need to search for the context of a field in the previous or
following lines.

### Added fields

- `_type`: stores the name of the node (e.g., `Module`, `Expr`, `Call`).
- `_pos`: stores the line number (extracted from the attribute `lineno` of the node, if
  any[^lineno]), followed by a colon `:`, followed by the path from the root of the AST to this
  node. A path is coded as a sequence of positive integers, hyphen-separated and ended by a hyphen.
  Its fundamental property is: node \(n_2\) is nested within node \(n_1\) iff the path of \(n_1\)
  is a prefix of the path of \(n_2\).
- `_hash`: see next section.

[^lineno]: Numerous nodes, e.g. `Module`, `Store`, `Load`, `Lt`, `Add`, are not associated with a
    line number.

### Expression decontextualization and hashing

In order to detect certain features, such as
[`swap`](https://repo/paroxython/resources/spec.md#feature-swap):

```python
(a[i], a[j]) = (a[j], a[i])
```
... we need to recognize a given expression accross its different occurrences. The function
`typed_ast.ast3.dump()` is used for this. For instance, in the following statement:

```python
a[i] = 42
```

... the expression `a[i]` is dumped as the string:

```python
"Subscript(value=Name(id='a', ctx=Load()), slice=Index(value=Name(id='i', ctx=Load())), ctx=Store())"
```

However, in the following statement:

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
    merely increments a counter and associates it with any newly encountered string.

### Negative literal simplification

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
"""

from typed_ast import ast3 as ast
from typing import Any, Callable

import regex  # type: ignore


def flatten_ast(tree) -> str:
    """Return a non-recursive, multiline dump of the AST (with some tweaks).

    A simple wrapper around the recursive function `flatten_node`, with a call to
    `simplify_negative_literals` as post-processing.
    """
    pseudo_hash.reset()
    flat_ast = flatten_node(tree)
    flat_ast = simplify_negative_literals(flat_ast)
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
            result of `ast3.dump()`.
            [Not to be explicitly provided.](docs_developer_manual/index.html#default-argument-trick)
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
        if isinstance(node, ast.FunctionDef):
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
        # If the node is a terminal value, dump it unquoted
        return f"""{prefix}={repr(node).strip("'")}\n"""


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

    Argument `sub` [not to be explicitly provided.](docs_developer_manual/index.html#default-argument-trick)
    """
    return sub(r"\1/_type=Num\2\1/n=-\3", flat_ast)


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
