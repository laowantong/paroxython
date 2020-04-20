from typing import Counter as Bag
from typing import Dict, List, NamedTuple, NewType, Set, Tuple, Union

from typing_extensions import TypedDict, Literal  # Python 3.8: import directly from typing

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

TaxonPatterns = List[str]


# Programs

ProgramName = NewType("ProgramName", str)
ProgramNames = List[ProgramName]
ProgramNameSet = Set[ProgramName]

class Program(NamedTuple):
    name: ProgramName = ProgramName("")
    source: Source = Source("")
    addition: LabelsSpans = {}
    deletion: LabelsSpans = {}
    labels: Labels = []
    links: ProgramNames = []

Programs = List[Program]
ProgramTaxons = Dict[ProgramName, Taxons]

ProgramPatterns = List[str]

# Serialization-ready types used for the JSON database

PoorSpan = Tuple[int, int]
LabelsPoorSpans = Dict[LabelName, List[PoorSpan]]
TaxonsPoorSpans = Dict[TaxonName, List[PoorSpan]]

class ProgramRecord(TypedDict):
    timestamp: str
    links: ProgramNames
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

# Recommendations

ProgramTaxonNames = Dict[ProgramName, TaxonNames]
AssessedPrograms = List[Tuple[float, ProgramName]]

# Pipeline dictionary
#
# The pipeline file consists in a Python dictionary which, for security purposes, will be
# evaluated by ast.literal_eval: https://docs.python.org/3/library/ast.html#ast.literal_eval).
#
# Main benefits over JSON:
# - with raw strings r"...", no need to double-escape backslashes in regexes;
# - trailing commas;
# - comments!

class Process(TypedDict):
    operation: Literal["impart", "exclude", "include"]
    programs_or_taxons: Literal["programs", "taxons"]
    name_or_pattern: Literal["name", "pattern"]
    source: Union[str, List[str]] # not source-code, but source of the data
    filtered_out: ProgramNames # to be populated by the execution of the process

class Pipeline(TypedDict):
    input_path: str
    output_path: str
    cost_assessment_strategy: str
    processes: List[Process]

# fmt:on
