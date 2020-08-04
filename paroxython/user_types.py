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

LabelPattern = NewType("LabelPattern", str)

# Taxa

TaxonName = NewType("TaxonName", str)
TaxonNames = List[TaxonName]
TaxonNameSet = Set[TaxonName]

class Taxon(NamedTuple):
    name: TaxonName
    spans: Bag[Span]

Taxa = List[Taxon]
TaxaSpans = Dict[TaxonName, Bag[Span]]

TaxonPattern = NewType("TaxonPattern", str)
TaxonPatterns = List[TaxonPattern]

# Programs

ProgramName = NewType("ProgramName", str)
ProgramNames = List[ProgramName]
ProgramNameSet = Set[ProgramName]

class Program(NamedTuple):
    labels: Labels
    taxa: Taxa
    addition: LabelsSpans
    deletion: LabelsSpans
    name: ProgramName = ProgramName("")
    source: Source = Source("")

Programs = List[Program]
ProgramTaxa = Dict[ProgramName, Taxa]

# Serialization-ready types used for the JSON tag database

PoorSpan = Tuple[int, int]
LabelsPoorSpans = Dict[LabelName, List[PoorSpan]]
TaxaPoorSpans = Dict[TaxonName, List[PoorSpan]]

class ProgramRecord(TypedDict):
    timestamp: str
    source: Source
    labels: LabelsPoorSpans
    taxa: TaxaPoorSpans

ProgramInfos = Dict[ProgramName, ProgramRecord]
LabelInfos = Dict[LabelName, ProgramNames]
TaxonInfos = Dict[TaxonName, ProgramNames]
ProgramToPrograms = Dict[ProgramName, ProgramNames]

class JsonDatabase(TypedDict):
    programs: ProgramInfos
    labels: LabelInfos
    taxa: TaxonInfos
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

Operation = NewType("Operation", str)

Criterion = Union[str, Tuple[str, str, str]] # either a pattern or a semantic triple

class Command(TypedDict):
    operation: Operation
    data: Union[str, List[Criterion]]
    filtered_out: ProgramNames # to be populated by the execution of the command

Predicate = Callable[[int, int], bool]

# Recommendations

AssessedPrograms = List[Tuple[float, ProgramName]]

AssessmentStrategy = Literal["zeno", "linear"]

# fmt:on
