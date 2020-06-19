"""Evolve a set of selected programs and a set of taxons representing the imparted knowledge.

Description:
    Initially, all programs in the database are selected, and the imparted knowledge is empty.

    ..note::
        As the filter evolves, the former set can only shrink, and the latter only increase.

    The class stores the state of these two sets and provides a collection of operators to be
    applied on them during the execution of the pipeline (see `paroxython.recommend_programs`).

## Internal calls

.. image:: resources/filter_flow.png


"""

from collections import Counter as counter
from collections import defaultdict
from itertools import permutations, product
from typing import Counter, Dict, Iterator, List, Tuple

import regex  # type: ignore

from .goodies import print_warning
from .normalize_predicate import normalize_predicate
from .user_types import (
    JsonDatabase,
    Operation,
    Predicate,
    ProgramInfos,
    ProgramName,
    ProgramNameSet,
    ProgramToPrograms,
    TaxonInfos,
    TaxonName,
    TaxonNameSet,
    TaxonsPoorSpans,
)

__pdoc__ = {
    "ProgramFilter.__init__": True,
    "ProgramFilter": "",
}


class ProgramFilter:

    # Initialization of the filter

    def __init__(self, db: JsonDatabase) -> None:
        """Call `define_shortcuts()`,  `init_filter_state()` and `add_imported_taxons()` (below)."""
        self.define_shortcuts(db)
        self.init_filter_state()
        self.add_imported_taxons()

    def define_shortcuts(self, db: JsonDatabase) -> None:
        """Define some attributes that point directly to the main parts of the database."""
        self.db_programs: ProgramInfos = db["programs"]
        self.db_taxons: TaxonInfos = db["taxons"]
        self.db_importations: ProgramToPrograms = db["importations"]
        self.db_exportations: ProgramToPrograms = db["exportations"]

    def init_filter_state(self) -> None:
        """Select all programs and define the imparted knowledge as empty."""
        self.imparted_knowledge: TaxonNameSet = set()
        self.selected_programs: ProgramNameSet = set(self.db_programs)

    def add_imported_taxons(self) -> None:
        """Copy under each program the taxons it featured by importation.

        Description:
            Initially, the JSON database stores under each program all the taxons it features
            _directly_, for instance:
            ```
            {
                "programs": {
                    ...
                    "fizzbuzz.py": {
                        ...
                        "taxons": {
                            "call/function/builtin/print": [[4,4],[6,6],[8,8],[10,10]],
                            "call/function/builtin/range": [[2,2]],
                            "flow/conditional": [[3,10],[5,10],[7,10]],
                            ...
            ```

             For performance and readability reasons, it is useful to complete such a dictionary
             with the taxons which are featured _indirectly_, namely those featured by the imported
             programs. For instance, assuming that `fizzbuzz.py` imports `collatz.py`, we must
             copy the taxons featured by the latter, but not by the former program, namely:

            ```
                            "operator/arithmetic/multiplication": [],
                            "subroutine/argument/arg": [],
                            "subroutine/procedure": [],
                            ...
            ```

        Notes:
            - The spans of the imported taxons are not copied, but replaced by an empty list (it is
            enough to know that a certain taxon is only featured by an imported program, not on
            which lines of which program).
            - All imported taxons starting with `"metadata/"` are by convention excluded from the
            copy.
        """
        for (exporter, importers) in self.db_exportations.items():
            exported_taxons = list(self.db_programs[exporter]["taxons"])
            for exported_taxon in exported_taxons:
                if exported_taxon.startswith("metadata/"):
                    continue
                for importer in importers:
                    importer_taxons = self.db_programs[importer]["taxons"]
                    if exported_taxon not in importer_taxons:
                        importer_taxons[exported_taxon] = []

    # Get the set of taxon names or program names matching the given pattern.

    def taxons_of_pattern(self, pattern: str) -> TaxonNameSet:
        """Find all the existing taxons matching the given regular expression pattern.

        Note:
            All taxons are searched, not just the ones featured by a selected program.
        """
        match = regex.compile(fr"{pattern}\b").match
        result: TaxonNameSet = set(filter(match, self.db_taxons))
        if not result:
            print_warning(f"the pattern '{pattern}' doesn't match any existing taxon.")
        return result

    def programs_of_pattern(self, pattern: str) -> ProgramNameSet:
        """Find all the existing programs matching the given regular expression pattern.

        Note:
            All programs are searched, not just the selected ones.
        """
        match = regex.compile(fr"{pattern}").match
        result: ProgramNameSet = set(filter(match, self.db_programs))
        if not result:
            print_warning(f"the pattern '{pattern}' doesn't match any existing program.")
        return result

    # Select programs from the taxons they feature, and vice versa.

    def taxons_of_programs(self, programs: ProgramNameSet, follow: bool = False) -> TaxonNameSet:
        """Return the taxons featured (or optionally imported) by any given program.

        Args:
            programs (ProgramNameSet): Program names. The non-existing ones are silently ignored.
            follow (bool, optional): If true, include the taxons featured by the imported programs.
                Defaults to `False`.

        Example:
            Let `p1`, `p2`, `p3` be three programs, with `p3` importing `p2`, and `p2` importing
                `p1`. Let `t` be a taxon featured by `p1` only. Then:
            >>> t in taxons_of_programs({p1})
            True
            >>> t in taxons_of_programs({p2})
            False
            >>> t in taxons_of_programs({p3}, follow=True)
            True
        """
        taxons: TaxonNameSet = set()
        for program in programs:
            if program in self.db_programs:
                for (taxon, spans) in self.db_programs[program]["taxons"].items():
                    if spans or follow:
                        # Either the taxon is featured directly or the imports must be followed.
                        taxons.add(taxon)
        return taxons

    def programs_of_taxons(self, taxons: TaxonNameSet, follow: bool = False) -> ProgramNameSet:
        """Return the programs featuring (or optionally importing) any given taxon.

        Args:
            taxons (TaxonNameSet): Taxon names. The non-existing ones are silently ignored.
            follow (bool, optional): If true, include the programs importing at least one program
                featuring at least one taxon. Defaults to `False`.

        Example:
            With `p1`, `p2`, `p3` and `t` as in the example of `ProgramFilter.taxons_of_programs`:
            >>> programs_of_taxons({t})
            {p1}
            >>> programs_of_taxons({t}, follow=True)
            {p1, p2, p3}
        """
        programs: ProgramNameSet = set()
        for taxon in taxons:
            programs.update(self.db_taxons.get(taxon, []))
        if follow:
            for program in list(programs):
                programs.update(self.db_exportations[program])
        return programs

    # Update the state of the filter by applying set operations with the given programs or taxons.

    def update_filter(self, data: List, operation: Operation, quantifier: str) -> None:
        """Update the selected programs and optionally impart the associated taxons.

        Description:
            - If the operation is `"impart"`:
                - calculate the appropriate sets of programs and taxons;
                - remove these programs from `self.selected_programs`;
                - add these taxons to `self.imparted_knowledge`.
            - Otherwise (the operation is either `"include"` or `"exclude"`):
                - calculate the appropriate bag of programs: this bag counts, for each program,
                    the number of criteria they meet (maximum: size of `data`);
                - if `quantifier` is `"all"`, remove from this bag all programs which do not
                    meet at least one criterion;
                - include or exclude the resulting programs. Note that the `"exclude"` operation
                    extends to the programs which import the resulting ones: if the user wants to
                    exclude a program, she obviously expects that the programs which require it
                    are excluded too.

        Args:
            data (List): A list of criteria, _i.e._, a mix of regular expression patterns (strings)
                and/or predicates (triples).
            operation (Operation): Either `"impart"`, `"include"` or `"exclude"`.
            quantifier (str): Either `"any"` or `"all"`.
        """
        if operation == "impart":
            (program_set, taxon_set) = self.programs_and_taxons_to_impart(data)
            self.exclude_programs(program_set, follow=False)
            self.impart_taxons(taxon_set)
        else:
            program_bag = self.programs_to_include_or_exclude(data, follow=(operation == "exclude"))
            if quantifier == "all":
                program_bag -= counter({program: len(data) - 1 for program in program_bag})
            if operation == "include":
                self.include_programs(set(program_bag))
            else:  # necessarily "exclude"
                self.exclude_programs(set(program_bag), follow=True)

    def programs_and_taxons_to_impart(self, data: List[str]) -> Tuple[ProgramNameSet, TaxonNameSet]:
        """Calculate the sets of programs and taxons that meet at least one of the data criteria.

        Description:
            Each data criterion is a string which is interpreted either as:

            - a program name pattern (ending with `".py"`). All programs matching it are accumulated
                in the result, along with any taxon they feature, directly or by importation;
            - or a taxon name pattern. All taxons matching it are accumulated in the result.

        Args:
            data (List[str]): A list of regular expression patterns (strings). Note that the
                operation `"impart"` does not support predicate criteria.

        Returns:
            Tuple[ProgramNameSet, TaxonNameSet]: The couple of accumulated programs and taxons.
        """
        resulting_taxons: TaxonNameSet = set()
        resulting_programs: ProgramNameSet = set()
        for datum in data:
            if isinstance(datum, str):
                if datum.endswith(".py"):
                    programs = self.programs_of_pattern(datum)
                    taxons = self.taxons_of_programs(programs, follow=False)
                    resulting_programs.update(programs)
                else:
                    taxons = self.taxons_of_pattern(datum)
                resulting_taxons.update(taxons)
            else:
                print_warning(f"datum {repr(datum)} cannot be imparted.")
        return (resulting_programs, resulting_taxons)

    def programs_to_include_or_exclude(self, data: List, follow: bool) -> Counter[ProgramName]:
        """Calculate the set of programs that meet at least one of the data criteria.

        Description:
            Each data criterion may be either:

            - a string, which will be interpreted either as:
                - a program name pattern (ending with `".py"`). All programs matching it are
                    accumulated in the result;
                - or a taxon name pattern. All programs featuring at least one taxon matching it
                    are accumulated in the result. If the operation is `"exclude"`, this set is
                    extended to the programs which import (either directly or by transitivity) at
                    least one of its members;
            - a triple consisting in a “subject” pattern, a predicate (positive or negative)
                and an ”object” pattern. This predicate is normalized and, depending on its
                “sign”, evaluated on the patterns by either `ProgramFilter.programs_of_triple` or
                `ProgramFilter.programs_of_negated_triple`.

        Args:
            data (List): A list of criteria, _i.e._, a mix of regular expression patterns (strings)
                and/or predicates (triples).
            follow (bool): If `True`, extend the result with all the programs which import (either
                directly or by transitivity) at least one program meeting a data criterion.

        Returns:
            Counter[ProgramName]: A bag (multiset) counting, for each resulting program, the number
                of criteria it meets.
        """
        resulting_programs: Counter[ProgramName] = counter()
        for datum in data:
            if isinstance(datum, str):
                if datum.endswith(".py"):
                    programs = self.programs_of_pattern(datum)
                else:
                    programs = self.programs_of_taxons(self.taxons_of_pattern(datum), follow=follow)
                resulting_programs.update(programs)
            elif isinstance(datum, (list, tuple)) and len(datum) == 3:
                (pattern_1, raw_predicate, pattern_2) = datum
                (predicate, negated) = normalize_predicate(raw_predicate)
                function = self.programs_of_negated_triple if negated else self.programs_of_triple
                resulting_programs.update(function(pattern_1, predicate, pattern_2))
            else:
                print_warning(f"datum {repr(datum)} cannot be included or excluded.")
        return resulting_programs

    def impart_taxons(self, taxons: TaxonNameSet) -> None:
        """Enrich the imparted knowledge with all the prefixes of the given taxons.

        Add to `self.imparted_knowledge` the given taxons, along with all their prefixes. For
        instance, imparting a taxon `a/b/c`, will impart taxons `a` and `a/b` too.

        Args:
            taxons (TaxonNameSet): The concepts to be imparted along with their “super” concepts.
        """
        for taxon in taxons:
            edges = taxon.split("/")
            for i in range(len(edges)):
                prefix = "/".join(edges[: i + 1])
                self.imparted_knowledge.add(TaxonName(prefix))

    def include_programs(self, programs: ProgramNameSet) -> None:
        """Deselect the programs not found among the given ones.

        Args:
            programs (ProgramNameSet): The set of programs to keep (provided they are already in
                `self.selected_programs`). All other programs of `self.selected_programs` will be
                filtered out.
        """
        self.selected_programs.intersection_update(programs)

    def exclude_programs(self, programs: ProgramNameSet, follow: bool) -> None:
        """Deselect the programs found among the given ones or (optionally) importing them.

        Args:
            programs (ProgramNameSet): The set of programs to exclude.
            follow (bool): If `True`, exclude also all programs which import (either directly or
                by transitivity) at least one member of the given `programs`.
        """
        self.selected_programs.difference_update(programs)
        if follow:
            for program in programs:
                self.selected_programs.difference_update(self.db_exportations.get(program, {}))

    # Deal with semantic triples of the form (taxon_pattern_1, taxon_pattern_2, predicate)

    def programs_of_triple(
        # fmt: off
        self,
        taxon_pattern_1: str,
        predicate: Predicate,
        taxon_pattern_2: str,
        # fmt: on
    ) -> ProgramNameSet:
        """Return the programs where two given taxons satisfy a given predicate.

        Args:
            taxon_pattern_1 (str): A regular expression pattern matching the “subject” of the
                semantic triple.
            predicate (Predicate): the predicate of the semantic triple, always expressed in
                positive form.
            taxon_pattern_2 (str): A regular expression pattern matching the ”object” of the
                semantic triple.

        Returns:
            ProgramNameSet: The programs featuring at least one span `s_1` of `taxon_1` and one
                span `s_2` of `taxon_2` for which `predicate(s_1, s_2)` is verified.
        """
        taxons_1 = self.taxons_of_pattern(taxon_pattern_1)
        taxons_2 = self.taxons_of_pattern(taxon_pattern_2)
        programs_1 = self.programs_of_taxons(taxons_1)
        programs_2 = self.programs_of_taxons(taxons_2)
        result: ProgramNameSet = set()
        for program in programs_1 & programs_2:  # for each program featuring both taxon sets
            spans = self.db_programs[program]["taxons"]
            for (span_1, span_2) in self.iterate_on_spans(spans, taxons_1, taxons_2):
                if predicate(span_1, span_2):
                    result.add(program)
                    break
        return result

    def programs_of_negated_triple(
        # fmt: off
        self,
        taxon_pattern_1: str,
        predicate: Predicate,
        taxon_pattern_2: str,
        # fmt: on
    ) -> ProgramNameSet:
        """Return the programs where at least one occurrence of two taxons violates the predicate.

        Args:
            The same arguments as `ProgramFilter.programs_of_triple()`, including the fact that the
            predicate is expressed in **positive** form.

        Returns:
            ProgramNameSet: The programs such that, for each span `s_1` of `taxon_1`, there
                exists no span `s_2` of `taxon_2` for which `predicate(s_1, s_2)` is verified.

        ..warning::
            Returns also all programs featuring at least one `taxon_1`, but no `taxon_2`. Indeed,
            suppose the user wants to exclude all the programs featuring at least one tuple which
            is not used in a parallel assignment. Let us call the two types of tuples “ordinary”
            and “parallel”. This function will return a set of programs where:

            - there is at least one tuple, but no parallel tuple (_i.e._, all tuples are ordinary);
            - or there is at least one ordinary tuple (_i.e._, one tuple which is not parallel).

            Excluding these two sets keeps only the programs where:

            - there is no tuple;
            - or all tuples are parallel.

            If, in the first stage, the function did not return the programs featuring at least one
            tuple, but no parallel tuple, the second stage would exclude all the programs featuring
            no tuple, which would certainly not correspond to the user's intention.

        Examples:
            If the predicate is `"taxon_1 not inside taxon_2"`, any program consisting in:

            - `"taxon_2{taxon_1}"`[^braces] is rejected;
            - `"taxon_1"` is **accepted** (although there is no `taxon_2`);
            - `"taxon_2"` is **rejected** (no `taxon_1`);
            - `"taxon_1{taxon_2}"` is accepted;
            - `"taxon_1 taxon_2{taxon_1}"` is accepted (there exists a couple (`s_1`, `s_2`) such
              that `taxon_1` is not inside `taxon_2`);
            - `"taxon_1 taxon_2{taxon_1} taxon_2{}"` is accepted.

            If the predicate is `"taxon_2 not contains taxon_1"` (sic), any program consisting in:

            - `"taxon_2{taxon_1}"` is rejected;
            - `"taxon_1"` is **rejected** (no `taxon_2`);
            - `"taxon_2"` is **accepted** (although there is no `taxon_1`);
            - `"taxon_1{taxon_2}"` is accepted;
            - `"taxon_1 taxon_2{taxon_1}"` is accepted (there exists a couple (`s_1`, `s_2`) such
              that `taxon_2` does not contain `taxon_1`);
            - `"taxon_1 taxon_2{taxon_1} taxon_2{}"` is accepted.

            Note that, due to the rule explained in the warning above, `"taxon_1 not inside taxon_2"`
            is not strictly equivalent to `"taxon_2 not contains taxon_1"`.

            [^braces]:
                In these examples, the braces are used to denote the fact that the span of a
                certain taxon is included in that of another taxon.
        """
        taxons_1 = self.taxons_of_pattern(taxon_pattern_1)
        taxons_2 = self.taxons_of_pattern(taxon_pattern_2)
        programs_1 = self.programs_of_taxons(taxons_1)
        programs_2 = self.programs_of_taxons(taxons_2)
        result: ProgramNameSet = programs_1  # by default, keep all programs featuring taxon_1
        for program in programs_1 & programs_2:  # for each program featuring both taxon sets
            spans = self.db_programs[program]["taxons"]
            exists_span_2_satisfying_predicate: Dict[Tuple, bool] = defaultdict(bool)
            for (span_1, span_2) in self.iterate_on_spans(spans, taxons_1, taxons_2):
                exists_span_2_satisfying_predicate[tuple(span_1)] |= predicate(span_1, span_2)
            if all(exists_span_2_satisfying_predicate.values()):
                # for any span_1, there is at least one span_2 such that predicate(span_1, span_2)
                result.remove(program)
        return result

    def iterate_on_spans(
        # fmt: off
        self, # declared as an instance method to prevent pdoc3 from misplacing its documentation.
        spans: TaxonsPoorSpans,
        taxons_1: TaxonNameSet,
        taxons_2: TaxonNameSet
        # fmt: on
    ) -> Iterator:
        """Generate all relevant couples of spans for the given “subject” and ”object” taxons.

        Description:
            This private function is invoked by `ProgramFilter.programs_of_triple` and
            `ProgramFilter.programs_of_negated_triple` to enumerate the couples of spans on which
            a condition of the form : “`subject_span` `predicate` `object_span`” will be evaluated.
            Initially, such a condition is expressed by the user as: “`subject_pattern` `predicate`
            `object_pattern`”. Both patterns may match several taxons and, in a given program, each
            taxon can occur on several different or even identical spans. Ultimately, the predicate
            expresses a relation between two spans.

        Args:
            spans (TaxonsPoorSpans): The dictionary of the taxons featured by a certain program,
                each taxon being associated with a list of poor spans (“poor” meaning that they
                contain no other information than the numbers of the first and last line of a taxon
                occurrence).
            taxons_1 (TaxonNameSet): The various “subject” taxons of the semantic triple.
            taxons_2 (TaxonNameSet): The various “object” taxons of the semantic triple.

        Yields:
            Iterator[PoorSpan]: Couples of poor spans, in no particular order.

        Example:
            Consider a program featuring taxons `t1`, `t2`, `t3` and `t4` on the following spans:
            >>> spans = {
            ...      "t1": [(1, 1), (1, 1), (1, 2)],
            ...      "t2": [(2, 3), (1, 2)],
            ...      "t3": [(3, 3)],
            ...      "t4": [(4, 4)],
            ... }

            Note that `t1` occurs twice on span `(1, 1)`, and that `t1` and `t2` have span `(1, 2)`
            in common.

            Suppose first that the sets `taxons_1` and `taxons_2` have no common taxons. In this
            case, the couples of spans on which to check the predicate are obtained by a simple
            cross-product, _e.g._:

            >>> iterate_on_spans(spans, {"t1", "t2"}, {"t3", "t4"})
            ((1, 1), (3, 3))  # t1 (1) ⨉ t3
            ((1, 1), (3, 3))  # t1 (2) ⨉ t3
            ((1, 2), (3, 3))  # t1 (3) ⨉ t3
            ((1, 1), (4, 4))  # t1 (1) ⨉ t4
            ((1, 1), (4, 4))  # t1 (2) ⨉ t4
            ((1, 2), (4, 4))  # t1 (3) ⨉ t4
            ((2, 3), (3, 3))  # t2 (1) ⨉ t3
            ((1, 2), (3, 3))  # t2 (2) ⨉ t3
            ((2, 3), (4, 4))  # t2 (1) ⨉ t4
            ((1, 2), (4, 4))  # t2 (2) ⨉ t4

            Suppose now that the sets `taxons_1` and `taxons_2` have `t1` in common. In that case,
            we must suppress the diagonal of the cross-product, which not only carries zero useful
            information, but will make certain conditions fail. For instance, if we seek to include
            all the programs _not_ featuring two multiplications on the same line, the condition
            will be something like: “no multiplication is featured on the same line than another
            one”. Keeping the diagonal would add “or itself“ to the previous condition. Since any
            taxon is obviously featured on the same line than itself, no program would satisfy the
            condition.

            In the example below, note which lines are suppressed, and which are kept (particularly
            for `((1, 1), (1, 1))`):

            >>> iterate_on_spans(spans, {"t1", "t2"}, {"t1", "t3"})
            # ((1, 1), (1, 1))  # t1 (1) ⨉ t1 (1) (not generated)
              ((1, 1), (1, 1))  # t1 (1) ⨉ t1 (2)
              ((1, 1), (1, 2))  # t1 (1) ⨉ t1 (3)
              ((1, 1), (1, 1))  # t1 (2) ⨉ t1 (1)
            # ((1, 1), (1, 1))  # t1 (2) ⨉ t1 (2) (not generated)
              ((1, 1), (1, 2))  # t1 (2) ⨉ t1 (3)
              ((1, 2), (1, 1))  # t1 (3) ⨉ t1 (1)
              ((1, 2), (1, 1))  # t1 (3) ⨉ t1 (2)
            # ((1, 2), (1, 2))  # t1 (3) ⨉ t1 (3) (not generated)
              ((1, 1), (3, 3))  # t1 (1) ⨉ t3
              ((1, 1), (3, 3))  # t1 (2) ⨉ t3
              ((1, 2), (3, 3))  # t1 (3) ⨉ t3
              ((2, 3), (1, 1))  # t2 (1) ⨉ t1 (1)
              ((2, 3), (1, 1))  # t2 (1) ⨉ t1 (2)
              ((2, 3), (1, 2))  # t2 (1) ⨉ t1 (3)
              ((1, 2), (1, 1))  # t2 (2) ⨉ t1 (1)
              ((1, 2), (1, 1))  # t2 (2) ⨉ t1 (2)
              ((1, 2), (1, 2))  # t2 (2) ⨉ t1 (3)
              ((2, 3), (3, 3))  # t2 (1) x t3
              ((1, 2), (3, 3))  # t2 (2) x t3
        """
        for (taxon_1, taxon_2) in product(taxons_1, taxons_2):
            if taxon_1 in spans and taxon_2 in spans:
                if taxon_1 == taxon_2:  # exclude diagonal from iteration
                    yield from permutations(spans[taxon_1], 2)
                else:
                    yield from product(spans[taxon_1], spans[taxon_2])


# <graphviz>
# "__init__" -> "define_shortcuts"
# "__init__" -> "init_filter_state"
# "__init__" -> "add_imported_taxons"
# "init_filter_state" -> "taxons_of_programs"  [style=invis]
# "update_filter" -> "programs_and_taxons_to_impart"
# "programs_and_taxons_to_impart" -> "programs_of_pattern"
# "programs_and_taxons_to_impart" -> "taxons_of_programs"
# "programs_and_taxons_to_impart" -> "taxons_of_pattern"
# "update_filter" -> "programs_to_include_or_exclude"
# "programs_to_include_or_exclude" -> "programs_of_pattern"
# "programs_to_include_or_exclude" -> "programs_of_taxons"
# "programs_to_include_or_exclude" -> "taxons_of_pattern"
# "programs_to_include_or_exclude" -> "programs_of_triple"
# "programs_of_triple" -> "taxons_of_pattern"
# "programs_of_triple" -> "programs_of_taxons"
# "programs_of_triple" -> "iterate_on_spans"
# "programs_to_include_or_exclude" -> "programs_of_negated_triple"
# "programs_of_negated_triple" -> "taxons_of_pattern"
# "programs_of_negated_triple" -> "programs_of_taxons"
# "programs_of_negated_triple" -> "iterate_on_spans"
# "update_filter" -> "impart_taxons"
# "update_filter" -> "include_programs"
# "update_filter" -> "exclude_programs"
# </graphviz>
