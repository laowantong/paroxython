import regex  # type: ignore

from user_types import TaxonName, JsonDatabase, ProgramNameSet, TaxonNameSet


class ProgramProcessor:
    def __init__(self, db: JsonDatabase):
        self.db = db
        self.old_program_names: ProgramNameSet = set()
        self.old_taxons: TaxonNameSet = set()

    def init_old_programs(
        self,
        syllabus_text: str,
        path_prefix: str = "",
        search_pattern: str = r"(?sm)(.*)^ *# EOF",  # \1 matches the useful part of the syllabus
        finditer_pattern: str = r"\+ *(?:\[.+?\] *)?(\w+\.py)\b",  # \1 matches a program name
    ):
        """Retrieve the programs marked as already studied in the teacher's syllabus."""
        source = regex.search(search_pattern, syllabus_text)[1]
        matches = regex.finditer(finditer_pattern, source)
        syllabus_old_programs = {path_prefix + match[1] for match in matches}
        self.old_program_names = syllabus_old_programs.intersection(self.db["programs"])

    def init_old_taxons(self):
        """
        Construct the set of the notions covered by the programs already studied.

        A taxon having the form "segment_0/segment_1/.../segment_n/", it covers subsequently:
            - "segment_0"
            - "segment_0/segment_1/"
            - ...
            - "segment_0/segment_1/.../segment_n/"
        """
        self.old_taxons.clear()
        for old_program_name in self.old_program_names:
            taxon_names = self.db["programs"][old_program_name]["taxons"]
            for taxon_name in taxon_names:
                segments = taxon_name.split("/")
                for i in range(len(segments)):
                    self.old_taxons.add("/".join(segments[:~i]))

    def calculate_taxon_cost(self, taxon_name: TaxonName) -> int:
        """Evaluate the learning cost of a new taxon as the minimal path length from an old one."""
        segments = taxon_name.split("/")
        for cost in range(len(segments)):
            if "/".join(segments[:~cost]) in self.old_taxons:
                break
        return cost


if __name__ == "__main__":
    Path = __import__("pathlib").Path
    json = __import__("json")
    db = json.loads(Path("db.json").read_text())
    processor = ProgramProcessor(db)
    syllabus = Path("../algo/timeline.txt").read_text()
    processor.init_old_programs(syllabus, "../algo/programs/")
    processor.init_old_taxons()
