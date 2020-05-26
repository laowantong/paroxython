"""
.. include:: ../README.md
   :start-after: ![](docs/resources/logo.png)
   :end-before: # Documentation

<br>

# How it works

.. image:: resources/flow.png

# Pattern specifications

Browse [spec.md](https://github.com/laowantong/paroxython/blob/master/paroxython/resources/spec.md) on GitHub.

# Default Taxonomy

Browse [taxonomy.tsv](https://github.com/laowantong/paroxython/blob/master/paroxython/resources/taxonomy.tsv) on GitHub.

# User types

Paroxython makes heavy use of Python 3.5+ [type hints](https://docs.python.org/3/library/typing.html).
They are documented directly in the source code.
Browse [user_types.py](https://github.com/laowantong/paroxython/blob/master/paroxython/user_types.py) on GitHub.

# Glossary

- Hint:
- Label:
- Span:
- Tag:
- Taxon:
- Taxonomy:
"""


import sys

if "ipykernel" in sys.modules:
    # Declare the magic stuff paroxython iff the module is loaded as an IPython extension.

    from IPython.core.magic import Magics, line_cell_magic, magics_class  # type: ignore
    from IPython.display import Markdown, display  # type: ignore

    from .cli.cli_tag import main

    def load_ipython_extension(ipython):
        ipython.register_magics(ParoxythonMagics)

    @magics_class
    class ParoxythonMagics(Magics):
        @line_cell_magic
        def paroxython(self, line, source=None):
            """
            Tag a Python code cell and output the table of its taxons or labels.

            In cell mode:
                %%paroxython [labels] [raw]
                ... Python source code ...
            """
            if source:
                args = set(line.lower().split())
                tags = "Label" if args.intersection(["label", "labels"]) else "Taxon"
                source = f"# Compensate the offset of the magic command.\n{source}"
                result = main(source, tags=tags)
                if "raw" in args:
                    print(result)
                else:
                    display(Markdown(result))
