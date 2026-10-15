# DynamicCareerCanvas

[![Jekyll](https://img.shields.io/badge/Jekyll-4.x-red.svg)](https://jekyllrb.com/)
[![GitHub Pages](https://img.shields.io/badge/Hosted%20on-GitHub%20Pages-blue.svg)](https://pages.github.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Professional portfolio of Elvis Nuno: infrastructure and systems engineer, open-source maintainer, and builder of governed AI-agent infrastructure.

## 🌟 Features

- **Data-Driven**: All content in YAML files - easy to edit
- **Featured open source**: UniFi MCP Server, Noesis Agent Stack, and Noesis Ansible, with GitHub metrics from a cached snapshot (see [docs/CONTENT.md](docs/CONTENT.md))
- **Editorial design**: Charcoal/slate with a teal accent, system fonts, no external requests
- **Dark Mode**: Follows the system theme, with a manual toggle
- **AI-Friendly**: Comprehensive documentation for AI coding assistants
- **Accessible**: WCAG AA compliant
- **Fast**: Static site, optimized performance
- **SEO Optimized**: Sitemap, robots.txt, structured data
- **LLM Discovery**: llm.txt and llm-all.txt for AI crawlers

## 🚀 Quick Start

### Prerequisites

- Ruby 3.1+ and Bundler, **or** Docker (`scripts/build-docker.sh`)
- Python 3 and Node.js for the tests

### Local Development

```bash
# Install dependencies
bundle install

# Serve with live reload
./scripts/serve-local.sh
# or
bundle exec jekyll serve --livereload

# Build site
./scripts/build-local.sh
# or
bundle exec jekyll build
```

Visit http://localhost:4000

## 📂 Project Structure

```
DynamicCareerCanvas/
├── _data/              # Content (YAML files)
│   ├── experience.yml  # Work experience
│   ├── featured_projects.yml  # Three featured open-source projects
│   ├── github_metrics.json    # GitHub metrics snapshot (generated)
│   ├── projects.yml    # Other projects & publications
│   ├── skills.yml      # Expertise domains
│   ├── profile.yml     # Hero, bio, principles, contact
│   └── site.yml        # Navigation, SEO, footer
├── _includes/          # Reusable templates
│   ├── components/     # UI components
│   ├── head.html
│   ├── header.html
│   └── footer.html
├── _layouts/           # Page layouts
│   ├── default.html
│   ├── home.html
│   └── page.html
├── _sass/              # Styles (SCSS)
│   ├── base/           # Variables, reset, utilities
│   ├── components/     # Component styles
│   └── layout/         # Layout styles
├── assets/             # Static files
│   ├── css/
│   ├── js/
│   └── images/
├── scripts/            # Utility scripts
│   ├── build-local.sh
│   ├── build-docker.sh # Build in a Ruby 3.1 container
│   ├── refresh_github_metrics.py
│   ├── serve-local.sh
│   ├── validate-yaml.sh
│   └── new-experience.sh
├── tests/              # Metrics, built-site, and navigation tests
├── .ai/                # AI assistant documentation
│   ├── CONTEXT.md
│   ├── CONVENTIONS.md
│   ├── PROMPTS.md
│   └── CHANGELOG_AI.md
├── docs/               # Project documentation
├── AGENTS.md           # Universal AI agent rules
├── CLAUDE.md           # Claude-specific config
├── CURSOR.md           # Cursor-specific config
├── COPILOT.md          # Copilot-specific config
├── sitemap.xml         # SEO sitemap
├── robots.txt          # Crawler instructions
├── llm.txt             # LLM discovery (summary)
└── llm-all.txt         # LLM discovery (complete)
```

## 📝 Editing Content

### Adding Work Experience

Edit `_data/experience.yml`:

```yaml
- company: "Company Name"
  title: "Job Title"
  location: "City, State"
  start_date: "2024-01"
  end_date: "2024-08"  # or null if current
  current: false
  description: |
    Your description here
  highlights:
    - "Achievement 1"
    - "Achievement 2"
  technologies:
    - "Tech 1"
    - "Tech 2"
```

Or use the helper script:
```bash
./scripts/new-experience.sh
```

### Featured Projects and GitHub Metrics

Edit `_data/featured_projects.yml` (schema at the top of the file). Refresh
the metrics snapshot with `python3 scripts/refresh_github_metrics.py`. See
[docs/CONTENT.md](docs/CONTENT.md) for the editorial rules and fallback
behavior.

### Adding Projects

Edit `_data/projects.yml` (the "More projects, writing, and community work" list):

```yaml
- name: "Project Name"
  type: "project"  # project, publication, presentation, media, advisory
  featured: true
  year: 2024
  status: "completed"
  description: "Project description"
  url: "https://..."
  technologies:
    - "Tech 1"
```

### Updating Skills

Edit `_data/skills.yml`: a few domains, each with a summary and a tool list.

### Personal Info

Edit `_data/profile.yml` for the hero, bio, principles, contact info, and social links.

## 🎨 Customization

### Colors

Edit the theme mixins in `_sass/base/_variables.scss` (`theme-dark` and
`theme-light` share token names). See [DESIGNSYSTEM.md](DESIGNSYSTEM.md) for
the tokens and measured contrast.

### Components

Create new components in `_includes/components/` and add styles in `_sass/components/`.

## 🤖 AI Assistant Support

This project is optimized for AI coding assistants:

- **AGENTS.md** - Universal rules for all AI agents
- **CLAUDE.md** - Claude Code specific
- **CURSOR.md** - Cursor IDE specific
- **COPILOT.md** - GitHub Copilot specific
- **GEMINI.md** - Google Gemini specific
- **CLINERULES.md** - Cline specific
- **.ai/** directory - Detailed AI context and conventions

### Using AI Assistants

1. AI reads `AGENTS.md` and tool-specific file
2. Reviews `.ai/CONTEXT.md` for project details
3. Follows `.ai/CONVENTIONS.md` for code style
4. Uses `.ai/PROMPTS.md` for common tasks

## 🔧 Utility Scripts

```bash
# Build site
./scripts/build-local.sh

# Serve with live reload
./scripts/serve-local.sh

# Validate YAML files
./scripts/validate-yaml.sh

# Generate experience entry template
./scripts/new-experience.sh
```

## 🚢 Deployment

Automated via GitHub Actions:

1. Push to `main` branch
2. GitHub Actions builds Jekyll site
3. Deploys to GitHub Pages
4. Live in ~2 minutes

## 📊 SEO & Discovery

- **sitemap.xml** - Search engine sitemap
- **robots.txt** - Crawler instructions
- **llm.txt** - Summary for AI/LLM crawlers
- **llm-all.txt** - Complete profile for AI/LLM crawlers

## 🔍 Testing

```bash
# Build (or: scripts/build-docker.sh)
bundle exec jekyll build

# Automated checks (built-site checks run against _site/)
python3 -m unittest discover -s tests -p 'test_*.py'
node --test tests/

# Serve locally
bundle exec jekyll serve --livereload
```

Also check manually:
- ✅ Builds without errors
- ✅ Looks good in browser
- ✅ Mobile responsive (resize to ~375px)
- ✅ Dark mode works
- ✅ Links function
- ✅ Images load

## 📄 Documentation

- **DEVELOPMENT_PLAN.md** - Overall project roadmap
- **CODE_DEVELOPMENT_PLAN.md** - Coding guidelines
- **CONTRIBUTING.md** - How to contribute
- **DESIGNSYSTEM.md** - Visual design standards
- **SECURITY.md** - Security policies

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

This is primarily a personal project, but suggestions and improvements are welcome!

## 📜 License

MIT License - see [LICENSE](LICENSE) file.

## 🙏 Acknowledgments

- Built with [Jekyll](https://jekyllrb.com/)
- Hosted on [GitHub Pages](https://pages.github.com/)
- Developed with AI assistance from Claude Code

## 📬 Contact

**Elvis Nuno**
- Email: enuno@proton.me
- Phone: +1 (406) 519-9696
- LinkedIn: [elvis-nuno-5635914](https://linkedin.com/in/elvis-nuno-5635914)
- GitHub: [@enuno](https://github.com/enuno)

---

**Last Updated**: 2025-10-21
**Version**: 2.0
**Status**: Active Development

Built with ❤️ using Jekyll, GitHub Pages, and AI collaboration