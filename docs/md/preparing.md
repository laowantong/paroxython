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

### Other conventions

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

## Style

### Guards

Some guidelines and linters (e.g.,
[LLVM Coding Standards](https://llvm.org/docs/CodingStandards.html#don-t-use-else-after-a-return),
[Pylint](https://pheanex.github.io/pylint/),
[ESLint](https://eslint.org/docs/rules/no-else-return),
[TSLint](https://palantir.github.io/tslint/rules/unnecessary-else/))
warn that an `else` branch following a `return` statement “is not necessary and increases indentation level”.
Although this is technically true, our approach is more nuanced. Specifically, we recommend our students to use the “no else” style when the condition can be seen as a [guard](https://en.wikipedia.org/wiki/Guard_(computer_science)), i.e., a **pre-**condition to avoid failing, complicating or slowing down the main treatment of the subroutine:

```python
def is_prime(n):
    if n < 2: # avoid calculating the square root of a negative number
        return False
    if n == 2: # avoid returning a wrong result for 2
        return True
    if n % 2 == 0: # avoid wasting time in the loop
        return False
    # this is where the real work begins
    for candidate in range(3, int(sqrt(n) + 1), 2):
        if n % candidate == 0:
            return False
    return True
```

However, as noted [here](https://blog.mozilla.org/nnethercote/2009/08/31/no-else-after-return-considered-harmful/) or [here](https://dmerej.info/blog/post/else-after-return-yea-or-nay/), there are situations where applying the blanket rule would break an inherent symmetry in the treatment:

```python
def max_(a, b):
    if a >= b:
        return a
    else: # removing this branch would hurt readability
        return b
```

So, both styles have their uses. Consider choosing one as an opportunity to better communicate your intention[^swift_guard]. In any case, remember that Paroxython will try to tag every relevant `if` statement as `flow/conditional/guard` (see [here](https://repo/paroxython/resources/spec.md#feature-if_guard) for details on the heuristic).

[^swift_guard]:
    A modern language like Swift definitely clarifies this intention by making `guard` a keyword (since [2.0](https://www.appcoda.com/swift-2-introduction/)).


## Manual hints

On a given source code, the tagging algorithm may sometimes result in false positives or false negatives. Moreover, the semantics of some features may be subjective (e.g., `meta/topic/fun`) or beyond the capabilities of Paroxython (e.g., deciding the relevance of the `short_circuit` property of a boolean operator). In any case, the user has the possibility to manually tag certain lines of their source code to hint either the presence or absence of a given feature.

### Addition

The addition of one or several tags is hinted by a comment starting with `# paroxython:`.

#### Hinting with labels

A tag can be a label (of the kind defined, but not necessarily included in [spec.md](https://repo/paroxython/resources/spec.md)):

```python
if i < len(s) and s[i] == x: # paroxython: short_circuit:And
```

This is powerful: a label can be derived into several other labels, and then converted into any number of taxa (according to the mapping of [taxonomy.tsv](https://repo/paroxython/resources/taxonomy.tsv)). But it asks you to check the taxonomy to see how it will be converted.

#### Hinting directly with the final taxa

A tag can be a taxon (starting with a non-empty sequence of word characters and a slash):

```python
if i < len(s) and s[i] == x: # paroxython: operator/boolean/and/short_circuit
```

Hinting with a taxon is easier: you put it directly into the taxonomy. But sometimes you want more.

### Deletion

To delete a **label**, prefix it with a minus symbol. For instance, the following hint requalifies an addition into a string concatenation:

```python
print(a + b) # paroxython: -addition_operator +concatenation_operator
```

..warning::
    You cannot directly hint the deletion of a given **taxon**.

### Multiple lines

If a label should span over several lines, it is hinted on the first line with a `.​.​.` suffix (meaning “to be continued”), and on the last line with a `..​.​` prefix (meaning “continuing”). In the following example, a new label is manually substituted to the calculated label `loop:for`:

```python
for am in ifera: # paroxython:  -loop:for... +amoeboid_protist...
    catch()
    eat() # paroxython: ...loop:for ...amoeboid_protist
```

### Formatting details

Some tolerances exist for the syntax:

- `+` can be omitted.
- `..​.​` can be written `…` (HORIZONTAL ELLIPSIS, U+2026).
- `# paroxython:` is neither space- nor case-sensitive.

..warning::
    If you use a code formatter like [Black](https://github.com/psf/black), beware that it may reject a deletion hint after the line which features the label to be deleted. In this case, protect the line with `# fmt:off` and `# fmt:on`.

### Why would I do that?

On simple programs such as those found in programming education, the results of Paroxython are generally quite satisfactory. But the better the feature labelling, the better the recommendations. You will sometimes, hopefully not too often, feel the need to remove (`-`) some false positives or correct (`+`) some false negatives. There are, however, more interesting possibilities.

#### Adding metadata

Consider the following naive suboptimal solution to the general problem of deduplicating a given sequence:

```python
1   def unique_elements(sequence):
2       result = []
3       for x in sequence:
4           if sequence.count(x) == 1:
5               result.append(x)
6       return result
```

What if we take the trouble to give Paroxython some hints about what we meant by “naive”, “suboptimal” and “general”?

```python
1   def unique_elements(sequence):
2       result = []
3       for x in sequence: # paroxython: complexity:O(n) complexity:O(n^2)...
4           if sequence.count(x) == 1: # paroxython: complexity:O(n)
5               result.append(x) # paroxython: ...complexity:O(n^2)
6       return result
7   # paroxython: meta/level/naive complexity:suboptimal
8   # paroxython: topic:general
```

| Taxon | Lines |
|:--|:--|
| `meta/complexity/O(n)` | 3, 4 |
| `meta/complexity/O(n^2)` | 3-5 |
| `meta/complexity/suboptimal` | 1-8 |
| `meta/level/naive` | 1-8 |
| `meta/topic/general` | 1-8 |

Wow, this is handy. Let's break these comments down:

- We have pinpoint the lines featuring a linear operation: `for` and `count()`. The latter is not obvious for most students, and yes, that's the kind of thing you're going to have to repeat over and over again, unless you give up with high level languages like Python, and go back to C, assembler, Turing machines, Brainfuck, whatever.
- Nesting these two operations results in a quadratic complexity, which we have hinted by opening and closing a tag on the lines involved (3-5).
- As stated above, this approach is generally known as _naive_. No translation for a label `level:(.+)` is provided in the default taxonomy, so you hint directly at the desired taxon.
- Tagging the program as suboptimal, or as a counter-example, can be useful: when you are setting up an exam, you don't need to be recommended _bad_ programs, do you? With this kind of metadata, you can easily exclude all of them.
- Tagging your programs by topic is an alternative to distributing them in different folders, and is arguably better: when a program belongs to several topics, you don't have to bother with symlinks; and you are not stuck when you change your mind about the categorization (when, suddenly, you decide to classify your programs by technique: like _greedy_, _dynamic programming_, _divide and conquer_, etc.). By the way, remember you can always redirect the recommendations to `stdout`, and get a simple list of files. See `paroxython.cli.cli_recommend` for an example of how to copy them in another directory.

#### Duck hunting

Python famously thinks that:

> If it looks like a duck, swims like a duck, and quacks like a duck, then it is a duck.

This is called [duck typing](https://en.wikipedia.org/wiki/Duck_typing), and the reason why `unique_elements()` (above) would be happy with either a list, a tuple or a string: all of them sport the same methods, specifically `count()` (explicit) and `__iter__()` (implicit).

<center>
<figure class="image">
  <img src="https://regmedia.co.uk/2007/05/03/cartoon_duck.jpg" alt="A duck typing.">
  <figcaption><em>A duck typing on a typewriter, author<br>unknown, courtesy of <a url="https://stackoverflow.com/questions/289176/how-is-duck-typing-different-from-the-old-variant-type-and-or-interfaces">StackOverflow</a>.</em></figcaption>
</figure>
</center>

For us, this cute duck typing comes with a challenge. [As already explained](#beware-of-renaming-built-ins), Paroxython relies on the names of the methods and attributes to guess the type of the built-in objects. For instance, the default taxonomy has these two lines:

```plain
type/sequence/list	          member_call_method:(append|extend|insert|reverse|sort)
call/method/sequence/list/\1  member_call_method:(append|extend|insert|reverse|sort)
```

This is why the expression `foo.append(bar)` will be tagged `member_call_method:append` (label), and then `call/method/sequence/list/append` and `type/sequence/list` (taxa). Here, this technique increases our chances of finding programs that feature lists, but it does not achieve the same accuracy for `foo.count(bar)`: indeed, `count()` is shared by all sequential types. In the taxonomy, this comes down to:

```plain
type/sequence	                member_call_method:(count|index)
call/method/sequence_duck/\1	member_call_method:(count|index)
```

Did you spot the duck in the second row? It's there to tell you: “Quack! that's the best I can say, but in case this sequence can't actually be anything other than a list, just let me know.”

Well, ok. How to do this?

In fact, the taxonomy has two lines for that:

```plain
type/sequence/list	            member_call_method:list:(count|index|pop|...)
call/method/sequence/list/\1	member_call_method:list:(count|index|pop|...)
```

This means that you can hint at every ambiguous list method (`count()`, etc.) by
deleting the original label and adding a new one with an inserted `":list"`:

```python
a.count(b)  # paroxython: -member_call_method:count +member_call_method:list:count
```

Now, the generated taxa will be: `type/sequence/list` and `call/method/sequence/list/count`[^explicit_duck]. As for the duck, it is no more. It has ceased to be. It is expired and gone to meet its maker. It has run down the curtain and joined the choir invisible. This is an ex-duck.

[^explicit_duck]:
    For the similar cases where no translation is provided in the default taxonomy, you can either add it yourself, or directly hint at the desired  taxa, i.e., after `# paroxython:`, replace `+member_call_method:list:count` by `type/sequence/list` and `call/method/sequence/list/count`🦆.

Admittedly, all of this may be overkill, since a program featuring a list would most of the time feature it in several places, most of them without ambiguity. After all, generally speaking, you just want Paroxython to help you find programs in your repository, but don't need it to find features in a given program (you know better).

But if you feel like it, just fire up this 1 weird pipeline:

```python
{
    [
        "operation": "include",
        "data": [".+\bduck\b"],
    ]
}
```

... and happy duck hunting!
