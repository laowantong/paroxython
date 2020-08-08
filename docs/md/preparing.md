# Preparing your program collection

## Naming things

### Capitalization

Paroxython takes advantage of the official [PEP 8 naming conventions](https://www.python.org/dev/peps/pep-0008/#naming-conventions). In a nutshell:

`lowercase_with_underscores`
:   Variables, functions (in the broadest sense, including methods), modules, packages.

`CapitalizedWords`
:   Classes, exceptions, [type variables](https://www.python.org/dev/peps/pep-0484/).

`ALL_CAPITAL_LETTERS_WITH_UNDERSCORES`
:   Constants, defined on a module level.

For example, with a careless style like this:

```python
def ComputeSquare(x): # bad: CamelCase for a function name
    return x * x

FOO = 42
FOO = ComputeSquare(FOO) # bad: redefinition of a constant
```

... Paroxython will wrongly detect two definitions of constants (`var/assignment/constant`) and the instanciation of a class (`call/class/constructor`). To make these false positives disappear, just write:


```python
def compute_square(x):
    return x * x

foo = 42
foo = compute_square(foo)
```

### Leading and trailing underscores

`_single_leading_underscore`
:   Weak “internal use” indicator.

`__double_leading_underscore`
:   Mangled non-public class attributes.

`single_trailing_underscore_`
:   Conflict-averse objects (avoiding a name collision with a keyword).

`__double_leading_and_trailing_underscore__`
:   "Magic" methods or attributes (never invent such names).

### Common sense conventions

When the name of a function returning a value starts with `"is_"`, `"are_"`, `"has_"`, `"have_"`, `"can_"`, `"must_"` or `"needs_"`, it is tagged as predicate (`"def/function/predicate"`):

```python
def is_even(n):
    return n % 2
```

When the name of a function returning nothing starts or ends with `"test"` or `"tests"`, it is tagged as test (`"def/procedure/test"`):

```python
def test_is_even():
    assert not is_even(42)
    assert is_even(5)
```

### Beware of renaming built-ins

It's never a good idea to reuse a [built-in function](https://docs.python.org/3/library/functions.html) name:

```python
max = 42 # bad: max() is a built-in function
```

In the same way, if you write classes, consider the names of the methods of the [built-in types](https://docs.python.org/3/library/stdtypes.html) as taboo. Paroxython relies on them to try guessing the type of objects to which they apply. For instance, in:

```python
def change_separator(s, old, new):
    return new.join(s.split(old))
```

... nothing indicates that `s` is a `type/sequence/string` except from the call of its method `split()`.

## Flow



## Manual hints

On a given source code, the labelling algorithm may sometimes produce false positives or false negatives. Moreover, the semantics of some features may be subjective (e.g., `topic:fun`) or beyond the capabilities of Paroxython (e.g., deciding the relevance of the `short_circuit` property of a boolean operator). In any case, the user has the possibility to manually label certain lines of their source code to hint either the presence or absence of a given feature.

The addition of a label is hinted by a comment starting with `# paroxython:`.

```python
if i < len(s) and s[i] == x: # paroxython: short_circuit:And
```

.. note::
	`short_circuit:And` is a **label** (of the kind defined, but not necessarily included in [spec.md](https://repo/paroxython/resources/spec.md)), but not a taxon. It will be later converted into one or more taxa (according to the mapping of [taxonomy.tsv](https://repo/paroxython/resources/taxonomy.tsv)).

To delete a label, prefix it with a minus symbol. For instance, the following hint requalifies an addition into a string concatenation:

```python
print(a + b) # paroxython: -addition_operator +concatenation_operator
```

If a label should span over several lines, it is hinted on the first line with a `.​.​.` suffix (meaning “to be continued”), and on the last line with a `..​.​` prefix (meaning “continuing”). In the following example, a new label is manually substituted to the calculated label `loop:for`:

```python
for am in ifera: # paroxython:  -loop:for... +amoeboid_protist...
    catch()
    eat() # paroxython: ...loop:for ...amoeboid_protist
```

Some tolerances exist for the syntax:

- `+` can be omitted.
- `..​.​` can be written `…` (HORIZONTAL ELLIPSIS, U+2026).
- `# paroxython:` is neither space- nor case-sensitive.
