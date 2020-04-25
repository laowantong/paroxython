from IPython.core.magic import Magics, line_cell_magic, magics_class  # type: ignore
from IPython.display import Markdown, display  # type: ignore

import sys

if sys.path[0] != "paroxython":
    sys.path[0:0] = ["paroxython"]

from analyze_one import analyze_one


def load_ipython_extension(ipython):
    ipython.register_magics(ParoxythonMagics)


@magics_class
class ParoxythonMagics(Magics):
    @line_cell_magic
    def paroxython(self, line, source=None):
        """
        Tag a program.

        In cell mode:
            %%paroxython [labels]
            ... Python source code ...
        """
        if source:
            args = set(line.lower().split())
            tags = "Label" if args.intersection(["label", "labels"]) else "Taxon"
            source = f"# Compensate the offset of the magic command.\n{source}"
            display(Markdown(analyze_one(source, tags)))
