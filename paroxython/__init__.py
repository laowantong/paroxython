"""
# Will you ever read me?

.. include:: ../README.md
   :start-after: </p>
   :end-before: # Read them

<br>

.. include:: ../docs/md/about.md

*[AST]: Abstract Syntax Tree
*[SQL]: Structured Query Language
*[TSV]: Tab Separated Values
*[JSON]: JavaScript Object Notation
*[SLOC]: Source Lines Of Code
"""

import sys
import pkg_resources

try:
    PAROXYTHON_VERSION = pkg_resources.get_distribution("paroxython").version
except pkg_resources.DistributionNotFound:
    PAROXYTHON_VERSION = "(unknown version)"  # For tests during CI

if "ipykernel" in sys.modules:
    # Declare the magic stuff paroxython iff the module is loaded as an IPython extension.

    from IPython.core.magic import Magics, cell_magic, magics_class  # type: ignore
    from IPython.display import Markdown, display  # type: ignore

    from .cli_tag import main

    def load_ipython_extension(ipython):
        ipython.register_magics(ParoxythonMagics)
        print(f"Paroxython {PAROXYTHON_VERSION} loaded.")

    @magics_class
    class ParoxythonMagics(Magics):
        @staticmethod
        @cell_magic
        def paroxython(line, cell=""):
            """
            Tag a Python code cell and output the table of its taxa or labels.

            In cell mode:
                %%paroxython [labels] [raw]
                ... Python cell code ...
            """
            args = set(line.lower().split())
            tags = "Label" if args.intersection(["label", "labels"]) else "Taxon"
            cell = f"# Compensate the offset of the magic command.\n{cell}"
            try:
                result = main(cell, tags=tags)
            except ValueError as e:
                print(e, file=sys.stderr)
            else:
                if "raw" in args:
                    print(result)
                else:
                    display(Markdown(result))
