from typing import Counter as Bag
from typing import Dict, List, NamedTuple, NewType, Set, Tuple, Union, Callable

from typing_extensions import TypedDict, Literal  # Python 3.8: import directly from typing

# fmt: off


# --------------------------------------------------------------------------------------------------
# Various types
# --------------------------------------------------------------------------------------------------

Source = NewType("Source", str)  # Source code of the user's programs.
Query = NewType("Query", str)  # SQL specification of a feature, as defined in `spec.md`.

class Span(NamedTuple):  # Location of a given feature.
    start: int  # First line of the feature.
    end: int  # Last line of the feature.
    path: str = ""  # Identifier of the beginning of the feature in the AST.


# --------------------------------------------------------------------------------------------------
# Labels
# --------------------------------------------------------------------------------------------------

LabelName = NewType("LabelName", str)  # Name of a feature, as defined in `spec.md`.
LabelNames = List[LabelName]

class Label(NamedTuple):
    name: LabelName
    spans: List[Span]

Labels = List[Label]
LabelsSpans = Dict[LabelName, List[Span]]

LabelPattern = NewType("LabelPattern", str)  # Member of the second row of `taxonomy.tsv`.


# --------------------------------------------------------------------------------------------------
# Taxa
# --------------------------------------------------------------------------------------------------

TaxonName = NewType("TaxonName", str) # Path from a root to a node in the taxonomy.
TaxonNames = List[TaxonName]
TaxonNameSet = Set[TaxonName]

class Taxon(NamedTuple):
    name: TaxonName
    spans: Bag[Span]  # For a given taxon, associate each span to its number of occurrences.
                      # For instance, if there are three integer literals on line 42, the
                      # corresponding entry is: (42, 42, '...'): 3.

Taxa = List[Taxon]
TaxaSpans = Dict[TaxonName, Bag[Span]]

TaxonPattern = NewType("TaxonPattern", str) # Member of the first row of `taxonomy.tsv`.
TaxonPatterns = List[TaxonPattern]


# --------------------------------------------------------------------------------------------------
# Programs
# --------------------------------------------------------------------------------------------------

ProgramPath = NewType("ProgramPath", str)  # relative path of a program in the directory to search
ProgramPaths = List[ProgramPath]
ProgramPathSet = Set[ProgramPath]

class Program(NamedTuple):  # All the information pertaining to a program.
    labels: Labels
    taxa: Taxa
    addition: LabelsSpans  # Features scheduled for addition.
    deletion: LabelsSpans  # Features scheduled for deletion.
    path: ProgramPath = ProgramPath("")
    source: Source = Source("")

Programs = List[Program]
ProgramTaxa = Dict[ProgramPath, Taxa]


# --------------------------------------------------------------------------------------------------
# Serialization-ready types used for the JSON tag database
# --------------------------------------------------------------------------------------------------

PoorSpan = Tuple[int, int]  # A span, deprived from its path.
LabelsPoorSpans = Dict[LabelName, List[PoorSpan]]
TaxaPoorSpans = Dict[TaxonName, List[PoorSpan]]

class ProgramRecord(TypedDict):
    timestamp: str  # Date of last modification: currently unused.
    source: Source
    labels: LabelsPoorSpans
    taxa: TaxaPoorSpans

ProgramInfos = Dict[ProgramPath, ProgramRecord]
LabelInfos = Dict[LabelName, ProgramPaths]
TaxonInfos = Dict[TaxonName, ProgramPaths]
ProgramToPrograms = Dict[ProgramPath, ProgramPaths]  # For import-export stuff.

class JsonTagDatabase(TypedDict):  # Schema of the JSON version of a tag database.
    programs: ProgramInfos
    labels: LabelInfos
    taxa: TaxonInfos
    importations: ProgramToPrograms
    exportations: ProgramToPrograms


# --------------------------------------------------------------------------------------------------
# Pipeline dictionary
# --------------------------------------------------------------------------------------------------

Operation = NewType("Operation", str) # "exclude", "include", "include all", "include any", etc.

Criterion = Union[str, Tuple[str, str, str]] # Either a pattern or a semantic triple.

class Command(TypedDict):
    operation: Operation
    data: Union[str, List[Criterion]]  # Either a shell command or a list of criteria.

Predicate = Callable[[PoorSpan, PoorSpan], bool] # A value of the dictionary `compare_spans`.


# --------------------------------------------------------------------------------------------------
# Recommendations
# --------------------------------------------------------------------------------------------------

AssessedPrograms = List[Tuple[float, ProgramPath]] # Associative array between costs and programs
AssessmentStrategy = Literal["zeno", "linear"]

# fmt:on
