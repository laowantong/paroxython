from pathlib import Path

from label_programs import ProgramLabeller
from map_taxonomy import Taxonomy
from list_programs import get_program

from goodies import couple_to_string
from user_types import Source


def analyze_one(source: Source, tags: str = "Taxon", relative_path: Path = Path(".")) -> str:
    labeller = ProgramLabeller(relative_path)
    program = get_program(source, relative_path)
    labeller.label_program(program)
    result = []
    result.append(f"| {tags} | Lines |")
    result.append("|:------|:------|")
    if tags == "Label":
        for (label_name, label_spans) in sorted(program.labels):
            s = ", ".join(map(couple_to_string, sorted(label_spans)))
            result.append(f"| `{label_name}` | {s} |")
    else:
        taxonomy = Taxonomy()
        taxons = taxonomy.to_taxons(program.labels)
        for (taxon_name, taxon_spans) in sorted(taxons):
            s = ", ".join(map(couple_to_string, sorted(taxon_spans.elements())))
            result.append(f"| `{taxon_name}` | {s} |")
    return "\n".join(result)


if __name__ == "__main__":
    path = Path("../Algo/programs/gcd_4.py")
    source = Source(path.read_text())
    print(analyze_one(source))
