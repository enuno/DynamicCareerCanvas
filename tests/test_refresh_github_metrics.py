"""Tests for scripts/refresh_github_metrics.py.

The fetcher is passed in, so these tests exercise the real merge, validation,
and file-writing logic without network access.
"""

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import refresh_github_metrics as rgm  # noqa: E402

GOOD = {
    "stars": 290,
    "forks": 55,
    "latest_release": "v0.6.1",
    "latest_release_date": "2026-10-14",
}


class FailingFetch(Exception):
    pass


def fetch_ok(repo):
    return dict(GOOD)


def fetch_fail(repo):
    raise FailingFetch("rate limited")


class ParseReposTest(unittest.TestCase):
    def test_reads_repo_keys_in_order(self):
        text = (
            '- slug: "a"\n  repo: "enuno/one"\n'
            "- slug: b\n  repo: enuno/two\n"
            '  # repo: "commented/out"\n'
        )
        self.assertEqual(rgm.parse_repos(text), ["enuno/one", "enuno/two"])


class MergeTest(unittest.TestCase):
    def test_success_replaces_entry_and_stamps_date(self):
        previous = {"repos": {"enuno/x": {"stars": 1, "checked_at": "2020-01-01"}}}
        result, failures = rgm.merge(previous, ["enuno/x"], fetch_ok, "2026-10-15")
        self.assertEqual(failures, [])
        entry = result["repos"]["enuno/x"]
        self.assertEqual(entry["stars"], 290)
        self.assertEqual(entry["checked_at"], "2026-10-15")

    def test_failure_keeps_last_known_good_entry(self):
        previous = {"repos": {"enuno/x": {"stars": 281, "checked_at": "2026-09-01"}}}
        result, failures = rgm.merge(previous, ["enuno/x"], fetch_fail, "2026-10-15")
        self.assertEqual(failures, ["enuno/x"])
        self.assertEqual(
            result["repos"]["enuno/x"], {"stars": 281, "checked_at": "2026-09-01"}
        )

    def test_failure_without_previous_entry_omits_repo(self):
        result, failures = rgm.merge({}, ["enuno/new"], fetch_fail, "2026-10-15")
        self.assertEqual(failures, ["enuno/new"])
        self.assertNotIn("enuno/new", result["repos"])

    def test_invalid_payload_counts_as_failure(self):
        previous = {"repos": {"enuno/x": {"stars": 281, "checked_at": "2026-09-01"}}}
        for bad in ({"stars": "290"}, {"stars": -1}, {"forks": 3}, {"stars": True}):
            result, failures = rgm.merge(
                previous, ["enuno/x"], lambda repo, bad=bad: bad, "2026-10-15"
            )
            self.assertEqual(failures, ["enuno/x"], bad)
            self.assertEqual(result["repos"]["enuno/x"]["stars"], 281)

    def test_repos_no_longer_featured_are_dropped(self):
        previous = {"repos": {"enuno/old": {"stars": 5, "checked_at": "2026-01-01"}}}
        result, _ = rgm.merge(previous, ["enuno/x"], fetch_ok, "2026-10-15")
        self.assertEqual(list(result["repos"]), ["enuno/x"])

    def test_output_is_labelled_snapshot(self):
        result, _ = rgm.merge({}, ["enuno/x"], fetch_ok, "2026-10-15")
        self.assertEqual(result["source"], "snapshot")


class FileTest(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.TemporaryDirectory()
        self.path = Path(self.dir.name) / "github_metrics.json"

    def tearDown(self):
        self.dir.cleanup()

    def test_missing_or_malformed_file_loads_as_empty(self):
        self.assertEqual(rgm.load(self.path), {})
        self.path.write_text("{not json")
        self.assertEqual(rgm.load(self.path), {})

    def test_save_round_trips_and_leaves_no_temp_file(self):
        data = {"source": "snapshot", "repos": {"enuno/x": {"stars": 3}}}
        rgm.save(self.path, data)
        self.assertEqual(json.loads(self.path.read_text()), data)
        self.assertEqual([p.name for p in Path(self.dir.name).iterdir()], [self.path.name])

    def test_run_with_total_failure_preserves_file_and_exits_zero(self):
        original = {"source": "snapshot", "repos": {"enuno/x": {"stars": 281}}}
        self.path.write_text(json.dumps(original))
        code = rgm.run(self.path, ["enuno/x"], fetch_fail, "2026-10-15")
        self.assertEqual(code, 0)
        self.assertEqual(json.loads(self.path.read_text()), original)


if __name__ == "__main__":
    unittest.main()
