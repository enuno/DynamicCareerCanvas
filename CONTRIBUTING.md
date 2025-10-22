# Contributing to DynamicCareerCanvas

Thank you for your interest in contributing to DynamicCareerCanvas! This document provides guidelines and instructions for contributing to this project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Workflow](#development-workflow)
- [Branch Strategy](#branch-strategy)
- [Commit Guidelines](#commit-guidelines)
- [Pull Request Process](#pull-request-process)
- [AI-Assisted Contributions](#ai-assisted-contributions)
- [Testing](#testing)
- [Documentation](#documentation)
- [Style Guide](#style-guide)

## Code of Conduct

This project adheres to a Code of Conduct that all contributors are expected to follow. Please read [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) before contributing.

## Getting Started

### Prerequisites

- **Ruby** 3.1 or higher
- **Bundler** (Ruby gem manager)
- **Git** 2.x or higher
- **Node.js** (optional, for additional tooling)

### Initial Setup

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/YOUR-USERNAME/DynamicCareerCanvas.git
   cd DynamicCareerCanvas
   ```

3. Add the upstream repository:
   ```bash
   git remote add upstream https://github.com/enuno/DynamicCareerCanvas.git
   ```

4. Install dependencies:
   ```bash
   bundle install
   ```

5. Build and serve locally:
   ```bash
   bundle exec jekyll serve --livereload
   ```

6. Visit http://localhost:4000 to view the site

### Understanding the Project Structure

Before contributing, familiarize yourself with:
- [DEVELOPMENT_PLAN.md](DEVELOPMENT_PLAN.md) - Overall project plan
- [.ai/CONTEXT.md](.ai/CONTEXT.md) - Project context and architecture
- [.ai/CONVENTIONS.md](.ai/CONVENTIONS.md) - Coding conventions

## Development Workflow

### 1. Sync Your Fork

Before starting work, sync with upstream:

```bash
git checkout develop
git fetch upstream
git merge upstream/develop
git push origin develop
```

### 2. Create a Feature Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/bug-description
# or
git checkout -b docs/documentation-update
```

### 3. Make Your Changes

- Follow the [style guide](#style-guide)
- Write clear, concise code
- Comment complex logic
- Update documentation as needed

### 4. Test Your Changes

```bash
# Validate YAML files
./scripts/validate-yaml.sh

# Build locally
./scripts/build-local.sh

# Test in browser (mobile and desktop)
bundle exec jekyll serve --livereload
```

### 5. Commit Your Changes

Follow the [commit guidelines](#commit-guidelines).

### 6. Push to Your Fork

```bash
git push origin feature/your-feature-name
```

### 7. Create a Pull Request

Open a PR from your fork to `upstream/develop`.

## Branch Strategy

### Main Branches

- **main** - Production-ready code (protected)
- **develop** - Integration branch for features

### Supporting Branches

| Prefix | Purpose | Example |
|--------|---------|---------|
| `feature/` | New features | `feature/timeline-visualization` |
| `fix/` | Bug fixes | `fix/mobile-nav-overflow` |
| `docs/` | Documentation | `docs/update-contributing` |
| `ai/` | AI-assisted changes | `ai/redesign-homepage` |
| `refactor/` | Code refactoring | `refactor/sass-organization` |
| `test/` | Testing | `test/add-yaml-validation` |

### Branch Lifecycle

```
develop → feature/new-feature → develop → main
```

1. Create branch from `develop`
2. Make changes and commit
3. Create PR to `develop`
4. After review and approval, merge to `develop`
5. Periodically, `develop` is merged to `main` for releases

## Commit Guidelines

### Commit Message Format

Use [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types

| Type | Description |
|------|-------------|
| `feat` | New feature |
| `fix` | Bug fix |
| `docs` | Documentation only |
| `style` | Formatting, missing semicolons, etc. |
| `refactor` | Code restructuring |
| `test` | Adding tests |
| `chore` | Maintenance tasks |
| `ai` | AI-assisted changes |

### Scope

Optional, indicates what part of the codebase:
- `experience` - Work experience section
- `projects` - Projects section
- `skills` - Skills section
- `design` - Visual design
- `nav` - Navigation
- `mobile` - Mobile responsiveness
- `a11y` - Accessibility
- `perf` - Performance

### Examples

```
feat(experience): add timeline visualization component

Implemented interactive timeline showing career progression
with company logos and smooth scroll animations.
```

```
fix(mobile): resolve navigation overflow on small screens

Fixed horizontal scroll issue on devices < 375px width
by adjusting flex properties and max-width constraints.

Closes #42
```

```
docs(ai): update CONTEXT.md with data structure changes

Reflected migration to YAML-based content system in
AI context documentation.
```

```
ai(design): redesign homepage hero section

Complete redesign of hero section with:
- Animated gradient background
- Typewriter effect for tagline
- Responsive image handling
- Dark mode support

AI-Assisted: Claude Code (Sonnet 4.5)
Co-Authored-By: Claude <noreply@anthropic.com>
```

## Pull Request Process

### Before Creating a PR

Quick checks:
- [ ] Does it build without errors?
- [ ] Does it look right in the browser?
- [ ] Tested on mobile (or at least resized the browser)?
- [ ] Updated docs if you changed something major?

### PR Template

Keep it simple:

````markdown
## What changed
Brief description of what you did

## Why
Why you made this change

## Testing
- Built locally: Yes/No
- Checked in browser: Yes/No
- Mobile tested: Yes/No

## Screenshots (if UI changed)
Add images if relevant

## Notes
Anything else worth mentioning (AI used, related issues, etc.)
````

### Review Process

1. **Automated Checks**: GitHub Actions runs tests
2. **Code Review**: At least one reviewer approval required
3. **Testing**: Reviewer tests changes locally
4. **Approval**: Reviewer approves PR
5. **Merge**: Maintainer merges to `develop`
6. **Cleanup**: Delete feature branch after merge

### Addressing Feedback

- Make requested changes in new commits
- Don't force-push after review has started
- Respond to all comments
- Re-request review after changes

## AI-Assisted Contributions

This project embraces AI-assisted development. When using AI tools:

### Required Attribution

Include in commits:
```
AI-Assisted: [Tool Name and Version]
Tool: [CLI/IDE/Web]
Co-Authored-By: Claude <noreply@anthropic.com>
```

### AI Collaboration Guidelines

1. **Read AI Documentation First**
   - `.ai/CONTEXT.md` - Project context
   - `.ai/CONVENTIONS.md` - Coding standards
   - `.ai/PROMPTS.md` - Reusable prompts

2. **Use AI Branch Prefix**
   ```bash
   git checkout -b ai/feature-description
   ```

3. **Document AI Contributions**
   - Update `.ai/CHANGELOG_AI.md` for significant changes
   - Include AI attribution in commits
   - Note which AI tool was used

4. **Human Review Required**
   - All AI-generated code must be reviewed by a human
   - Test thoroughly before committing
   - Understand the code, don't blindly accept

5. **Quality Standards**
   - AI code must meet same standards as human code
   - Follow project conventions
   - Include appropriate comments
   - Pass all tests

See [docs/contributing/AI_COLLABORATION.md](docs/contributing/AI_COLLABORATION.md) for detailed guidelines.

## Testing

### Basic Testing

```bash
# Just build and serve
bundle exec jekyll serve --livereload
```

Then open http://localhost:4000 and check:
- Does it work?
- Does it look good?
- Resize browser - does mobile look okay?

### When to Test More Thoroughly

Do deeper testing when:
- Making major design changes
- Changing navigation or core functionality
- Adding complex JavaScript
- Before major releases

Otherwise, basic testing is usually fine.

## Documentation

### When to Update Documentation

Update documentation when you:
- Add new features
- Change existing behavior
- Modify project structure
- Update dependencies
- Change development workflow

### Documentation Files

| File | When to Update |
|------|----------------|
| `README.md` | Project overview, quick start changes |
| `DEVELOPMENT_PLAN.md` | Major architectural decisions |
| `.ai/CONTEXT.md` | Project structure, common tasks |
| `.ai/CONVENTIONS.md` | Coding standards |
| `.ai/PROMPTS.md` | New useful prompts |
| `docs/architecture/DECISIONS.md` | Architecture decisions |
| `CONTRIBUTING.md` | Contribution process changes |

### Documentation Style

- Use clear, concise language
- Include code examples
- Add tables for structured information
- Keep line length under 100 characters
- Use proper markdown formatting

## Style Guide

Don't overthink it. Main things:

### YAML
- Use quotes on strings
- Dates: `YYYY-MM` format
- Keep it consistent with existing files

### HTML/CSS
- Use clear, readable class names
- Add alt text to images
- Make it responsive (mobile matters)
- Use CSS variables when they exist

### JavaScript
- Modern syntax (ES6+) is fine
- Keep it simple - no heavy frameworks needed
- Make sure it works without JS too

### General
- **Indentation**: 2 spaces
- **Be consistent**: Match the existing style
- **Comment**: When code isn't obvious

If your editor has prettier or a formatter, use it. Otherwise, just keep it readable.

## Getting Help

- **Questions**: Open a Discussion on GitHub
- **Bugs**: Open an Issue with reproduction steps
- **Features**: Open an Issue describing the feature
- **Security**: Email enuno@proton.me (see SECURITY.md)

## Recognition

Contributors will be recognized in:
- GitHub contributor graph
- Release notes (for significant contributions)
- `.ai/CHANGELOG_AI.md` (for AI-assisted work)

## License

By contributing, you agree that your contributions will be licensed under the same license as the project (see [LICENSE](LICENSE)).

---

**Questions?** Feel free to ask in GitHub Discussions or open an issue.

**Thank you for contributing!**

---

**Last Updated**: 2025-10-21
**Version**: 1.0
