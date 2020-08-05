"""
# Will you ever read me?

.. include:: ../README.md
   :start-after: logo.png)
   :end-before: ## Further reading

<br>

# [User manual](docs_user_manual/index.html)

# [Developer manual](docs_developer_manual/index.html)

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
