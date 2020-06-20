[
    {
        "operation": "impart",
        "programs_or_taxa": "programs",
        "data": "python helpers/parse_syllabus.py {base_path}/syllabus.txt",
    },
    {"operation": "exclude", "programs_or_taxa": "programs", "data": ["prg7.py", "prg9.py"],},
    {"operation": "exclude", "programs_or_taxa": "taxa", "data": ["X/S/M/L/R/D/.*"],},
    {"operation": "include", "programs_or_taxa": "taxa", "data": ["O/C.*"],},
]
