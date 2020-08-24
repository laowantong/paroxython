from pathlib import Path
import sqlite3

import regex  # type: ignore

import context
from paroxython.make_db import TagDatabase

js_template = """// This file is auto-generated. Any changes here will be lost.
google.charts.load('current', {packages:['wordtree']});
google.charts.setOnLoadCallback(draw_tree);
google.charts.setOnLoadCallback(draw_full_tree);
function draw_tree() {
var data = google.visualization.arrayToDataTable(%s);
var options = {
    wordtree: {
    format: 'implicit',
    word: '•',
    },
};
var tree = new google.visualization.WordTree(document.getElementById('tree'));
tree.draw(data, options);
}
"""


def dump_trees(directory, update_database=True):
    if update_database:
        db = TagDatabase(directory, ignore_timestamps=True)
        db.write_sqlite()

    db_path = directory.parent / f"{directory.name}_db.sqlite"
    connexion = sqlite3.connect(str(db_path))  # str() for Python 3.6 compatibility
    c = connexion.cursor()

    query = "SELECT taxon, count(*) FROM taxon WHERE taxon not LIKE 'meta/sloc/%' GROUP BY taxon"
    table = c.execute(query).fetchall()
    result = [["node", "occurrences"]]
    for (taxon, count) in table:
        result.append([f"• {taxon.replace('/', ' ')}.", count])
    Path("docs/resources/tree.js").write_text(js_template % result)

    c.close()


if __name__ == "__main__":
    # Data from: https://github.com/TheAlgorithms/Python
    dump_trees(Path("../Python"), update_database=True)
