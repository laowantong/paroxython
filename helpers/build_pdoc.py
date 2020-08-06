import shutil
import subprocess
from os.path import dirname
from pathlib import Path

import regex  # type: ignore

import context
from paroxython.cli.cli_tag import main as tag_program
from paroxython.goodies import add_line_numbers
from paroxython.preprocess_source import Cleanup

import draw_flow

PATH = f"{Path(dirname(__file__)).parent}"

VERSION = regex.search(r'(?<=version = ").+?(?=")', Path("pyproject.toml").read_text())[0]
print(f"Release version: {VERSION}")


def update_readme_example():
    source = Path("docs/resources/fibonacci.py").read_text().strip()
    readme_path = Path("README.md")
    readme_text = readme_path.read_text()
    (readme_text, n) = regex.subn(
        # fmt: off
        r"(?sm)^1   %%paroxython.+?(?=\n```)",
        add_line_numbers(source),
        readme_text,
        count=1,
        # fmt: on
    )
    assert n == 1, "Example program not found."
    (readme_text, n) = regex.subn(
        # fmt: off
        r"(?sm)^\| Taxon \| Lines \|.+?(?=\n\n)",
        tag_program(f"# {source}"),
        readme_text,
        count=1,
        # fmt: on
    )
    assert n == 1
    (readme_text, n) = regex.subn(r"(?<=paroxython )\S+(?= loaded)", VERSION, readme_text)
    assert n == 1
    readme_path.write_text(readme_text)


def generate_html():
    pdoc_options = " ".join(
        [
            "--force",
            "--html",
            "-c latex_math=True ",
            "-c show_source_code=True",
            "--template-dir=docs/pdoc_template",
            "--output-dir docs",
        ]
    )

    base_path = Path("docs")

    directory_names = ("cli", "docs_user_manual", "docs_developer_manual")
    for directory_name in directory_names:
        path = base_path / directory_name
        if path.is_dir():
            shutil.rmtree(path)

    subprocess.run(f"pdoc {pdoc_options} paroxython", shell=True)

    subprocess.run(f"mv -f docs/paroxython/* docs; rmdir docs/paroxython/", shell=True)


def resolve_new_types():
    data = [
        ("user_types", "source", "Source"),
        ("assess_costs", "taxon", "TaxonName"),
        ("preprocess_source", "label_name", "LabelName"),
        ("derived_labels_db", "query", "Query"),
        ("filter_programs", "operation", "Operation"),
    ]
    result = {}
    for (filename, trigger, type_name) in data:
        source = Path(f"docs/{filename}.html").read_text()
        match = regex.search(
            fr"{trigger}(?:</span> )?: (<function NewType\.<locals>\.new_type at 0x\w+?>)", source
        )
        result[type_name] = match[1]
        print(f"{match[1]} -> {type_name}")
    for path in Path("docs/").rglob("*.html"):
        source = path.read_text()
        initial_length = len(source)
        for (type_name, bad_string) in result.items():
            source = source.replace(bad_string, type_name)
        if len(source) < initial_length:
            path.write_text(source)
    for path in Path("docs/").rglob("*.html"):
        if path.name == "index.html":
            continue
        source = path.read_text()
        source = regex.sub(
            r'<a title="paroxython\.user_types\.(\w+?)" href="user_types\.html#paroxython\.user_types\.\1">\1</a>',
            r"\1",
            source,
        )
        source = source.replace("paroxython.user_types.", "")
        source = source.replace("typing_extensions.", "")
        source = source.replace("_regex.Pattern object", "regex")
        source = source.replace(PATH, ".")
        path.write_text(source)
    path = Path("docs/index.html")
    source = path.read_text()
    source = regex.sub(r"(?m)^.+paroxython\.user_types.+\n", "", source)
    (source, n) = regex.subn(
        r"""(<section>\n)(</section>\n</article>)""",
        r"""\1<h3 class="section-title" id="flow">Internal dependencies</h3>\n<p><img alt="" src="resources/flow.png"></p>\n\2""",
        source,
    )
    assert n == 1
    path.write_text(source)
    Path("docs/user_types.html").unlink()


def remove_blacklisted_sources():
    filenames = ("index.html",)
    base_path = Path("docs/")
    for filename in filenames:
        path = base_path / filename
        source = path.read_text()
        source = regex.sub(r'(?ms)^<details class="source">.+?^</details>\n', "", source)
        path.write_text(source)


def strip_docstrings():
    sub_code = regex.compile(r'(?ms)^(<pre><code class="python">)(.+?)(</code></pre>)').sub
    sub_docstrings = regex.compile(r"(?ms)^\s*r?&#34;&#34;&#34;.+?&#34;&#34;&#34;\n+").sub
    for path in Path("docs/").rglob("*.html"):
        source = path.read_text()
        source = sub_code(lambda m: m[1] + sub_docstrings("", m[2]) + m[3], source)
        source = source.replace('"git-link">Browse git</a>', '"git-link">Browse GitHub</a>')
        path.write_text(source)


def embed_code_with_line_numbers():
    path = Path("docs/index.html")
    source = path.read_text()
    embed = '<script src="https://emgithub.com/embed.js?target=https%3A%2F%2Fgithub.com%2Flaowantong%2Fparoxython%2Fblob%2Fmaster%2Fdocs%2Fresources%2Ffibonacci.py&style=github&showBorder=on&showLineNumbers=on"></script>'
    source = regex.sub(r"(?s) \(line numbers.+?</pre>", fr":</p>\n{embed}", source)
    source = source.replace("docs/resources/readme_flow.png", "resources/readme_flow.png")
    path.write_text(source)


def cleanup_index():
    for path in Path("docs/").rglob("index.html"):
        source = path.read_text()
        source = source.replace(" …", ".")
        path.write_text(source)


def insert_line_breaks():
    sub_args = regex.compile(
        r'(?m)^(<span>def <span class="ident">\w+</span></span>\(<span>.+?)(,.+\) ‑>)'
    ).sub
    sub_arg = regex.compile(r"(\w+:|\) ‑>|\*\*?\w+)").sub
    for path in Path("docs/").rglob("*.html"):
        source = path.read_text()
        source = sub_args(lambda m: m[1] + sub_arg(r"<br>\1", m[2]), source)
        path.write_text(source)


def compute_stats():
    readme_path = Path("README.md")
    readme_text = readme_path.read_text()
    cleanup = Cleanup("full")
    directories = ["paroxython", "tests", "helpers"]
    for directory in directories:
        total = 0
        for program_path in Path(directory).glob("**/*.py"):
            source = program_path.read_text()
            # Work around a weird error:
            # tokenize.TokenError: ('EOF in multi-line string', (12, 10))
            source = source.replace('if __name__ == "__main__":\n    bar = foo', "pass\npass")
            source = cleanup.run(source)
            total += source.count("\n")
        print(f"{directory}: {total} SLOC")
        total = 50 * round(total / 50)
        (readme_text, n) = regex.subn(
            fr"(?m)^(!\[{directory} SLOC\].+?)~\d+(%20SLOC)", fr"\1~{total}\2", readme_text
        )
        assert n > 0, f"Unable to create badge for '{directory}' SLOC."
    readme_path.write_text(readme_text)


def patch_prose():
    index_path = Path("docs/index.html")
    index_text = index_path.read_text()
    for title in ("cli", "User manual", "Developer manual"):
        slug = title if title == "cli" else "docs_" + title.lower().replace(" ", "_")
        path = Path("docs") / slug / "index.html"
        text = path.read_text()
        if title != "cli":
            (text, n) = regex.subn(
                f"""<h1 class="title">Module <code>paroxython.{slug}</code></h1>""",
                f"""<h1 class="title">{title}</h1>""",
                text,
            )
            assert n == 1, f"Unable to change the title of {slug}!"
            (text, n) = regex.subn(f"<h1>Index</h1>", f"<h1>{title}</h1>", text,)
            assert n == 1, f"Unable to change the title of {slug} in nav!"
            (text, n) = regex.subn(fr"""(?s)</div>\n<ul id="index">.+</ul>\n""", "", text)
            assert n == 1, f"Unable to suppress the index section in prose {slug}'s nav!"
            href = title.lower().replace(" ", "-")
            (index_text, n) = regex.subn(f"#{href}", f"{slug}/index.html", index_text)
            assert n == 1, f"Unable to patch main url for {slug}!"
            (index_text, n) = regex.subn(f"""<h1 id="{href}".+\n""", "", index_text)
            assert n == 1, f"Unable to remove section title for {slug}!"
            (index_text, n) = regex.subn(
                fr"""<li><code><a title="paroxython.{slug}".+\n""", "", index_text
            )
            assert n == 1, f"Unable to remove nav url for {slug}!"
            (index_text, n) = regex.subn(
                fr"""(?s)<dt><code class="name"><a title="paroxython\.{slug}".+?</dd>\n""",
                "",
                index_text,
            )
            assert n == 1, f"Unable to remove module section for {slug}!"
        (text, n) = regex.subn(fr"""(?s)<details class="source">.+</details>\n""", "", text)
        assert n == 1, f"Unable to suppress the source code in prose {slug}!"
        (text, n) = regex.subn("""href="index.html">""", """href="../index.html">""", text,)
        assert n == 1, f"Unable to patch the Home url in {slug}!"
        path.write_text(text)
        index_path.write_text(index_text)


def update_github_links():
    count = 2
    source = Path("tests/test_recommend_programs.py").read_text()
    path = Path("docs/md/pipeline_documentation.md")
    text = path.read_text()
    (text, n) = regex.subn(
        r"test_recommend_programs.py#L\d+-L\d+", f"test_recommend_programs.py#L-L", text
    )
    assert n == count
    for i in range(1, count + 1):
        start = source.partition(f"# extract_{i} (start)")[0].count("\n") + 2
        stop = source.partition(f"# extract_{i} (stop)")[0].count("\n")
        assert start < stop
        (text, n) = regex.subn(
            r"test_recommend_programs.py#L-L",
            f"test_recommend_programs.py#L{start}-L{stop}",
            text,
            count=1,
        )
        assert n == 1
    path.write_text(text)


def inject_flow_diagram_in_nav():
    path = Path("docs/docs_developer_manual/index.html")
    text = path.read_text()
    (text, n) = regex.subn(r"(</nav>)", r'<p><img alt="" src="../resources/flow.png"></p>\1', text)
    assert n == 1
    path.write_text(text)


def expand_repo_urls():
    for path in Path("docs/").rglob("*.html"):
        source = path.read_text()
        source = source.replace(
            "https://repo/", "https://github.com/laowantong/paroxython/blob/master/"
        )
        path.write_text(source)


def update_version_number():
    for path in ["paroxython/cli/cli_tag.py", "paroxython/cli/cli_collect.py"]:
        path = Path(path)
        source = path.read_text()
        (source, n) = regex.subn(
            r"(?<=https://github\.com/laowantong/paroxython/blob/)[^/]+", VERSION, source
        )
        assert n == 1, path
        path.write_text(source)


def link_manuals():
    index_path = Path("docs/index.html")
    index_text = index_path.read_text()
    (index_text, n) = regex.subn(
        '(<li><a href="docs_user_manual/index.html">User manual</a></li>)',
        r"""\1
        <ul>
        <li><a href="docs_user_manual/index.html#pipeline-tutorial-getting-recommendations">Pipeline tutorial</a></li>
        <li><a href="docs_user_manual/index.html#tag-databases">Tag databases</a></li>
        <li><a href="docs_user_manual/index.html#taxonomy">Taxonomy</a></li>
        <li><a href="docs_user_manual/index.html#manual-hints">Manual hints</a></li>
        <li><a href="docs_user_manual/index.html#deep-in-the-pipeline">Deep in the pipeline</a></li>
        </ul>""",
        index_text,
    )
    assert n == 1
    (index_text, n) = regex.subn(
        '(<li><a href="docs_developer_manual/index.html">Developer manual</a></li>)',
        r"""\1
        <ul>
        <li><a href="docs_developer_manual/index.html#bird-view">Bird view</a></li>
        <li><a href="docs_developer_manual/index.html#helper-programs">Helper programs</a></li>
        <li><a href="docs_developer_manual/index.html#implementation-notes">Implementation notes</a></li>
        </ul>""",
        index_text,
    )
    assert n == 1
    index_path.write_text(index_text)


def inject_taxonomy():
    """
    Data from: https://github.com/TheAlgorithms/Python
    For updating them:
    > paroxython collect -o db.sqlite Python
    > sqlite3 db.sqlite
        SELECT taxon, count(*)
        FROM taxon
        WHERE taxon LIKE 'type/%'
        GROUP BY taxon;
    Copy-paste the result below
    """
    index_path = Path("docs/docs_user_manual/index.html")
    text = index_path.read_text()
    data = """
        type/boolean|1854
        type/boolean/literal/False|193
        type/boolean/literal/True|241
        type/non_sequence/dictionary|79
        type/non_sequence/dictionary/literal|57
        type/non_sequence/dictionary/literal/empty|26
        type/non_sequence/set|57
        type/non_sequence/set/literal|6
        type/null/literal|362
        type/number/complex|1
        type/number/complex/literal|1
        type/number/floating_point|48
        type/number/floating_point/literal|292
        type/number/floating_point/literal/zero|22
        type/number/integer|198
        type/number/integer/literal|5119
        type/number/integer/literal/zero|1750
        type/sequence|54
        type/sequence/list|531
        type/sequence/list/literal|629
        type/sequence/list/literal/empty|285
        type/sequence/string|445
        type/sequence/string/literal|1938
        type/sequence/string/literal/empty|128
        type/sequence/string/literal/formatted|62
        type/sequence/tuple|7
        type/sequence/tuple/literal|891
    """
    rows = data.strip().split("\n")
    acc = []
    for row in rows:
        (taxon, count) = row.split("|")
        taxon = taxon.replace("/", " ")
        acc.append(f"['{taxon}.', {count}],")
    head = f"""
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript">
      google.charts.load('current', {{packages:['wordtree']}});
      google.charts.setOnLoadCallback(drawChart);

      function drawChart() {{
        var data = google.visualization.arrayToDataTable(
          [ ['node', 'occurrences'], {" ".join(acc)} ]
        );
        var options = {{
          wordtree: {{
            format: 'implicit',
            word: 'type'
          }}
        }};
        var chart = new google.visualization.WordTree(document.getElementById('wordtree_basic'));
        chart.draw(data, options);
      }}
    </script>
    """
    (text, n) = regex.subn("</head>", fr"{head}</head>", text)
    assert n == 1
    body = """<div id="wordtree_basic" style="width: 100%; height: 500px;"></div>"""
    (text, n) = regex.subn("<!-- Here comes the tree -->", body, text)
    assert n == 1
    index_path.write_text(text)


def main():
    update_readme_example()
    update_version_number()
    update_github_links()
    generate_html()
    expand_repo_urls()
    resolve_new_types()
    remove_blacklisted_sources()
    strip_docstrings()
    embed_code_with_line_numbers()
    cleanup_index()
    insert_line_breaks()
    patch_prose()
    inject_flow_diagram_in_nav()
    link_manuals()
    inject_taxonomy()
    compute_stats()


if __name__ == "__main__":
    main()
