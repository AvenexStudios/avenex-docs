"""Validate public language parity, version consistency and generated links."""
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml

root = Path(__file__).resolve().parents[1]
project = root / "AvenexRaceControl"
docs = project / "docs"
site = root / "site" / "AvenexRaceControl"
versions = json.loads((project / "versions.json").read_text(encoding="utf-8"))
config = yaml.safe_load((project / "mkdocs.yml").read_text(encoding="utf-8"))
assert config["extra"]["product_version"] == versions["version"]
for item in [versions, *versions["modules"]]:
    assert re.fullmatch(r"\d+\.\d+\.\d+", item["version"])
    assert versions["production"] or item["version"].startswith("0.")

english = {p.relative_to(docs) for p in docs.rglob("*.md") if "es" not in p.relative_to(docs).parts}
spanish = {p.relative_to(docs / "es") for p in (docs / "es").rglob("*.md")}
assert english == spanish, (english - spanish, spanish - english)
for path in docs.rglob("*.md"):
    text = path.read_text(encoding="utf-8")
    assert not re.search(r"RULE-T\d|ADMIN-T\d|DOC-T\d|2026-\d\d-\d\d|Pending capture|owner.reported|TO-VALIDATE", text), path

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

checked = 0
for relative in english:
    route = relative.with_suffix("").as_posix()
    route = "" if route == "index" else route.removesuffix("/index") + "/"
    for language in ("en", "es"):
        prefix = "" if language == "en" else "es/"
        page = site / prefix / route / "index.html"
        parser = Links()
        rendered = page.read_text(encoding="utf-8")
        assert '<aside class="md-banner"' not in rendered, page
        header = rendered.split('<header ', 1)[1].split('</header>', 1)[0]
        assert 'avenex-header-version' in header and versions['version'] in header, page
        parser.feed(rendered)
        for target_language, target_prefix in (("en", ""), ("es", "es/")):
            assert parser.languages[target_language] == "/AvenexRaceControl/" + target_prefix + route, page
        for href in parser.links:
            url = urlsplit(href)
            if url.scheme or url.netloc or not url.path:
                continue
            path = unquote(url.path)
            if path.startswith("/AvenexRaceControl/"):
                target = site / path.removeprefix("/AvenexRaceControl/")
            elif path.startswith("/"):
                continue
            else:
                target = page.parent / path
            assert target.exists(), (page, href)
        checked += 1
print(f"Public docs OK: {checked} pages, EN/ES parity, language links and version {versions['version']}")
