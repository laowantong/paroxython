"""
# Will you ever read me?

.. include:: ../README.md
   :start-after: logo.png)
   :end-before: ## Further reading

<br>

# [User manual](docs_user_manual/index.html)

# [Developer manual](docs_developer_manual/index.html)

# About

## What's in a name?

Far from being an arbitrary label, “Paroxython” can be justified as follows:

1. It features both “Python” and “taxon”.
2. According to Merriam-Webster, “paroxytone” denotes a word accented or stressed on the penult.
3. “Paroxytone” translates as “paroxyton” in my mother tongue, and I fart in your general direction.
"""


import sys
import pkg_resources

try:
    PAROXYTHON_VERSION = pkg_resources.get_distribution("paroxython").version
except pkg_resources.DistributionNotFound:
    PAROXYTHON_VERSION = "(unknown version)"  # For tests during CI

if "ipykernel" in sys.modules:
    # Declare the magic stuff paroxython iff the module is loaded as an IPython extension.

    from IPython.core.magic import Magics, line_cell_magic, magics_class  # type: ignore
    from IPython.display import Markdown, display  # type: ignore

    from .cli.cli_tag import main

    def load_ipython_extension(ipython):
        ipython.register_magics(ParoxythonMagics)
        print(f"Paroxython {PAROXYTHON_VERSION} loaded.")

    @magics_class
    class ParoxythonMagics(Magics):
        @staticmethod
        @line_cell_magic
        def paroxython(line, source=None):
            """
            Tag a Python code cell and output the table of its taxa or labels.

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
