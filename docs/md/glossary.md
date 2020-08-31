# Glossary

Inside a definition, the terms which have their own entry in the glossary are _italicized_.

**AST (flat —)**
:   The dump of an [Abstract Syntax Tree](https://en.wikipedia.org/wiki/Abstract_syntax_tree) as a sequence of text lines, each one consisting of the whole _path_ from the tree root to the current node, with some tweaks.

**Command**
:   A _pipeline_ _operation_, along with its _data_.

**Criterion** (plur. **criteria**)
:   Either a _taxon_ _pattern_, a program _pattern_ or a _semantic triple_.

**Data**
:   In a restricted sense, the second member of a _command_.

:   - If it is a string, it is interpreted as a shell command printing a list of program or _taxon_ _patterns_.
:   - If it is a list, each element is interpreted as a _criterion_.

**Hint (manual —)**
:   A comment that you may add in a _source_, either to fix a mislabelling problem, or to specify some metadata. It starts with `"# paroxython:` and can schedule either a _label_ or a _taxon_ for addition (by default) or deletion. Example:

        print(a + b) # paroxython: -addition_operator +concatenation_operator

**Label**
:   Name of a _feature_, as defined in `spec.md`. Examples:

:   - simple: `swap`, `if_else_branch`, `verbose_conditional_assignment`;
:   - with one variable suffix: `loop_with_return:for`, `import_module:foo`, `member_call_method:append`;
:   - with several variable suffixes: `member_call:bar:append`, `for_range:start:stop:-1`.

:   Comparison with _taxa_: the _taxa_ aim to represent concepts; _labels_, not so much. For instance, labelling `a = b` by `assignment:42` captures, in addition to the concept (assignment), an arbitrary piece of information (a name) which may or may not be internally used later to _label_ more complex _features_. Moreover, _taxa_ are structured into a _taxonomy_; _labels_ are free form.

**Operation**
:   A string among `"include"`, `"exclude"`, `"impart"` and `"hide"`, with an optional suffix `"any"` (implicit) or `"all"`.

**Path**
:   A continuous sequence of distinct edges from the root to a given node of a tree. Can be used for the _taxonomy_ or for the _flat AST_.

**Pattern**
:   A regular expression describing the name of a program, a _label_ or a _taxon_.

**Pipeline**
:   A list of filtering _commands_, expressed as a Python value and evaluated by `ast.literal_eval()`.

**Predicate**
:   Used in a restricted sense to denote the middle term of a _semantic triple_. It is a function taking two _poor spans_ `x` and `y` and telling whether they satisfy a certain relationship (for instance, “`x` after `y`”, or “`y` not inside `x`”).

**Source**
:   The text of a Python program of your collection.

**Span**
:   The location of a given _feature_, as the couple of its first and last lines. By extension, a third member, the _path_, identifies the beginning of the _feature_ in the AST.

**Span (poor —)**
:   A _span_ deprived from its last member.

**Tag**
:   Generic term, covering both _labels_ and _taxa_.

**Taxon** (plur. **taxa**)
:   Name of a _feature_, resulting from the conversion of a given _label_. Examples:

:   - the _label_ `swap` is converted to the _taxon_ `var/assignment/explicit/parallel/swap`;
:   - the _label_ `member_call_method:append` is converted to the _taxa_ `call/subroutine/method/sequence/list/append` and `type/sequence/list`.

:   A _taxon_ is a _path_ from a root to a node in the _taxonomy_. It represents a learning concept that should be of interest to the teacher.

**Taxonomy**
:   A forest structuring the learning concepts of the domain. The idea is that the concept represented by a node must be introduced _after_ its parent concept (if any).

**Triple (semantic —)**
:   Consists of a _taxon_ _pattern_ (the _subject_), a _predicate_ and an another _taxon_ _pattern_ (the _object_). Example: `("flow/conditional", "finished by", "def/subroutine/return")`.
