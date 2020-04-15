{
    "input_path": "dummy/db.json",
    "output_path": "dummy/recommendations.md",
    "cost_assessment_strategy": "zeno",
    "processes": [
        {
            "operation": "impart",
            "programs_or_taxons": "programs",
            "name_or_pattern": "name",
            "source": "python helpers/parse_syllabus.py {base_path}/dummy/syllabus.txt",
        },
        {
            "operation": "exclude",
            "programs_or_taxons": "programs",
            "name_or_pattern": "name",
            "source": ["prg7.py", "prg9.py"],
        },
        {
            "operation": "exclude",
            "programs_or_taxons": "taxons",
            "name_or_pattern": "pattern",
            "source": ["X/S/M/L/R/D/.*"],
        },
        {
            "operation": "include",
            "programs_or_taxons": "taxons",
            "name_or_pattern": "pattern",
            "source": ["O/C.*"],
        },
    ],
}
