from collections import defaultdict
from pathlib import Path

import pytest
import regex

import context
from paroxython.program_filter import ProgramFilter

text = Path("tests/data/taxons_and_programs.txt").read_text()

taxon_names = regex.search(r"(?ms)^TAXONS\n(.+?)\n\n", text)[1].split()
programs = regex.findall(r"(?ms)^(prg\d+)\n(.+?)\n\n", text)

db = {
    "programs": {
        name: {"source": source, "taxons": defaultdict(list)}
        for (name, source) in programs
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

f = ProgramFilter(db)


def test_no_filter():
    f.reset()
    print(f.result)
    assert f.result == {
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
    f.reset()
    f.filter_blacklisted_programs(["prg[1-5]$"])
    print(f.result)
    assert f.result == {"prg6", "prg7", "prg8", "prg9"}


def test_filter_mandatory_taxons():
    f.reset()
    f.filter_mandatory_taxons(["O/$", "O/C/F/U/$"])
    print(f.result)
    assert f.result == {"prg3", "prg4", "prg7"}


def test_filter_forbidden_taxons():
    f.reset()
    f.filter_forbidden_taxons(["O/$", "O/C/F/U/$"])
    print(f.result)
    assert f.result == {"prg1", "prg5"}


def test_get_taxons_in_programs():
    f.reset()
    result = f.get_taxons_in_programs(["prg[1-3]$"])
    print(result)
    assert result == {
        "O/",
        "O/C/",
        "O/C/F/U/",
        "O/C/H/",
        "O/C/H/B/",
        "O/C/H/B/I/",
        "O/J/",
        "O/N/",
        "O/N/P/",
        "X/",
        "X/G/",
        "X/K/",
        "X/S/",
        "X/S/M/",
        "X/S/M/L/",
        "X/S/M/L/R/",
        "X/S/M/L/R/D/",
        "X/S/M/L/V/",
        "X/W/",
        "Y/",
        "Y/E/",
        "Y/T/",
        "Y/T/Q/",
    }


def test_get_taxons_not_in_programs():
    result = f.get_taxons_not_in_programs(["prg[1-3]$"])
    print(result)
    assert result == {"O/C/F/", "X/S/M/L/R/D/A/"}


def test_set_operations():
    f.reset()
    f.filter_mandatory_taxons(["O/$", "O/C/F/U/$"])
    print(f.result)
    assert f.result == {"prg3", "prg4", "prg7"}
    f.complement_update()
    print(f.result)
    assert f.result == {"prg9", "prg5", "prg6", "prg1", "prg2", "prg8"}
    f.update({"prg7"})
    print(f.result)
    assert f.result == {"prg9", "prg5", "prg6", "prg1", "prg2", "prg8", "prg7"}
    f.difference_update({"prg6", "prg1"})
    print(f.result)
    assert f.result == {"prg9", "prg5", "prg2", "prg8", "prg7"}
    f.symmetric_difference_update({"prg9", "prg5", "prg1"})
    print(f.result)
    assert f.result == {"prg1", "prg2", "prg8", "prg7"}
    f.intersection_update({"prg1", "prg2", "prg5"}, {"prg2", "prg8"})
    print(f.result)
    assert f.result == {"prg2"}


def test_get_extra_taxon_names():
    f.reset()
    result = f.get_extra_taxon_names(["O", "X"])
    print(result)
    assert result == {
        "prg1": ["Y/T/", "Y/T/Q/", "Y/"],
        "prg2": ["Y/T/Q/", "Y/", "Y/T/"],
        "prg3": ["Y/T/", "Y/", "Y/E/"],
        "prg4": ["Y/T/", "Y/T/Q/", "Y/"],
        "prg5": [],
        "prg6": ["Y/T/Q/", "Y/T/", "Y/E/"],
        "prg7": ["Y/E/", "Y/T/Q/", "Y/T/"],
        "prg8": ["Y/E/"],
        "prg9": ["Y/", "Y/T/Q/", "Y/E/", "Y/T/"],
    }


def test_sort_by_extra_taxon_count():
    f.reset()
    result = f.sorted_by_extra_taxon_count(["O", "X"])
    print(result)
    assert result == [
        "prg5",  # no extra taxon, see test_get_extra_taxon_names()
        "prg8",  # 2 extra taxons
        "prg1",  # 3 extra taxons
        "prg2",
        "prg3",
        "prg4",
        "prg6",
        "prg7",
        "prg9",  # 4 extra taxons
    ]


def test_get_lacking_taxon_patterns():
    f.reset()
    result = f.get_lacking_taxon_patterns(["O/$", "O/C/H/$", "O/C/F/U/$"])
    print(result)
    assert result == {
        "prg1": ["O/$", "O/C/H/$", "O/C/F/U/$"],
        "prg2": ["O/C/H/$", "O/C/F/U/$"],
        "prg3": [],
        "prg4": ["O/C/H/$"],
        "prg5": ["O/$", "O/C/F/U/$"],
        "prg6": ["O/$", "O/C/H/$"],
        "prg7": ["O/C/H/$"],
        "prg8": ["O/$", "O/C/H/$"],
        "prg9": ["O/C/F/U/$"],
    }


def test_sort_by_lacking_taxon_count():
    f.reset()
    result = f.sorted_by_lacking_taxon_count(["O/$", "O/C/H/$", "O/C/F/U/$"])
    print(result)
    assert result == [
        "prg3",  # prg3 has all the wanted taxons
        "prg4",  # 1 taxon is lacking
        "prg7",
        "prg9",
        "prg2",
        "prg5",
        "prg6",
        "prg8",
        "prg1",  # 3 taxons are lacking
    ]


def test_sort_by_distance():
    f.reset()
    taxon_names = [name + "$" for name in db["programs"]["prg3"]["taxons"]]
    lacking = f.get_lacking_taxon_patterns(taxon_names)
    print(lacking)
    assert lacking == {
        "prg1": ["X/S/M/L/V/$", "O/C/H/B/$", "O/C/F/U/$", "O/C/H/$", "O/$", "Y/E/$"],
        "prg2": [
            "X/K/$",
            "O/J/$",
            "O/C/F/U/$",
            "O/C/H/$",
            "X/S/$",
            "X/S/M/L/$",
            "Y/E/$",
        ],
        "prg3": [],
        "prg4": ["X/K/$", "X/S/M/L/V/$", "O/J/$", "X/S/M/$", "O/C/H/$", "Y/E/$"],
        "prg5": [
            "Y/T/$",
            "X/S/M/L/R/$",
            "O/J/$",
            "X/S/M/$",
            "O/C/F/U/$",
            "Y/$",
            "O/$",
            "X/S/M/L/$",
            "Y/E/$",
        ],
        "prg6": [
            "O/N/P/$",
            "O/C/H/B/$",
            "X/S/M/L/R/$",
            "X/S/M/$",
            "O/C/H/$",
            "X/S/$",
            "Y/$",
            "O/$",
            "X/S/M/L/$",
        ],
        "prg7": ["O/N/P/$", "X/S/M/L/V/$", "O/C/H/$", "Y/$"],
        "prg8": ["Y/T/$", "X/S/M/L/R/$", "X/S/M/$", "O/C/H/$", "X/S/$", "Y/$", "O/$"],
        "prg9": ["O/N/P/$", "O/C/H/B/$", "O/C/F/U/$", "X/S/$", "X/S/M/L/$"],
    }
    extra = f.get_extra_taxon_names(taxon_names)
    print(extra)
    assert extra == {
        "prg1": ["X/W/", "X/", "Y/T/Q/", "X/S/M/L/R/D/", "O/N/"],
        "prg2": ["Y/T/Q/", "X/S/M/L/R/D/", "O/C/", "X/G/", "O/C/H/B/I/"],
        "prg3": [],
        "prg4": ["X/", "Y/T/Q/", "X/S/M/L/R/D/A/", "X/G/", "X/S/M/L/R/D/"],
        "prg5": ["O/C/H/B/I/", "O/N/", "X/", "X/S/M/L/R/D/A/", "O/C/", "O/C/F/"],
        "prg6": [
            "X/",
            "O/N/",
            "Y/T/Q/",
            "X/W/",
            "O/C/",
            "X/S/M/L/R/D/A/",
            "O/C/F/",
            "O/C/H/B/I/",
        ],
        "prg7": ["O/N/", "Y/T/Q/", "X/", "O/C/H/B/I/", "X/S/M/L/R/D/"],
        "prg8": ["X/W/", "O/C/", "O/N/", "X/S/M/L/R/D/A/", "X/S/M/L/R/D/"],
        "prg9": ["X/W/", "O/N/", "Y/T/Q/", "O/C/H/B/I/", "O/C/F/"],
    }
    result = f.sorted_by_distance(taxon_names)
    print(result)
    assert result == [
        "prg3",  # 0 lacking and 0 extra taxons
        "prg7",  # 4             5
        "prg9",  # 5             5
        "prg1",  # 6             5
        "prg4",  # 6             5
        "prg2",  # 7             5
        "prg8",  # 7             5
        "prg5",  # 9             6
        "prg6",  # 9             8
    ]


def test_sort_by_taxon_count():
    f.reset()
    result = f.sorted_by_taxon_count()
    print(result)
    assert result == [
        "prg5",
        "prg2",
        "prg8",
        "prg1",
        "prg4",
        "prg6",
        "prg3",
        "prg9",
        "prg7",
    ]
    counts = [len(db["programs"][program_name]["taxons"]) for program_name in result]
    print(counts)
    assert counts == [12, 13, 13, 14, 14, 14, 15, 15, 16]


def test_sorted_by_line_count():
    f.reset()
    result = f.sorted_by_line_count()
    print(result)
    assert result == [
        "prg8",
        "prg1",
        "prg2",
        "prg3",
        "prg4",
        "prg5",
        "prg6",
        "prg7",
        "prg9",
    ]


pytest.main(args=["-q"])
