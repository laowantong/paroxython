"""Tag one Python file and output the table of its taxa or labels.

USAGE:
    ```
    paroxython tag [options] FILENAME
    ```

OPTIONS:
    ```plain
    -f --format=FORMAT  Format of the output, either "md" (Markdown)
                        or "tsv" (Tab Separated Values). [default: md]
    -l --labels         Output the labels instead of the taxa.
    -t --taxonomy=PATH  The path of a TSV file mapping labels onto taxa.
                        If not specified, use the included default taxonomy:
                        https://github.com/laowantong/paroxython/blob/0.7.0/paroxython/resources/taxonomy.tsv
    ```
"""

from pathlib import Path
from typing import List, Tuple, Optional
from typing_extensions import Literal

from .goodies import couple_to_string, print_exit
from .parse_program import ProgramParser
from .list_programs import get_program
from .map_taxonomy import Taxonomy
from .user_types import Source


def main(
    source: Source,
    tags: Literal["Taxon", "Label"] = "Taxon",
    relative_path: Path = Path("."),
    output_format: Literal["md", "tsv"] = "md",
    taxonomy_path: Optional[Path] = None,
) -> str:
    program = get_program(source, relative_path)
    parse = ProgramParser()
    program.labels[:] = parse(program)
    couples: List[Tuple[str, str]] = [(tags, "Lines")]
    if tags == "Label":
        for (label_name, label_spans) in sorted(program.labels):
            s = ", ".join(map(couple_to_string, sorted(label_spans)))
            couples.append((label_name, s))
    else:
        taxonomy = Taxonomy(taxonomy_path)
        taxa = taxonomy.to_taxa(program.labels)
        for (taxon_name, taxon_spans) in sorted(taxa):
            s = ", ".join(map(couple_to_string, sorted(taxon_spans.elements())))
            couples.append((taxon_name, s))
    if output_format == "md":
        result = [f"| `{tag}` | {lines} |" for (tag, lines) in couples]
        result[0] = result[0].replace("`", "")
        result[1:1] = ["|:--|:--|"]
    else:
        result = [f"{tag}\t{lines}" for (tag, lines) in couples]
    return "\n".join(result)


def cli_wrapper(args):
    path = Path(args["FILENAME"])
    try:
        source = path.read_text()
    except Exception as e:
        print_exit(str(e))
    result = main(
        source=Source(source),
        tags="Label" if args["--labels"] else "Taxon",
        relative_path=path.parent,
        output_format=args["--format"],
        taxonomy_path=Path(args["--taxonomy"]) if args["--taxonomy"] else None,
    )
    print(result)
