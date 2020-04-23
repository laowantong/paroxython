"""Dump the contents of two test files:

1. tests/data/dummy/taxons_and_programs.txt
2. tests/data/dummy/db.txt
"""

import random
import networkx as nx
from pathlib import Path
import regex
from collections import defaultdict
import json


def create_program(taxons, line_count=9, iterations=20):
    result = [[] for _ in range(line_count)]
    for _ in range(iterations):
        line = random.randrange(line_count)
        candidate = random.choice(taxons)
        for taxon in result[line]:
            if candidate.startswith(taxon):
                break
        else:
            if random.randrange(8) == 0 and line_count - line > 1:
                scope = random.randrange(1, line_count - line)
                candidate = f"{candidate}+{scope}"
            result[line].append(candidate)
    return ["  ".join(x) for x in result]


def dump_dummy_taxons_and_programs():
    G = nx.generators.trees.random_tree(26)
    paths = [nx.shortest_path(G, 0, node) for node in G]
    taxons = []
    for path in paths:
        taxons.append("/".join(chr(64 + i) for i in path[1:]))
    taxons.sort()
    del taxons[0]  # suppress root to get a forest
    result = []
    result.append("TAXONS")
    result.append("\n".join(taxons))
    result.append("")
    result.append("PROGRAMS")
    for i in range(1, 10):
        result.append(f"prg{i}.py")
        program = create_program(taxons)
        for (j, line) in enumerate(program, 1):
            if i == 8 and j >= 7:
                # the sloc count of prg8.py is altered by deleting its last three lines.
                break
            result.append(f"{j}   {line}")
        result.append("")
    result.append("")
    output_path = Path("tests/data/dummy/taxons_and_programs.txt")
    output_path.write_text("\n".join(result))


def dump_dummy_db():
    text = Path("tests/data/dummy/taxons_and_programs.txt").read_text()
    taxon_names = regex.search(r"(?ms)^TAXONS\n(.+?)\n\n", text)[1].split()
    program_names_and_sources = regex.findall(r"(?ms)^(prg\d+\.py)\n(.+?)\n\n", text)
    data = {
        "programs": {
            program_name: {"source": source, "taxons": defaultdict(list),}
            for (program_name, source) in program_names_and_sources
        },
        "taxons": {taxon_name: set() for taxon_name in taxon_names},
        "importations": {p: [] for (p, _) in program_names_and_sources},
        "exportations": {p: [] for (p, _) in program_names_and_sources},
    }
    for (program_name, source) in program_names_and_sources:
        program = data["programs"][program_name]
        for line in source.split("\n"):
            (i, *taxons) = line.split()
            i = int(i)
            for taxon in taxons:
                (taxon_name, _, length) = taxon.partition("+")
                span = (i, i + int(length)) if length else (i, i)
                program["taxons"][taxon_name].append(span)
                data["taxons"][taxon_name].add(program_name)
    for (taxon_name, program_names) in data["taxons"].items():
        data["taxons"][taxon_name] = sorted(program_names)
    text = json.dumps(data, indent=2)
    text = regex.sub(r"\s*\[\s+(\d+),\s+(\d+)\s+\](,?)\s+", r"[\1,\2]\3", text)
    output_path = Path("tests/data/dummy/db.json")
    output_path.write_text(text + "\n")


if __name__ == "__main__":
    random.seed(1)
    dump_dummy_taxons_and_programs()
    dump_dummy_db()
