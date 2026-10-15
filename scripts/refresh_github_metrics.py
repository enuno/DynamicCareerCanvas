#!/usr/bin/env python3
"""Refresh the GitHub metrics snapshot for featured projects.

Reads repository names from _data/featured_projects.yml, fetches public
metadata from the GitHub REST API, and writes _data/github_metrics.json.

The output is a snapshot, not live data. A repository that fails to fetch
(network error, rate limit, bad payload) keeps its last-known-good entry;
a repository with no previous entry is omitted. The script always exits 0,
so it can never break a build.

Usage:
    python3 scripts/refresh_github_metrics.py
    GITHUB_TOKEN=... python3 scripts/refresh_github_metrics.py   # optional, raises rate limit

The token is read from the environment on this machine only. It is never
written to the snapshot or sent anywhere but api.github.com.
"""

import datetime
import json
import os
import re
import sys
import tempfile
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROJECTS_FILE = ROOT / "_data" / "featured_projects.yml"
METRICS_FILE = ROOT / "_data" / "github_metrics.json"
API = "https://api.github.com"
REPO_LINE = re.compile(r'^\s*-?\s*repo:\s*"?([\w.-]+/[\w.-]+)"?\s*$')


def parse_repos(yaml_text):
    """Return the `repo:` values from the featured projects file, in order."""
    return [m.group(1) for m in map(REPO_LINE.match, yaml_text.splitlines()) if m]


def _get_json(url, token):
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "DynamicCareerCanvas-metrics",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=15) as resp:
        return json.load(resp)


def fetch_github(repo, token=None):
    """Fetch stars, forks, and the latest release for one repository."""
    info = _get_json(f"{API}/repos/{repo}", token)
    metrics = {"stars": info["stargazers_count"], "forks": info["forks_count"]}
    try:
        release = _get_json(f"{API}/repos/{repo}/releases/latest", token)
        metrics["latest_release"] = release["tag_name"]
        metrics["latest_release_date"] = release["published_at"][:10]
    except urllib.error.HTTPError as err:
        if err.code != 404:  # 404 means the repository has no releases
            raise
    return metrics


def _valid(metrics):
    stars = metrics.get("stars") if isinstance(metrics, dict) else None
    return isinstance(stars, int) and not isinstance(stars, bool) and stars >= 0


def merge(previous, repos, fetch, today):
    """Build a new snapshot. Return (snapshot, list of repos that failed)."""
    old = previous.get("repos", {}) if isinstance(previous, dict) else {}
    result = {"source": "snapshot", "repos": {}}
    failures = []
    for repo in repos:
        try:
            metrics = fetch(repo)
            if not _valid(metrics):
                raise ValueError(f"invalid payload: {metrics!r}")
            result["repos"][repo] = {**metrics, "checked_at": today}
        except Exception as err:  # any failure falls back to the last-known-good entry
            failures.append(repo)
            print(f"warning: {repo}: {err}; keeping previous snapshot", file=sys.stderr)
            if repo in old:
                result["repos"][repo] = old[repo]
    return result, failures


def load(path):
    try:
        return json.loads(Path(path).read_text())
    except (OSError, ValueError):
        return {}


def save(path, data):
    """Write JSON atomically so a crash never leaves a half-written file."""
    path = Path(path)
    fd, tmp = tempfile.mkstemp(dir=path.parent, suffix=".tmp")
    with os.fdopen(fd, "w") as handle:
        json.dump(data, handle, indent=2, sort_keys=True)
        handle.write("\n")
    os.replace(tmp, path)


def run(path, repos, fetch, today):
    snapshot, failures = merge(load(path), repos, fetch, today)
    save(path, snapshot)
    ok = len(repos) - len(failures)
    print(f"github metrics: {ok}/{len(repos)} refreshed -> {path}")
    return 0


def main():
    token = os.environ.get("GITHUB_TOKEN")
    repos = parse_repos(PROJECTS_FILE.read_text())
    today = datetime.date.today().isoformat()
    return run(METRICS_FILE, repos, lambda repo: fetch_github(repo, token), today)


if __name__ == "__main__":
    sys.exit(main())
