[
    {
        "operation": "impart",
        "programs_or_taxons": "programs",
        "data": "python helpers/parse_syllabus.py {base_path}/syllabus.txt",
    },
    {"operation": "exclude", "programs_or_taxons": "programs", "data": ["prg7.py", "prg9.py"],},
    {"operation": "exclude", "programs_or_taxons": "taxons", "data": ["X/S/M/L/R/D/.*"],},
    {"operation": "include", "programs_or_taxons": "taxons", "data": ["O/C.*"],},
]
