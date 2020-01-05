"""These tests cannot fail, but update some snapshots for version controlling."""

import json
import time
from itertools import chain
from pathlib import Path

import pytest

import context
from paroxython.generate_labels import generate_labeled_programs, generate_labeled_sources
from paroxython.map_taxonomy import Taxonomy


def test_update_snapshots():
    # fmt: off
    DIRECTORIES = [
        "../Python/project_euler",
        "../Python/maths",
        "../Algo/programs",
    ]
    # fmt: on
    total_elapsed_time: float = 0
    for directory in DIRECTORIES:
        path = Path(directory)
        if (path / "__is_private_directory").exists():
            output_path = Path(path.parent, "snapshot_" + path.parts[-1] + ".py")
        else:
            output_path = Path("snapshots", "-".join(path.parts[-2:]) + ".py")
        start = time.perf_counter()
        acc = [result for result in generate_labeled_sources(directory)]
        total_elapsed_time += time.perf_counter() - start
        output_path.write_text("\n".join(acc))
    print(f"Total elapsed time: {total_elapsed_time:.2f} s.")


def test_update_taxon_db():
    # fmt: off
    DIRECTORIES = [
        "../Python/project_euler",
        # "../Python/maths",
        # "../Algo/programs"
    ]
    # fmt:on
    programs = chain.from_iterable(map(generate_labeled_programs, DIRECTORIES))
    taxonomy = Taxonomy()
    acc = {}
    for (path, taxons) in taxonomy(programs):
        acc[str(path)] = {name: " ".join(map(str, sorted(set(spans)))) for (name, spans) in taxons}
    output_path = Path("snapshots/taxon_db.json")
    output_path.write_text(json.dumps(acc, indent=2))
