{
    "input_path": "dummy_db.json",
    "output_path": "dummy_recommendations.md",
    "cost_computation_strategy": "zeno",
    "processes": [
        {
            "operation": "impart",
            "programs_or_taxons": "programs",
            "name_or_pattern": "name",
            "source": ["prg8"],
        },
        {
            "operation": "exclude",
            "programs_or_taxons": "programs",
            "name_or_pattern": "name",
            "source": ["prg7", "prg9"],
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
