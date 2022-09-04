# WARNING: fails under version 0.10.0 of pdoc. Revert to version 0.9.1 in the meantime.

import shutil
import subprocess
from os.path import dirname
from pathlib import Path

import regex  # type: ignore

import context
from paroxython.cli_tag import main as tag_program
from paroxython.preprocess_source import Cleanup

PATH = f"{Path(dirname(__file__)).parent}"

VERSION = regex.search(r'(?<=version = ").+?(?=")', Path("pyproject.toml").read_text())[0]
print(f"Release version: {VERSION}")


def update_readme_example():
    source = Path("docs/resources/fibonacci.py").read_text().strip()
    readme_path = Path("README.md")
    readme_text = readme_path.read_text()
    (readme_text, n) = regex.subn(
        r"(?sm)^\| Taxon \| Lines \|.+?(?=\n\n)",
        tag_program(f"# {source}"),
        readme_text,
        count=1,
    )
    assert n == 1
    (readme_text, n) = regex.subn(r"(?<=paroxython )\S+(?= loaded)", VERSION, readme_text)
    assert n == 1
    readme_path.write_text(readme_text)


def generate_html():
    temp = {
        "user_manual": [
            "foreword_user.md",
            "preparing.md",
            "taxonomy.md",
            "pipeline_tutorial.md",
            "pipeline_documentation.md",
            "glossary.md",
        ],
        "developer_manual": [
            "bird_view.md",
            "helpers.md",
            "databases.md",
            "implementation_notes.md",
        ],
    }
    package_path = Path("paroxython")
    for (temp_folder, names) in temp.items():
        path = package_path / temp_folder
        if path.is_dir():
            shutil.rmtree(path)
        path.mkdir()
        lines = "\n\n<br>\n\n".join(f".. include:: ../../docs/md/{name}" for name in names)
        path = path / "__init__.py"
        path.write_text(f'"""\n{lines}\n"""\n')

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

    directory_names = ("cli", "user_manual", "developer_manual")
    for directory_name in directory_names:
        path = base_path / directory_name
        if path.is_dir():
            shutil.rmtree(path)

    subprocess.run(f"pdoc {pdoc_options} paroxython", shell=True)

    subprocess.run(f"mv -f docs/paroxython/* docs; rmdir docs/paroxython/", shell=True)

    for temp_folder in temp:
        path = package_path / temp_folder
        if path.is_dir():
            shutil.rmtree(path)


def resolve_new_types():
    data = [
        ("user_types", "source", "Source"),
        ("assess_costs", "taxon", "TaxonName"),
        ("preprocess_source", "label_name", "LabelName"),
        ("derived_labels_db", "query", "Query"),
        ("filter_programs", "operation", "Operation"),
        ("map_taxonomy", "label_pattern", "LabelPattern"),
    ]
    result = {}
    for (filename, trigger, type_name) in data:
        source = Path(f"docs/{filename}.html").read_text()
        match = regex.search(
            rf"{trigger}(?:</span> )?: (<function NewType\.<locals>\.new_type at 0x\w+?>)", source
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
            rf"(?m)(!\[{directory} SLOC\].+?)~\d+(%20SLOC)",
            rf"\1~{total}\2",
            readme_text,
        )
        assert n > 0, f"Unable to create badge for '{directory}' SLOC."
    total = Path("paroxython/resources/spec.md").read_text().count("#### Feature")
    (readme_text, n) = regex.subn(
        rf"(?m)(!\[spec features\].+?)-\d+(%20features)",
        rf"\1-{total}\2",
        readme_text,
    )
    assert n == 1
    total = Path("paroxython/resources/taxonomy.tsv").read_text().partition("-- EOF")[0].count("\n")
    (readme_text, n) = regex.subn(
        rf"(?m)(!\[taxonomy mappings\].+)-\d+(%20mappings)",
        rf"\1-{total}\2",
        readme_text,
    )
    assert n == 1
    readme_path.write_text(readme_text)


def patch_prose():
    index_path = Path("docs/index.html")
    index_text = index_path.read_text()
    index_text = index_text.replace("<h1>Index</h1>\n", "")
    for title in ("User manual", "Developer manual"):
        slug = title.lower().replace(" ", "_")
        path = Path("docs") / slug / "index.html"
        text = path.read_text()
        (text, n) = regex.subn(
            f"""<h1 class="title">Module <code>paroxython.{slug}</code></h1>""",
            f"""<h1 class="title">{title}</h1>""",
            text,
        )
        assert n == 1, f"Unable to change the title of {slug}!"
        (text, n) = regex.subn(
            f"<h1>Index</h1>",
            f"<h1>{title}</h1>",
            text,
        )
        assert n == 1, f"Unable to change the title of {slug} in nav!"
        (text, n) = regex.subn(rf"""(?s)</div>\n<ul id="index">.+</ul>\n""", "", text)
        assert n == 1, f"Unable to suppress the index section in prose {slug}'s nav!"
        (index_text, n) = regex.subn(
            rf"""<li><code><a title="paroxython.{slug}".+\n""", "", index_text
        )
        assert n == 1, f"Unable to remove nav url for {slug}!"
        (index_text, n) = regex.subn(
            rf"""(?s)<dt><code class="name"><a title="paroxython\.{slug}".+?</dd>\n""",
            "",
            index_text,
        )
        assert n == 1, f"Unable to remove module section for {slug}!"
        (text, n) = regex.subn(rf"""(?s)<details class="source">.+</details>\n""", "", text)
        assert n == 1, f"Unable to suppress the source code in prose {slug}!"
        (text, n) = regex.subn(
            """href="index.html">""",
            """href="../index.html">""",
            text,
        )
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
    path = Path("docs/developer_manual/index.html")
    text = path.read_text()
    (text, n) = regex.subn(r"(</nav>)", r'<p><img alt="" src="../resources/flow.png"></p>\1', text)
    assert n == 1
    path.write_text(text)


def expand_repo_urls():
    for path in Path("docs/").rglob("*.html"):
        source = path.read_text()
        source = source.replace(
            "<code>spec.md</code>",
            '<a href="https://repo/paroxython/resources/spec.md"><code>spec.md</code></a>',
        )
        source = source.replace(
            "<code>taxonomy.tsv</code>",
            '<a href="https://repo/paroxython/resources/taxonomy.tsv"><code>taxonomy.tsv</code></a>',
        )
        source = source.replace(
            "https://repo/", "https://github.com/laowantong/paroxython/blob/master/"
        )
        path.write_text(source)


def update_version_number():
    for path in ["paroxython/cli_tag.py", "paroxython/cli_collect.py"]:
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
        r'(<li><a href="#about">About</a><ul>)',
        (
            '<li><a href="user_manual/index.html">User manual</a></li>'
            "<ul>"
            '<li><a href="user_manual/index.html#how-to-read-this-manual">How to read this manual</a></li>'
            '<li><a href="user_manual/index.html#preparing-your-program-collection">Preparing your program collection</a></li>'
            '<li><a href="user_manual/index.html#taxonomy">Taxonomy</a></li>'
            '<li><a href="user_manual/index.html#pipeline-tutorial">Pipeline tutorial</a></li>'
            '<li><a href="user_manual/index.html#pipeline-documentation">Pipeline documentation</a></li>'
            '<li><a href="user_manual/index.html#glossary">Glossary</a></li>'
            "</ul>"
            '<li><a href="developer_manual/index.html">Developer manual</a></li>'
            "<ul>"
            '<li><a href="developer_manual/index.html#bird-view">Bird view</a></li>'
            '<li><a href="developer_manual/index.html#helper-programs">Helper programs</a></li>'
            '<li><a href="developer_manual/index.html#tag-databases">Tag databases</a></li>'
            '<li><a href="developer_manual/index.html#implementation-notes">Implementation notes</a></li>'
            "</ul>"
            r"\1"
        ),
        index_text,
    )
    assert n == 1
    (index_text, n) = regex.subn(r'\b(src|href)="docs/', r'\1="', index_text)
    assert n == 2
    index_path.write_text(index_text)


def inject_taxonomy():
    index_path = Path("docs/user_manual/index.html")
    text = index_path.read_text()
    tree = Path("docs/resources/tree.js").read_text()
    head = f"""
        <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
        <script type="text/javascript">{tree}</script>
    """
    (text, n) = regex.subn("</head>", rf"{head}</head>", text)
    assert n == 1
    index_path.write_text(text)


def disable_cli_code_syntax_hightlighting():
    base_path = Path("docs")
    for path in base_path.glob("cli*.html"):
        print(path)
        source = path.read_text()
        source = regex.sub('(?s)<code class="plain">(.+?)</code>', r"\1", source)
        path.write_text(source)


def main():
    update_readme_example()
    update_version_number()
    update_github_links()
    generate_html()
    expand_repo_urls()
    resolve_new_types()
    remove_blacklisted_sources()
    strip_docstrings()
    cleanup_index()
    insert_line_breaks()
    patch_prose()
    inject_flow_diagram_in_nav()
    link_manuals()
    inject_taxonomy()
    disable_cli_code_syntax_hightlighting()
    compute_stats()


if __name__ == "__main__":
    main()
