from pathlib import Path
from typing import Counter as Bag
from typing import Dict, List, NamedTuple, NewType, Set, Tuple

from typing_extensions import TypedDict  # Python 3.8: import directly from typing

from span import Span

# fmt: off


# Various types

Source = NewType("Source", str)
Query = NewType("Query", str)


# Labels

LabelName = NewType("LabelName", str)
LabelNames = List[LabelName]

class Label(NamedTuple):
    name: LabelName
    spans: List[Span]

Labels = List[Label]
LabelsSpans = Dict[LabelName, List[Span]]


# Taxons

TaxonName = NewType("TaxonName", str)
TaxonNames = List[TaxonName]
TaxonNameSet = Set[TaxonName]

class Taxon(NamedTuple):
    name: TaxonName
    spans: Bag[Span]

Taxons = List[Taxon]
TaxonsSpans = Dict[TaxonName, Bag[Span]]

class PathTaxons(NamedTuple):
    path: Path
    taxons: Taxons

TaxonPatterns = List[str]


# Programs

ProgramName = NewType("ProgramName", str)
ProgramNames = List[ProgramName]
ProgramNameSet = Set[ProgramName]

class Program(NamedTuple):
    path: Path = Path("")
    source: Source = Source("")
    addition: LabelsSpans = {}
    deletion: LabelsSpans = {}
    labels: Labels = []

ProgramPatterns = List[str]


# Serialization-ready types used for the JSON database

PoorSpan = Tuple[int, int]
LabelsPoorSpans = Dict[LabelName, List[PoorSpan]]
TaxonsPoorSpans = Dict[TaxonName, List[PoorSpan]]

class ProgramRecord(TypedDict):
    timestamp: str
    source: Source
    labels: LabelsPoorSpans
    taxons: TaxonsPoorSpans

ProgramInfos = Dict[ProgramName, ProgramRecord]
LabelInfos = Dict[LabelName, List[ProgramName]]
TaxonInfos = Dict[TaxonName, List[ProgramName]]

class JsonDatabase(TypedDict):
    programs: ProgramInfos
    labels: LabelInfos
    taxons: TaxonInfos


# Configuration dictionary

class Syllabus(TypedDict):
    path: str
    search_pattern: str
    finditer_pattern: str

class Configuration(TypedDict):
    input_path: str # A JSON database as produced by make_db.py
    output_path: str # The path for the recommendations in Markdown format
    syllabus: Syllabus
    cost_computation_strategy: str
    mandatory_taxon_patterns: List[str]
    excluded_program_patterns: List[str]
    excluded_taxon_patterns: List[str]


# fmt:on
