# Content and Metrics

How to update the homepage content, refresh GitHub metrics, build, and test.

## Where content lives

| File | Drives |
|---|---|
| `_data/profile.yml` | Hero (eyebrow, headline, intro, stack diagram layers), About bio, engineering principles, contact links |
| `_data/featured_projects.yml` | The three featured open-source projects (editorial content only) |
| `_data/github_metrics.json` | GitHub stars, forks, and latest release (generated snapshot) |
| `_data/projects.yml` | "More projects, writing, and community work" list |
| `_data/skills.yml` | Systems expertise domains |
| `_data/experience.yml` | Experience timeline (first six roles shown; the rest in "Earlier roles") |
| `_data/site.yml` | Navigation, SEO description and keywords, footer note |
| `resume.md` | The résumé page (`/resume/`) |
| `assets/files/resume.pdf` | Downloadable résumé |

The schema for featured projects is documented at the top of
`_data/featured_projects.yml`.

### Editorial rules for featured projects

- Write only claims you can point to in the repository. Add an `evidence`
  link for anything a visitor might want to check.
- Put the date a claim was checked in `status.note` or the highlight itself
  ("README, 11 Oct 2026"). Update `checked` when you re-verify.
- Keep definitions, implementation, and deployment separate. A passing test
  suite is not a deployment; stars are not adoption.
- `baseline_stars` is an owner-supplied floor. It is shown (as "N+") only when
  the snapshot has no star count for the repository.

### Experience entries

The homepage shows `summary` when present, otherwise `description`. Use
`summary` to give a short, factual line for the timeline while the full
`highlights` stay in the data. `previous_title` shows "Previously …" under the
current title.

## GitHub metrics

Metrics are a **snapshot**, not live data. The site makes no GitHub requests
from the browser, and the build makes none either.

Refresh the snapshot:

```bash
python3 scripts/refresh_github_metrics.py
# Optional: a token raises the API rate limit. It is read from the
# environment only and is never written to the snapshot.
GITHUB_TOKEN=... python3 scripts/refresh_github_metrics.py
```

The script reads the `repo:` values from `_data/featured_projects.yml` and
writes `_data/github_metrics.json` atomically. Then review and commit the
JSON.

Failure behavior:

| Situation | Result |
|---|---|
| A repository fails (network, rate limit, bad payload) | Its last-known-good entry is kept, with its old `checked_at` date |
| A repository fails and has no previous entry | It is omitted; no number is invented |
| The JSON file is missing or malformed | The page falls back to `baseline_stars` ("280+") or omits the count; the build still succeeds |
| A star count is 0 | No star count is shown |

The page always labels the number "Snapshot from GitHub, checked <date>".

## Build

CI (`.github/workflows/jekyll.yml`) builds with Ruby 3.1 and the
`github-pages` gem. Locally, either:

```bash
bundle install && bundle exec jekyll build      # needs Ruby 3.x
scripts/build-docker.sh                         # needs only Docker
```

`scripts/build-docker.sh` uses the official `ruby:3.1` image from the AWS ECR
Public mirror and caches gems in the `dcc-bundle` Docker volume.

## Tests

```bash
python3 -m unittest discover -s tests -p 'test_*.py'   # metrics script + built-site checks
node --test tests/                                     # navigation controller
```

- `tests/test_refresh_github_metrics.py`: merge, fallback, validation, and
  atomic writes of the metrics script (no network).
- `tests/test_built_site.py`: runs against `_site/` (skips if not built).
  Checks heading order, unique ids, in-page anchors, skip link, nav ARIA
  wiring, image attributes, canonical URL, structured data, and that the
  rendered star count matches the snapshot and is labeled as one.
- `tests/nav-toggle.test.js`: open/close, Escape and focus return, link and
  outside clicks.
