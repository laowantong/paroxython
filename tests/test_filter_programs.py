from collections import defaultdict
from pathlib import Path

import pytest
import regex  # type: ignore

import context
from paroxython.filter_programs import DatabaseFilter

text = Path("tests/data/dummy_taxons_and_programs.txt").read_text()

taxon_names = regex.search(r"(?ms)^TAXONS\n(.+?)\n\n", text)[1].split()
programs = regex.findall(r"(?ms)^(prg\d+)\n(.+?)\n\n", text)

db = {
    "programs": {
        program_name: {"source": source, "taxons": defaultdict(list),}
        for (program_name, source) in programs
    },
    "taxons": {taxon_name: set() for taxon_name in taxon_names},
}


for (program_name, source) in programs:
    program = db["programs"][program_name]
    for line in source.split("\n"):
        (i, *taxons) = line.split()
        i = int(i)
        for taxon in taxons:
            (taxon_name, _, length) = taxon.partition("+")
            span = (i, i + int(length)) if length else (i, i)
            program["taxons"][taxon_name].append(span)
            db["taxons"][taxon_name].add(program_name)

# from pprint import pprint
# pprint(db, width=200)


def test_no_filter():
    dbf = DatabaseFilter(db)
    print(dbf.program_names)
    assert dbf.program_names == {
        "prg1",
        "prg2",
        "prg3",
        "prg4",
        "prg5",
        "prg6",
        "prg7",
        "prg8",
        "prg9",
    }


def test_filter_blacklisted_programs():
    dbf = DatabaseFilter(db)
    dbf.filter_blacklisted_programs(["prg[1-5]$"])
    print(dbf.program_names)
    assert dbf.program_names == {"prg6", "prg7", "prg8", "prg9"}


def test_filter_mandatory_taxons():
    dbf = DatabaseFilter(db)
    dbf.filter_mandatory_taxons(["O$", "O/C/F/U$"])
    print(dbf.program_names)
    assert dbf.program_names == {"prg3", "prg4", "prg7"}


def test_filter_forbidden_taxons():
    dbf = DatabaseFilter(db)
    dbf.filter_forbidden_taxons(["O$", "O/C/F/U$"])
    print(dbf.program_names)
    assert dbf.program_names == {"prg1", "prg5"}


def test_get_taxons_in_programs():
    dbf = DatabaseFilter(db)
    result = dbf.get_taxons_in_programs(["prg[1-3]$"])
    print(result)
    assert result == {
        "O",
        "O/C",
        "O/C/F/U",
        "O/C/H",
        "O/C/H/B",
        "O/C/H/B/I",
        "O/J",
        "O/N",
        "O/N/P",
        "X",
        "X/G",
        "X/K",
        "X/S",
        "X/S/M",
        "X/S/M/L",
        "X/S/M/L/R",
        "X/S/M/L/R/D",
        "X/S/M/L/V",
        "X/W",
        "Y",
        "Y/E",
        "Y/T",
        "Y/T/Q",
    }


def test_get_taxons_not_in_programs():
    dbf = DatabaseFilter(db)
    result = dbf.get_taxons_not_in_programs(["prg[1-3]$"])
    print(result)
    assert result == {"O/C/F", "X/S/M/L/R/D/A"}


def test_set_operations():
    dbf = DatabaseFilter(db)
    dbf.filter_mandatory_taxons(["O$", "O/C/F/U$"])
    print(dbf.program_names)
    assert dbf.program_names == {"prg3", "prg4", "prg7"}
    dbf.complement_update()
    print(dbf.program_names)
    assert dbf.program_names == {"prg9", "prg5", "prg6", "prg1", "prg2", "prg8"}
    dbf.update({"prg7"})
    print(dbf.program_names)
    assert dbf.program_names == {"prg9", "prg5", "prg6", "prg1", "prg2", "prg8", "prg7"}
    dbf.difference_update({"prg6", "prg1"})
    print(dbf.program_names)
    assert dbf.program_names == {"prg9", "prg5", "prg2", "prg8", "prg7"}
    dbf.symmetric_difference_update({"prg9", "prg5", "prg1"})
    print(dbf.program_names)
    assert dbf.program_names == {"prg1", "prg2", "prg8", "prg7"}
    dbf.intersection_update({"prg1", "prg2", "prg5"}, {"prg2", "prg8"})
    print(dbf.program_names)
    assert dbf.program_names == {"prg2"}


def test_get_extra_taxons():
    dbf = DatabaseFilter(db)
    result = dbf.get_extra_taxons(["O", "X"])
    print(result)
    assert result == {
        "prg1": ["Y", "Y/T", "Y/T/Q"],
        "prg2": ["Y", "Y/T", "Y/T/Q"],
        "prg3": ["Y", "Y/E", "Y/T"],
        "prg4": ["Y", "Y/T", "Y/T/Q"],
        "prg5": [],
        "prg6": ["Y/E", "Y/T", "Y/T/Q"],
        "prg7": ["Y/E", "Y/T", "Y/T/Q"],
        "prg8": ["Y/E"],
        "prg9": ["Y", "Y/E", "Y/T", "Y/T/Q"],
    }


def test_sort_by_extra_taxon_count():
    dbf = DatabaseFilter(db)
    dbf.sort_by_extra_taxon_count(["O", "X"])
    print(dbf.sorted_programs)
    assert dbf.sorted_programs == [
        (0, "prg5"),  # no extra taxon, see test_get_extra_taxons()
        (1, "prg8"),  # 1 extra taxons
        (3, "prg1"),  # 3 extra taxons
        (3, "prg2"),
        (3, "prg3"),
        (3, "prg4"),
        (3, "prg6"),
        (3, "prg7"),
        (4, "prg9"),  # 4 extra taxons
    ]


def test_get_lacking_taxons():
    dbf = DatabaseFilter(db)
    result = dbf.get_lacking_taxons(["O$", "O/C/H$", "O/C/F/U$"])
    print(result)
    assert result == {
        "prg1": ["O$", "O/C/F/U$", "O/C/H$"],
        "prg2": ["O/C/F/U$", "O/C/H$"],
        "prg3": [],
        "prg4": ["O/C/H$"],
        "prg5": ["O$", "O/C/F/U$"],
        "prg6": ["O$", "O/C/H$"],
        "prg7": ["O/C/H$"],
        "prg8": ["O$", "O/C/H$"],
        "prg9": ["O/C/F/U$"],
    }


def test_sort_by_lacking_taxon_count():
    dbf = DatabaseFilter(db)
    dbf.sort_by_lacking_taxon_count(["O$", "O/C/H$", "O/C/F/U$"])
    print(dbf.sorted_programs)
    assert dbf.sorted_programs == [
        (0, "prg3"),  # prg3 has all the wanted taxons
        (1, "prg4"),  # 1 taxon is lacking
        (1, "prg7"),
        (1, "prg9"),
        (2, "prg2"),
        (2, "prg5"),
        (2, "prg6"),
        (2, "prg8"),
        (3, "prg1"),  # 3 taxons are lacking
    ]


def test_sort_by_distance():
    dbf = DatabaseFilter(db)
    taxon_names = [name + "$" for name in db["programs"]["prg3"]["taxons"]]
    lacking = dbf.get_lacking_taxons(taxon_names)
    print(lacking)
    assert lacking == {
        "prg1": ["O$", "O/C/F/U$", "O/C/H$", "O/C/H/B$", "X/S/M/L/V$", "Y/E$"],
        "prg2": ["O/C/F/U$", "O/C/H$", "O/J$", "X/K$", "X/S$", "X/S/M/L$", "Y/E$"],
        "prg3": [],
        "prg4": ["O/C/H$", "O/J$", "X/K$", "X/S/M$", "X/S/M/L/V$", "Y/E$"],
        "prg5": [
            "O$",
            "O/C/F/U$",
            "O/J$",
            "X/S/M$",
            "X/S/M/L$",
            "X/S/M/L/R$",
            "Y$",
            "Y/E$",
            "Y/T$",
        ],
        "prg6": [
            "O$",
            "O/C/H$",
            "O/C/H/B$",
            "O/N/P$",
            "X/S$",
            "X/S/M$",
            "X/S/M/L$",
            "X/S/M/L/R$",
            "Y$",
        ],
        "prg7": ["O/C/H$", "O/N/P$", "X/S/M/L/V$", "Y$"],
        "prg8": ["O$", "O/C/H$", "X/S$", "X/S/M$", "X/S/M/L/R$", "Y$", "Y/T$"],
        "prg9": ["O/C/F/U$", "O/C/H/B$", "O/N/P$", "X/S$", "X/S/M/L$"],
    }
    extra = dbf.get_extra_taxons(taxon_names)
    print(extra)
    assert extra == {
        "prg1": ["O/N", "X", "X/S/M/L/R/D", "X/W", "Y/T/Q"],
        "prg2": ["O/C", "O/C/H/B/I", "X/G", "X/S/M/L/R/D", "Y/T/Q"],
        "prg3": [],
        "prg4": ["X", "X/G", "X/S/M/L/R/D", "X/S/M/L/R/D/A", "Y/T/Q"],
        "prg5": ["O/C", "O/C/F", "O/C/H/B/I", "O/N", "X", "X/S/M/L/R/D/A"],
        "prg6": ["O/C", "O/C/F", "O/C/H/B/I", "O/N", "X", "X/S/M/L/R/D/A", "X/W", "Y/T/Q"],
        "prg7": ["O/C/H/B/I", "O/N", "X", "X/S/M/L/R/D", "Y/T/Q"],
        "prg8": ["O/C", "O/N", "X/S/M/L/R/D", "X/S/M/L/R/D/A", "X/W"],
        "prg9": ["O/C/F", "O/C/H/B/I", "O/N", "X/W", "Y/T/Q"],
    }
    dbf.sort_by_distance(taxon_names)
    print(dbf.sorted_programs)
    assert dbf.sorted_programs == [
        (0, "prg3"),  #  0 lacking and 0 extra taxons
        (9, "prg7"),  #  4             5
        (10, "prg9"),  # 5             5
        (11, "prg1"),  # 6             5
        (11, "prg4"),  # 6             5
        (12, "prg2"),  # 7             5
        (12, "prg8"),  # 7             5
        (15, "prg5"),  # 9             6
        (17, "prg6"),  # 9             8
    ]


def test_sort_by_taxon_count():
    dbf = DatabaseFilter(db)
    dbf.sort_by_taxon_count()
    print(dbf.sorted_programs)
    assert dbf.sorted_programs == [
        (12, "prg5"),
        (13, "prg2"),
        (13, "prg8"),
        (14, "prg1"),
        (14, "prg4"),
        (14, "prg6"),
        (15, "prg3"),
        (15, "prg9"),
        (16, "prg7"),
    ]


def test_sorted_by_line_count():
    dbf = DatabaseFilter(db)
    dbf.sort_by_line_count()
    print(dbf.sorted_programs)
    assert dbf.sorted_programs == [
        (5, "prg8"),
        (8, "prg1"),
        (8, "prg2"),
        (8, "prg3"),
        (8, "prg4"),
        (8, "prg5"),
        (8, "prg6"),
        (8, "prg7"),
        (8, "prg9"),
    ]


def test_str():
    dbf = DatabaseFilter(db)
    dbf.sort_by_line_count()
    text = str(dbf)
    print(text)
    assert "[5] prg8" in text
    assert "[8] prg1" in text
