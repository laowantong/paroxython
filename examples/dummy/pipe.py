[
    {
        "operation": "impart",
        "programs_or_taxons": "programs",
        "source": "python helpers/parse_syllabus.py {base_path}/syllabus.txt",
    },
    {"operation": "exclude", "programs_or_taxons": "programs", "source": ["prg7.py", "prg9.py"],},
    {"operation": "exclude", "programs_or_taxons": "taxons", "source": ["X/S/M/L/R/D/.*"],},
    {"operation": "include", "programs_or_taxons": "taxons", "source": ["O/C.*"],},
]
