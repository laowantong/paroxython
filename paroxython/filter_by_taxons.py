from pathlib import Path
import json
from regex import compile


class FilterByTaxons:
    def __init__(self, db):
        """The expected db is a JSON object with the following schema:
        {
            "programs": {
                "program_1_label": {
                    "timestamp": "...", # not required here
                    "source": "...",
                    "tags": {
                        "tag_1_label": [spot_1, spot_2, ...],
                        ...
                    }
                    "taxons: {
                        "taxon_1_label": [spot_1, spot_2, ...],
                    }
                },
                ...
            },
            "tags": { # not required here
                "tag_1_label": [program_1_label, program_2_label, ...],
                ...
            },
            "taxons": {
                "taxon_1_label": [program_1_label, program_2_label, ...],
                ...
            }
        }
        """
        self.programs = db["programs"]
        self.taxons = db["taxons"]
        self.result = set(self.programs.keys())
        self.initial_count = len(self.result)

    def set_forbidden_taxons(self, patterns):
        def closure():
            """Compile the patterns and return the actual filter function."""
            match_taxon = compile("|".join(patterns)).match

            def enclosed_function():
                """Suppress from self.result all programs using any forbidden
                taxon, and return the number of suppressed programs."""
                count = len(self.result)
                for (label, program_names) in self.taxons.items():
                    if match_taxon(label):  # this taxon is forbidden
                        self.result.difference_update(program_names)
                return count - len(self.result)

            return enclosed_function

        self.filter_forbidden_taxons = closure() if patterns else lambda: 0

    def set_mandatory_taxons(self, patterns):
        def closure():
            """Compile the patterns and return the actual filter function."""
            mandatory_taxons = [compile(row).match for row in patterns]

            def enclosed_function():
                """Suppress from self.result all programs not using at least one
                mandatory taxon, and return the number of suppressed programs."""
                count = len(self.result)
                for program_name in list(self.result):
                    program = self.programs[program_name]
                    for mandatory_taxon in mandatory_taxons:
                        for label in program["taxons"]:
                            if mandatory_taxon(label):  # this mandatory taxon is used
                                break  # no need to test the other taxons of this program
                        else:  # this mandatory taxon is not used by this program
                            self.result.discard(program_name)
                            break  # no need to test the other mandatory taxons
                return count - len(self.result)

            return enclosed_function

        self.filter_mandatory_taxons = closure() if patterns else lambda: 0

    def print_results(self):
        for program_name in self.result:
            program = self.programs[program_name]
            print()
            print("-" * 80)
            print(program_name)
            print("-" * 80)
            print(program["source"])
            print()
            for (other_label, spots) in program["taxons"].items():
                print(f"{len(spots):3}: {other_label}")
        print()
        print(self.initial_count, "programs analyzed")
        print(self.forbidden_count, "programs forbidden")
        print(len(self.result), "programs selected")

    def __call__(self):
        self.forbidden_count = self.filter_forbidden_taxons()
        self.mandatory_count = self.filter_mandatory_taxons()
        self.print_results()


if __name__ == "__main__":
    db = json.loads(Path("db.json").read_text())
    filter_by_taxons = FilterByTaxons(db)
    forbidden_patterns = """
        call/method/.*
    """.strip().split()
    filter_by_taxons.set_forbidden_taxons(forbidden_patterns)
    mandatory_patterns = """
        function_definition/.*
        operator/percent/modulo/.*
    """.strip().split()
    filter_by_taxons.set_mandatory_taxons(mandatory_patterns)
    filter_by_taxons()
