from pathlib import Path
import shutil
import subprocess
import regex  # type: ignore


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

    for directory_name in ("resources", "cli"):
        path = base_path / directory_name
        if path.is_dir():
            shutil.rmtree(path)

    subprocess.run(f"pdoc {pdoc_options} paroxython", shell=True)

    subprocess.run(f"mv docs/paroxython/* docs; rmdir docs/paroxython/", shell=True)


def resolve_new_types():
    data = [
        ("user_types", "source", "Source"),
        ("user_types", r"Span\]\], name", "ProgramName"),
        ("assess_costs", "taxon", "TaxonName"),
        ("map_taxonomy", "label_name", "LabelName"),
        ("derived_labels_db", "query", "Query"),
    ]
    result = {}
    for (filename, trigger, type_name) in data:
        source = Path(f"docs/{filename}.html").read_text()
        match = regex.search(
            fr"{trigger}: (<function NewType\.<locals>\.new_type at 0x\w+?>)", source
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
        source = source.replace(" -> ", " ‑> ")  # non-breaking hyphen
        source = source.replace(" —> ", " ‑> ")  # non-breaking hyphen
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


def embed_code_with_line_numbers():
    path = Path("docs/index.html")
    source = path.read_text()
    embed = '<script src="https://emgithub.com/embed.js?target=https%3A%2F%2Fgithub.com%2Flaowantong%2Fparoxython%2Fblob%2Fmaster%2Fdocs%2Ffibonacci.py&style=github&showBorder=on&showLineNumbers=on"></script>'
    source = regex.sub(r"(?s) \(line numbers.+?</pre>", fr":</p>\n{embed}", source)
    path.write_text(source)


def main():
    generate_html()
    resolve_new_types()
    remove_blacklisted_sources()
    strip_docstrings()
    embed_code_with_line_numbers()


if __name__ == "__main__":
    main()
