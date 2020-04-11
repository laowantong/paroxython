{
    "input_path": "../snapshots/simple_db.json",
    "output_path": "../snapshots/simple_recommendations.md",
    "syllabus": {
        "path": "simple_syllabus.txt",
        "search_pattern": r"(?sm)(.*)^ *# EOF",
        "finditer_pattern": r"\+ *(?:\[.+?\] *)?(\w+\.py)\b",
    },
    "cost_computation_strategy": "zeno",
    "mandatory_taxon_patterns": [],
    "blacklisted_program_patterns": [],
    "forbidden_taxon_patterns": [],
}
