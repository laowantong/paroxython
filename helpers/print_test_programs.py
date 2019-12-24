"""Print the contents of a test file similar to tests/data/taxons_and_programs.txt.

The current version of this file was generated with a seed of 1. For testing purposes,
the sloc count of prg8 was manually altered by deleting its last three lines.
"""

import random
import networkx as nx

random.seed(1)
G = nx.generators.trees.random_tree(26)
paths = [nx.shortest_path(G, 0, node) for node in G]

taxons = []
for path in paths:
    taxons.append("/".join(chr(64 + i) for i in path[1:]) + "/")
taxons.sort()
del taxons[0]  # suppress root to get a forest
print("TAXONS")
print("\n".join(taxons))
print()


def create_program(line_count=9, iterations=20):
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


print("PROGRAMS")
for i in range(1, 10):
    print(f"prg{i}")
    program = create_program()
    for (j, line) in enumerate(program, 1):
        print(f"{j}   {line}")
    print()
print()
