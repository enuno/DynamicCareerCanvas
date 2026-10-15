"""Checks against the built site (run after `bundle exec jekyll build`).

    SITE_DIR=_site python3 -m unittest tests.test_built_site

Skips when the build output is missing. Uses only the standard library.
"""

import json
import os
import re
import unittest
from html.parser import HTMLParser
from pathlib import Path
from typing import TYPE_CHECKING

ROOT = Path(__file__).resolve().parent.parent
SITE = Path(os.environ.get("SITE_DIR", ROOT / "_site"))
METRICS = json.loads((ROOT / "_data" / "github_metrics.json").read_text())


class Page(HTMLParser):
    """Collects the elements and text these tests need."""

    def __init__(self, html):
        super().__init__()
        self.elements = []  # (tag, attrs)
        self.headings = []  # levels in document order
        self.text = []
        self._skip = 0
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.elements.append((tag, attrs))
        if re.fullmatch(r"h[1-6]", tag):
            self.headings.append(int(tag[1]))
        if tag in ("script", "style"):
            self._skip += 1

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self._skip -= 1

    def handle_data(self, data):
        if not self._skip:
            self.text.append(data)

    def all(self, tag):
        return [attrs for t, attrs in self.elements if t == tag]

    @property
    def ids(self):
        return [a["id"] for _, a in self.elements if "id" in a]

    @property
    def plain_text(self):
        return re.sub(r"\s+", " ", " ".join(self.text))


def load(rel):
    path = SITE / rel
    if not path.exists():
        raise unittest.SkipTest(f"{path} not built")
    return Page(path.read_text())


class CommonPageChecks(unittest.TestCase if TYPE_CHECKING else object):
    """Mixin: checks shared by every page. Subclasses set `rel`."""

    rel = None

    @classmethod
    def setUpClass(cls):
        cls.page = load(cls.rel)

    def test_exactly_one_h1(self):
        self.assertEqual(self.page.headings.count(1), 1)

    def test_heading_levels_do_not_skip(self):
        for prev, cur in zip(self.page.headings, self.page.headings[1:]):
            self.assertLessEqual(cur - prev, 1, self.page.headings)

    def test_ids_are_unique(self):
        ids = self.page.ids
        self.assertEqual(len(ids), len(set(ids)), [i for i in ids if ids.count(i) > 1])

    def test_skip_link_targets_main(self):
        first_link = self.page.all("a")[0]
        self.assertEqual(first_link.get("href"), "#main")
        self.assertIn("main", self.page.ids)

    def test_in_page_anchors_resolve(self):
        ids = set(self.page.ids)
        for a in self.page.all("a"):
            href = a.get("href", "")
            if href.startswith("#"):
                self.assertIn(href[1:], ids, href)

    def test_no_placeholder_links(self):
        for a in self.page.all("a"):
            href = (a.get("href") or "").strip()
            self.assertNotIn(href, ("", "#", "javascript:void(0)"), a)

    def test_new_tab_links_are_safe(self):
        for a in self.page.all("a"):
            if a.get("target") == "_blank":
                self.assertIn("noopener", a.get("rel", ""), a)

    def test_images_have_alt(self):
        for img in self.page.all("img"):
            self.assertIn("alt", img, img)
            self.assertIn("width", img, img)
            self.assertIn("height", img, img)

    def test_nav_toggle_is_wired_to_the_menu(self):
        toggles = [b for b in self.page.all("button") if "nav__toggle" in b.get("class", "")]
        self.assertEqual(len(toggles), 1)
        self.assertEqual(toggles[0].get("aria-expanded"), "false")
        self.assertIn(toggles[0].get("aria-controls"), self.page.ids)

    def test_canonical_link_present(self):
        canon = [l for l in self.page.all("link") if l.get("rel") == "canonical"]
        self.assertEqual(len(canon), 1)
        self.assertTrue(canon[0]["href"].startswith("https://enuno.github.io/"))


class HomePageTest(CommonPageChecks, unittest.TestCase):
    rel = "index.html"

    def test_flagship_stars_match_snapshot(self):
        stars = METRICS["repos"]["enuno/unifi-mcp-server"]["stars"]
        self.assertIn(f"{stars} GitHub stars", self.page.plain_text)

    def test_metrics_are_labelled_as_snapshot_not_live(self):
        text = self.page.plain_text
        self.assertIn("Snapshot from GitHub, checked", text)
        self.assertNotRegex(text, r"(?i)\blive\b (stars|metrics|count)")

    def test_only_the_flagship_shows_a_star_count(self):
        # Hero proof point + flagship metrics panel; zero-star projects show none.
        self.assertEqual(self.page.plain_text.count("GitHub stars"), 2)

    def test_featured_projects_have_anchors(self):
        for slug in ("unifi-mcp-server", "noesis-agent-stack", "noesis-ansible"):
            self.assertIn(f"project-{slug}", self.page.ids)

    def test_architecture_diagram_is_labelled_conceptual(self):
        self.assertIn("Conceptual architecture", self.page.plain_text)
        self.assertIn("not a live dashboard", self.page.plain_text)

    def test_structured_data_is_valid_json(self):
        html = (SITE / self.rel).read_text()
        blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.S)
        self.assertTrue(blocks)
        types = []
        for block in blocks:
            data = json.loads(block)
            types += [n.get("@type") for n in data.get("@graph", [data])]
        self.assertIn("Person", types)
        self.assertEqual(types.count("SoftwareSourceCode"), 3)


class ResumePageTest(CommonPageChecks, unittest.TestCase):
    rel = "resume/index.html"

    def test_pdf_link_points_to_existing_file(self):
        pdf_links = [a["href"] for a in self.page.all("a") if a.get("href", "").endswith("resume.pdf")]
        self.assertTrue(pdf_links)
        self.assertTrue((SITE / "assets" / "files" / "resume.pdf").exists())


if __name__ == "__main__":
    unittest.main()
