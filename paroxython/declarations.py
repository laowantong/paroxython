from pathlib import Path
from typing import Counter as Bag
from typing import Dict, List, NamedTuple, NewType

from span import Span

SourceText = NewType("SourceText", str)

ProgramName = NewType("ProgramName", str)
ProgramNames = List[ProgramName]
Program = NamedTuple("Program", [("path", Path), ("source", SourceText)])
Programs = List[Program]

LabelName = NewType("LabelName", str)
LabelNames = List[LabelName]
Label = NamedTuple("Label", [("name", LabelName), ("span", List[Span])])
Labels = List[Label]
LabelsSpans = Dict[LabelName, List[Span]]
PathLabels = NamedTuple("PathLabels", [("path", Path), ("labels", Labels)])

TaxonName = NewType("TaxonName", str)
TaxonNames = List[TaxonName]
Taxon = NamedTuple("Taxon", [("name", TaxonName), ("span_bag", Bag[Span])])
Taxons = List[Taxon]
TaxonsSpans = Dict[TaxonName, Bag[Span]]
PathTaxons = NamedTuple("PathTaxons", [("path", Path), ("taxons", Taxons)])
