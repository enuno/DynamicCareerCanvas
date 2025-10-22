# DynamicCareerCanvas

[![Jekyll](https://img.shields.io/badge/Jekyll-4.x-red.svg)](https://jekyllrb.com/)
[![GitHub Pages](https://img.shields.io/badge/Hosted%20on-GitHub%20Pages-blue.svg)](https://pages.github.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Professional portfolio website for Elvis Nuno, showcasing 20 years of experience in systems architecture, DevOps, and blockchain/DePIN technologies.

## 🌟 Features

- **Data-Driven**: All content in YAML files - easy to edit
- **Modern Design**: Clean, professional, responsive
- **Dark Mode**: Built-in light/dark theme support
- **AI-Friendly**: Comprehensive documentation for AI coding assistants
- **Accessible**: WCAG AA compliant
- **Fast**: Static site, optimized performance
- **SEO Optimized**: Sitemap, robots.txt, structured data
- **LLM Discovery**: llm.txt and llm-all.txt for AI crawlers

## 🚀 Quick Start

### Prerequisites

- Ruby 3.1+
- Bundler

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
│   ├── projects.yml    # Projects & publications
│   ├── skills.yml      # Technical skills
│   ├── profile.yml     # Personal info
│   └── site.yml        # Site configuration
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
│   ├── layout/         # Layout styles
│   └── themes/         # Theme definitions
├── assets/             # Static files
│   ├── css/
│   ├── js/
│   └── images/
├── scripts/            # Utility scripts
│   ├── build-local.sh
│   ├── serve-local.sh
│   ├── validate-yaml.sh
│   └── new-experience.sh
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

### Adding Projects

Edit `_data/projects.yml`:

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

Edit `_data/skills.yml` - organized by category.

### Personal Info

Edit `_data/profile.yml` for bio, contact info, social links.

## 🎨 Customization

### Colors

Edit `_sass/base/_variables.scss`:

```scss
:root {
  --color-primary: #2c3e50;
  --color-accent: #3498db;
  // ... more variables
}
```

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
# Build test
bundle exec jekyll build

# Check for errors
bundle exec jekyll build --verbose

# Serve locally
bundle exec jekyll serve --livereload
```

Check:
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