from pathlib import Path
from typing import Counter as Bag
from typing import Dict, List, NamedTuple, NewType, Generic
from span import Span

# fmt: off

Source = NewType("Source", str)

LabelName = NewType("LabelName", str)
LabelNames = List[LabelName]
class Label(NamedTuple):
    name: LabelName
    spans: List[Span]
Labels = List[Label]
LabelsSpans = Dict[LabelName, List[Span]]

ProgramName = NewType("ProgramName", str)
ProgramNames = List[ProgramName]
class Program(NamedTuple):
    path: Path = Path("")
    source: Source = Source("")
    addition: LabelsSpans = {}
    deletion: LabelsSpans = {}
    labels: Labels = []

TaxonName = NewType("TaxonName", str)
TaxonNames = List[TaxonName]
class Taxon(NamedTuple):
    name: TaxonName
    spans: Bag[Span]
Taxons = List[Taxon]
TaxonsSpans = Dict[TaxonName, Bag[Span]]
class PathTaxons(NamedTuple):
    path: Path
    taxons: Taxons

# fmt:on
