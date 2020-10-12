"""Dump the contents of two test files:

1. examples/dummy/taxa_and_programs.txt
2. examples/dummy/programs_db.json
"""

import random
import networkx as nx
from pathlib import Path
import regex
from collections import defaultdict
import json


def create_program(taxa, line_count=9, iterations=20):
    result = [[] for _ in range(line_count)]
    for _ in range(iterations):
        line = random.randrange(line_count)
        candidate = random.choice(taxa)
        for taxon in result[line]:
            if candidate.startswith(taxon):
                break
        else:
            if random.randrange(8) == 0 and line_count - line > 1:
                scope = random.randrange(1, line_count - line)
                candidate = f"{candidate}+{scope}"
            result[line].append(candidate)
    return ["  ".join(x) for x in result]


def dump_dummy_taxa_and_programs():
    G = nx.generators.trees.random_tree(26)
    paths = [nx.shortest_path(G, 0, node) for node in G]
    taxa = []
    for path in paths:
        taxa.append("/".join(chr(64 + i) for i in path[1:]))
    taxa.sort()
    del taxa[0]  # suppress root to get a forest
    result = []
    result.append("TAXONS")
    result.append("\n".join(taxa))
    result.append("")
    result.append("PROGRAMS")
    for i in range(1, 10):
        result.append(f"prg{i}.py")
        program = create_program(taxa)
        for (j, line) in enumerate(program, 1):
            if i == 8 and j >= 7:
                # the sloc count of prg8.py is altered by deleting its last three lines.
                break
            result.append(f"{j}   {line}")
        result.append("")
    result.append("")
    output_path = Path("examples/dummy/taxa_and_programs.txt")
    output_path.write_text("\n".join(result))


def dump_dummy_db():
    text = Path("examples/dummy/taxa_and_programs.txt").read_text()
    taxon_names = regex.search(r"(?ms)^TAXONS\n(.+?)\n\n", text)[1].split()
    program_paths_and_sources = regex.findall(r"(?ms)^(prg\d+\.py)\n(.+?)\n\n", text)
    data = {
        "programs": {
            program_path: {
                "source": source,
                "taxa": defaultdict(list),
            }
            for (program_path, source) in program_paths_and_sources
        },
        "taxa": {taxon_name: set() for taxon_name in taxon_names},
        "importations": {p: [] for (p, _) in program_paths_and_sources},
        "exportations": {p: [] for (p, _) in program_paths_and_sources},
    }
    for (program_path, source) in program_paths_and_sources:
        program = data["programs"][program_path]
        for line in source.split("\n"):
            (i, *taxa) = line.split()
            i = int(i)
            for taxon in taxa:
                (taxon_name, _, length) = taxon.partition("+")
                span = (i, i + int(length)) if length else (i, i)
                program["taxa"][taxon_name].append(span)
                data["taxa"][taxon_name].add(program_path)
    for (taxon_name, program_paths) in data["taxa"].items():
        data["taxa"][taxon_name] = sorted(program_paths)
    text = json.dumps(data, indent=2)
    text = regex.sub(r"\s*\[\s+(\d+),\s+(\d+)\s+\](,?)\s+", r"[\1,\2]\3", text)
    output_path = Path("examples/dummy/programs_db.json")
    output_path.write_text(text + "\n")


if __name__ == "__main__":
    random.seed(1)
    dump_dummy_taxa_and_programs()
    dump_dummy_db()
