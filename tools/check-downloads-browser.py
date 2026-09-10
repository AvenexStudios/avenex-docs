"""Optional browser QA: pip install playwright; use installed Google Chrome."""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread

from playwright.sync_api import sync_playwright

root = Path(__file__).resolve().parents[1]
server = ThreadingHTTPServer(("127.0.0.1", 0), partial(SimpleHTTPRequestHandler, directory=str(root / "site")))
thread = Thread(target=server.serve_forever, daemon=True)
thread.start()
try:
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome", headless=True)
        for width in (390, 1440):
            page = browser.new_page(viewport={"width": width, "height": 900})
            errors = []
            page.on("pageerror", lambda error: errors.append(str(error)))
            for prefix in ("", "es/"):
                base = f"http://127.0.0.1:{server.server_port}/AvenexRaceControl/"
                page.goto(base + prefix + "versions/", wait_until="networkidle")
                page.locator("[data-avenex-downloads]").click()
                page.wait_for_url(base + prefix + "downloads/")
                assert page.locator("h1").inner_text() == ("Descargas" if prefix else "Downloads")
                assert page.locator("article table tbody tr").count() == 2
                assert page.evaluate("document.documentElement.scrollWidth <= innerWidth"), width
                links = page.locator("header a[hreflang]")
                assert links.count() == 2
                target_lang = "en" if prefix else "es"
                expected = "/AvenexRaceControl/" + ("" if prefix else "es/") + "downloads/"
                assert page.locator(f'header a[hreflang="{target_lang}"]').get_attribute("href") == expected
                page.screenshot(path=str(root / "site" / f"downloads-{prefix.strip('/') or 'en'}-{width}.png"))
            assert not errors, errors
            page.close()
        browser.close()
    print("Downloads browser QA passed: EN/ES, mobile/desktop, header navigation, no overflow or JS errors")
finally:
    server.shutdown()
    server.server_close()
    thread.join()
