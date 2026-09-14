"""Validate public docs language parity, versions and generated links."""

import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml

ROOT = Path(__file__).resolve().parents[1]
PROJECTS = ("AvenexRaceControl", "CoDriverAIRaceEngineer")
PRIVATE_MARKERS = re.compile(
    r"RULE-T\d|ADMIN-T\d|DOC-T\d|DOCS-\d|RADIO-\d|ENG-\d|ENH-\d|"
    r"RE-\d|ADR-\d|2026-\d\d-\d\d|Pending capture|owner\.reported|"
    r"TO-VALIDATE|Kiro"
)
SEMVER = re.compile(r"\d+\.\d+\.\d+")


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.languages = {}

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "a" and "href" in attrs:
            self.links.append(attrs["href"])
            if attrs.get("hreflang") in ("en", "es"):
                self.languages[attrs["hreflang"]] = attrs["href"]


def read_yaml(path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def assert_version_consistency(project, versions, config):
    assert config["extra"]["product_version"] == versions["version"], project
    for item in [versions, *versions["modules"]]:
        assert SEMVER.fullmatch(item["version"]), (project, item)
        assert versions["production"] or item["version"].startswith("0."), (
            project,
            item,
        )


def markdown_pages(docs):
    english = {
        p.relative_to(docs)
        for p in docs.rglob("*.md")
        if "es" not in p.relative_to(docs).parts
    }
    spanish = {p.relative_to(docs / "es") for p in (docs / "es").rglob("*.md")}
    return english, spanish


def assert_language_parity(project, english, spanish):
    assert english == spanish, (project, english - spanish, spanish - english)


def assert_public_text(path, text):
    assert not PRIVATE_MARKERS.search(text), path


def assert_no_private_markers(docs):
    for path in docs.rglob("*.md"):
        assert_public_text(path, path.read_text(encoding="utf-8"))


def rendered_route(relative):
    route = relative.with_suffix("").as_posix()
    return "" if route == "index" else route.removesuffix("/index") + "/"


def assert_rendered_page(project_name, site, relative, language, versions):
    route = rendered_route(relative)
    prefix = "" if language == "en" else "es/"
    page = site / prefix / route / "index.html"
    parser = Links()
    rendered = page.read_text(encoding="utf-8")
    assert '<aside class="md-banner"' not in rendered, page
    header = rendered.split("<header ", 1)[1].split("</header>", 1)[0]
    assert "avenex-header-version" in header and versions["version"] in header, page
    assert 'for="__search"' not in header and 'data-md-component="search"' not in header, page
    assert "md-header__source" not in header, page
    assert "data-avenex-downloads" in header, page
    parser.feed(rendered)
    for target_language, target_prefix in (("en", ""), ("es", "es/")):
        assert parser.languages[target_language] == (
            f"/{project_name}/" + target_prefix + route
        ), page
    for href in parser.links:
        url = urlsplit(href)
        if url.scheme or url.netloc or not url.path:
            continue
        path = unquote(url.path)
        if path.startswith(f"/{project_name}/"):
            target = site / path.removeprefix(f"/{project_name}/")
        elif path.startswith("/"):
            continue
        else:
            target = page.parent / path
        assert target.exists(), (page, href)


def validate_project(project_name):
    project = ROOT / project_name
    docs = project / "docs"
    site = ROOT / "site" / project_name
    versions = json.loads((project / "versions.json").read_text(encoding="utf-8"))
    config = read_yaml(project / "mkdocs.yml")

    assert_version_consistency(project_name, versions, config)
    english, spanish = markdown_pages(docs)
    assert_language_parity(project_name, english, spanish)
    assert_no_private_markers(docs)

    checked = 0
    for relative in english:
        for language in ("en", "es"):
            assert_rendered_page(project_name, site, relative, language, versions)
            checked += 1
    return checked, versions["version"]


def assert_raises(fn):
    try:
        fn()
    except AssertionError:
        return
    raise AssertionError("expected validation failure")


def self_test():
    assert_raises(lambda: assert_language_parity("Example", {Path("index.md")}, set()))
    assert_raises(lambda: assert_public_text(Path("page.md"), "See DOCS-001"))
    assert_raises(
        lambda: assert_version_consistency(
            "Example",
            {"version": "1.0.0", "production": False, "modules": []},
            {"extra": {"product_version": "2.0.0"}},
        )
    )
    print("check-docs self-test OK: parity, private markers and versions fail closed")


def main():
    if "--self-test" in sys.argv:
        self_test()
        return

    total = 0
    versions = []
    for project in PROJECTS:
        checked, version = validate_project(project)
        total += checked
        versions.append(f"{project} {version}")
    print(
        "Public docs OK: "
        f"{total} rendered pages, EN/ES parity, language links and versions "
        + ", ".join(versions)
    )


if __name__ == "__main__":
    main()
