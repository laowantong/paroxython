{
    "input_path": "db.json",
    "output_path": "recommendations.md",
    "cost_assessment_strategy": "zeno",
    "commands": [
        {
            "operation": "impart",
            "programs_or_taxons": "programs",
            "name_or_pattern": "name",
            "source": "python helpers/parse_syllabus.py {base_path}/syllabus.txt",
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
