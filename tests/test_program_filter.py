from collections import defaultdict
from pathlib import Path

import pytest
import regex

import context
from paroxython.program_filter import ProgramFilter

text = Path("tests/data/taxons_and_programs.txt").read_text()

taxon_names = regex.search(r"(?ms)^TAXONS\n(.+?)\n\n", text)[1].split()
programs = regex.findall(r"(?ms)^(program_\d+)\n(.+?)\n\n", text)

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
    assert f.result == [
        "program_1",
        "program_2",
        "program_3",
        "program_4",
        "program_5",
        "program_6",
        "program_7",
        "program_8",
        "program_9",
    ]


def test_filter_blacklisted_programs():
    f.reset()
    f.filter_blacklisted_programs(["program_[1-5]$"])
    print(f.result)
    assert f.result == ["program_6", "program_7", "program_8", "program_9"]


def test_filter_mandatory_taxons():
    f.reset()
    f.filter_mandatory_taxons(["O/$", "O/C/F/U/$"])
    print(f.result)
    assert f.result == ["program_3", "program_4", "program_7"]


def test_filter_forbidden_taxons():
    f.reset()
    f.filter_forbidden_taxons(["O/$", "O/C/F/U/$"])
    print(f.result)
    assert f.result == ["program_1", "program_5"]


def test_get_taxons_in_programs():
    f.reset()
    result = f.get_taxons_in_programs(["program_[1-3]$"])
    print(result)
    assert result == [
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
    ]


def test_get_taxons_not_in_programs():
    result = f.get_taxons_not_in_programs(["program_[1-3]$"])
    print(result)
    assert result == ["O/C/F/", "X/S/M/L/R/D/A/"]


def test_get_extra_taxon_names():
    f.reset()
    result = f.get_extra_taxon_names(["O", "X"])
    print(result)
    assert result == {
        "program_1": ["Y/T/", "Y/T/Q/", "Y/"],
        "program_2": ["Y/T/Q/", "Y/", "Y/T/"],
        "program_3": ["Y/T/", "Y/", "Y/E/"],
        "program_4": ["Y/T/", "Y/T/Q/", "Y/"],
        "program_5": [],
        "program_6": ["Y/T/Q/", "Y/T/", "Y/E/"],
        "program_7": ["Y/E/", "Y/T/Q/", "Y/T/"],
        "program_8": ["Y/E/"],
        "program_9": ["Y/", "Y/T/Q/", "Y/E/", "Y/T/"],
    }


def test_sort_by_extra_taxon_count():
    f.reset()
    f.sort_by_extra_taxon_count(["O", "X"])
    print(f.result)
    assert f.result == [
        "program_5",  # no extra taxon, see test_get_extra_taxon_names()
        "program_8",  # 2 extra taxons
        "program_1",  # 3 extra taxons
        "program_2",
        "program_3",
        "program_4",
        "program_6",
        "program_7",
        "program_9",  # 4 extra taxons
    ]


def test_get_lacking_taxon_patterns():
    f.reset()
    result = f.get_lacking_taxon_patterns(["O/$", "O/C/H/$", "O/C/F/U/$"])
    print(result)
    assert result == {
        "program_1": ["O/$", "O/C/H/$", "O/C/F/U/$"],
        "program_2": ["O/C/H/$", "O/C/F/U/$"],
        "program_3": [],
        "program_4": ["O/C/H/$"],
        "program_5": ["O/$", "O/C/F/U/$"],
        "program_6": ["O/$", "O/C/H/$"],
        "program_7": ["O/C/H/$"],
        "program_8": ["O/$", "O/C/H/$"],
        "program_9": ["O/C/F/U/$"],
    }


def test_sort_by_lacking_taxon_count():
    f.reset()
    f.sort_by_lacking_taxon_count(["O/$", "O/C/H/$", "O/C/F/U/$"])
    print(f.result)
    assert f.result == [
        "program_3",  # program_3 has all the wanted taxons
        "program_4",  # 1 taxon is lacking
        "program_7",
        "program_9",
        "program_2",
        "program_5",
        "program_6",
        "program_8",
        "program_1",  # 3 taxons are lacking
    ]


def test_sort_by_distance():
    f.reset()
    taxon_names = [name + "$" for name in db["programs"]["program_3"]["taxons"]]
    lacking = f.get_lacking_taxon_patterns(taxon_names)
    print(lacking)
    assert lacking == {
        "program_1": [
            "X/S/M/L/V/$",
            "O/C/H/B/$",
            "O/C/F/U/$",
            "O/C/H/$",
            "O/$",
            "Y/E/$",
        ],
        "program_2": [
            "X/K/$",
            "O/J/$",
            "O/C/F/U/$",
            "O/C/H/$",
            "X/S/$",
            "X/S/M/L/$",
            "Y/E/$",
        ],
        "program_3": [],
        "program_4": ["X/K/$", "X/S/M/L/V/$", "O/J/$", "X/S/M/$", "O/C/H/$", "Y/E/$"],
        "program_5": [
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
        "program_6": [
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
        "program_7": ["O/N/P/$", "X/S/M/L/V/$", "O/C/H/$", "Y/$"],
        "program_8": [
            "Y/T/$",
            "X/S/M/L/R/$",
            "X/S/M/$",
            "O/C/H/$",
            "X/S/$",
            "Y/$",
            "O/$",
        ],
        "program_9": ["O/N/P/$", "O/C/H/B/$", "O/C/F/U/$", "X/S/$", "X/S/M/L/$"],
    }
    extra = f.get_extra_taxon_names(taxon_names)
    print(extra)
    assert extra == {
        "program_1": ["X/W/", "X/", "Y/T/Q/", "X/S/M/L/R/D/", "O/N/"],
        "program_2": ["Y/T/Q/", "X/S/M/L/R/D/", "O/C/", "X/G/", "O/C/H/B/I/"],
        "program_3": [],
        "program_4": ["X/", "Y/T/Q/", "X/S/M/L/R/D/A/", "X/G/", "X/S/M/L/R/D/"],
        "program_5": ["O/C/H/B/I/", "O/N/", "X/", "X/S/M/L/R/D/A/", "O/C/", "O/C/F/"],
        "program_6": [
            "X/",
            "O/N/",
            "Y/T/Q/",
            "X/W/",
            "O/C/",
            "X/S/M/L/R/D/A/",
            "O/C/F/",
            "O/C/H/B/I/",
        ],
        "program_7": ["O/N/", "Y/T/Q/", "X/", "O/C/H/B/I/", "X/S/M/L/R/D/"],
        "program_8": ["X/W/", "O/C/", "O/N/", "X/S/M/L/R/D/A/", "X/S/M/L/R/D/"],
        "program_9": ["X/W/", "O/N/", "Y/T/Q/", "O/C/H/B/I/", "O/C/F/"],
    }
    f.sort_by_distance(taxon_names)
    print(f.result)
    assert f.result == [
        "program_3",  # 0 lacking and 0 extra taxons
        "program_7",  # 4             5
        "program_9",  # 5             5
        "program_1",  # 6             5
        "program_4",  # 6             5
        "program_2",  # 7             5
        "program_8",  # 7             5
        "program_5",  # 9             6
        "program_6",  # 9             8
    ]


def test_sort_by_taxon_count():
    f.reset()
    f.sort_by_taxon_count()
    print(f.result)
    assert f.result == [
        "program_5",
        "program_2",
        "program_8",
        "program_1",
        "program_4",
        "program_6",
        "program_3",
        "program_9",
        "program_7",
    ]
    counts = [len(db["programs"][program_name]["taxons"]) for program_name in f.result]
    print(counts)
    assert counts == [12, 13, 13, 14, 14, 14, 15, 15, 16]


def test_sort_by_line_count():
    f.reset()
    f.sort_by_line_count()
    print(f.result)
    assert f.result == [
        "program_8",
        "program_1",
        "program_2",
        "program_3",
        "program_4",
        "program_5",
        "program_6",
        "program_7",
        "program_9",
    ]


pytest.main(args=["-q"])
