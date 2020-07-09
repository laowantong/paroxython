[
    {}, # no operation nor data
    {"operation": "foobar"}, # unknown operation
    {"operation": "exclude"}, # no data
    {"operation": "exclude", "data": []}, # empty data
    {"operation": "impart", "data": "python helpers/parse_syllabus.py {base_path}/syllabus.txt"},
    {"operation": "exclude", "data": ["prg7.py", "prg9.py"]},
    {"operation": "exclude", "data": ["X/S/M/L/R/D/.*"]},
    {"operation": "include", "data": ["O/C.*"]},
    {"operation": "hide", "data": ["O/C/H/B"]},
]
