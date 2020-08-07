# Manual hints

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
