from typing import Counter as Bag
from typing import Dict, List, NamedTuple, NewType, Set, Tuple, Union, Callable

from typing_extensions import TypedDict, Literal  # Python 3.8: import directly from typing

# fmt: off


# Various types

Source = NewType("Source", str)
Query = NewType("Query", str)

class Span(NamedTuple):
    start: int
    end: int
    path: str = ""

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


# Programs

ProgramName = NewType("ProgramName", str)
ProgramNames = List[ProgramName]
ProgramNameSet = Set[ProgramName]

class Program(NamedTuple):
    labels: Labels
    taxons: Taxons
    addition: LabelsSpans
    deletion: LabelsSpans
    name: ProgramName = ProgramName("")
    source: Source = Source("")

Programs = List[Program]
ProgramTaxons = Dict[ProgramName, Taxons]

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
LabelInfos = Dict[LabelName, ProgramNames]
TaxonInfos = Dict[TaxonName, ProgramNames]
ProgramToPrograms = Dict[ProgramName, ProgramNames]

class JsonDatabase(TypedDict):
    programs: ProgramInfos
    labels: LabelInfos
    taxons: TaxonInfos
    importations: ProgramToPrograms
    exportations: ProgramToPrograms


# Pipeline dictionary
#
# The pipeline file consists in a Python dictionary which, for security purposes, will be
# evaluated by ast.literal_eval: https://docs.python.org/3/library/ast.html#ast.literal_eval).
#
# Main benefits over JSON:
# - with raw strings r"...", no need to double-escape backslashes in regexes;
# - trailing commas;
# - comments!

Operation = Literal["include", "exclude", "impart"]

class Command(TypedDict):
    operation: Operation
    source: Union[str, List[str]] # not source code, but source of the data
    filtered_out: ProgramNames # to be populated by the execution of the command

Predicate = Callable[[int, int], bool]

# Recommendations

ProgramTaxonNames = Dict[ProgramName, TaxonNames]
AssessedPrograms = List[Tuple[float, ProgramName]]

AssessmentStrategy = Literal["zeno", "linear"]

# fmt:on
