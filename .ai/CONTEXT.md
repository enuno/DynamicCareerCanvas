# Project Context for AI Assistants

## Project Overview

**Name**: DynamicCareerCanvas
**Type**: Professional Portfolio & Resume Website
**Owner**: Elvis Nuno
**Purpose**: Showcase professional experience, projects, publications, and expertise in systems architecture, DevOps, and DePIN (Decentralized Physical Infrastructure Networks) technologies.

## Tech Stack

### Core Technologies
- **Static Site Generator**: Jekyll 4.x
- **Hosting**: GitHub Pages
- **Template Engine**: Liquid
- **Styling**: SCSS/CSS3
- **JavaScript**: Vanilla JS (ES6+)
- **Data Format**: YAML

### Build & Deploy
- **CI/CD**: GitHub Actions
- **Package Manager**: Bundler (Ruby Gems)
- **Version Control**: Git
- **Dependency Management**: Dependabot

## Architecture

### Data-Driven Approach
All content is stored in YAML files in the `_data/` directory, separating content from presentation.

```
Content (YAML) → Jekyll Processing → Liquid Templates → Static HTML
```

### Key Directories

| Directory | Purpose | AI Editing Frequency |
|-----------|---------|---------------------|
| `_data/` | Content data (experience, projects, skills) | HIGH - Edit often |
| `_layouts/` | Page templates | MEDIUM - Occasional changes |
| `_includes/` | Reusable components | MEDIUM - Add components |
| `_sass/` | Styling | MEDIUM - Theme updates |
| `assets/` | Static files (images, JS, CSS) | LOW - Add assets |
| `pages/` | Site pages | LOW - New pages rare |
| `.ai/` | AI documentation | HIGH - Keep updated |
| `docs/` | Project documentation | MEDIUM - As needed |
| `scripts/` | Utility scripts | LOW - Maintenance |

## Content Structure

### Experience Data (`_data/experience.yml`)
Each work experience entry includes:
- Company name
- Job title
- Location
- Start/end dates
- Description
- Highlights (bullet points)
- Technologies used

### Projects Data (`_data/projects.yml`)
Each project entry includes:
- Name
- Description
- URL
- Featured flag
- Status
- Year
- Technologies
- Image path

### Skills Data (`_data/skills.yml`)
Categorized skills:
- Networking
- Systems Engineering
- DevOps
- Blockchain/Web3
- Leadership

### Publications Data (`_data/publications.yml`)
Publications and presentations with:
- Title
- Description/quote
- Link
- Type (publication/presentation/media)

## Key Patterns & Conventions

### File Naming
- YAML data files: lowercase with underscores (`experience.yml`)
- Include files: lowercase with hyphens (`experience-card.html`)
- Layout files: lowercase (`default.html`, `resume.html`)
- Page files: lowercase with hyphens (`about.md`, `contact-form.md`)
- Scripts: lowercase with hyphens (`validate-yaml.sh`)

### YAML Structure
```yaml
- field_name: "Value"  # Use double quotes for strings
  date_field: "YYYY-MM"  # Dates in ISO format
  boolean_field: true  # Boolean without quotes
  description: |  # Multi-line with pipe
    Multiple lines of text
    Preserved with line breaks
```

### Component Pattern
```liquid
{% include components/component-name.html
   param1=value1
   param2=value2
%}
```

### Responsive Design
- Mobile-first approach
- Breakpoints: 576px, 768px, 992px, 1200px
- Use CSS Grid and Flexbox
- Test on: iPhone, iPad, Desktop

## Common AI Tasks

### 1. Adding New Work Experience
**File**: `_data/experience.yml`

**Steps**:
1. Open `_data/experience.yml`
2. Add new entry at the top (most recent first)
3. Follow existing structure
4. Validate YAML: `./scripts/validate-yaml.sh`
5. Test locally: `./scripts/build-local.sh`

### 2. Adding New Project
**File**: `_data/projects.yml`

**Steps**:
1. Add entry to `_data/projects.yml`
2. Add project image to `assets/images/projects/`
3. Set `featured: true` for homepage display
4. Validate and test

### 3. Updating Skills
**File**: `_data/skills.yml`

**Steps**:
1. Edit appropriate category
2. Keep alphabetical order within categories
3. Use consistent formatting

### 4. Creating New Component
**Location**: `_includes/components/`

**Steps**:
1. Create `component-name.html` in `_includes/components/`
2. Use Liquid syntax for parameters
3. Add corresponding styles in `_sass/components/_component-name.scss`
4. Document usage in component file header
5. Import SCSS in `_sass/components/_index.scss`

### 5. Adding New Page
**Location**: `pages/`

**Steps**:
1. Create `page-name.md` in `pages/`
2. Add front matter with layout
3. Add to navigation if needed
4. Test routing

## Testing Commands

```bash
# Validate all YAML files
./scripts/validate-yaml.sh

# Build site locally
./scripts/build-local.sh

# Serve locally (with live reload)
bundle exec jekyll serve --livereload

# Check for broken links
./scripts/check-links.sh
```

## Development Workflow

### For Content Updates
1. Edit YAML file in `_data/`
2. Validate YAML
3. Build and preview locally
4. Commit to feature branch
5. Create PR to `develop`
6. Merge to `main` after review

### For Design Changes
1. Create feature branch
2. Edit SCSS in `_sass/`
3. Test responsively
4. Check accessibility
5. PR to `develop`

## Important Notes for AI

### DO
- Always validate YAML after editing data files
- Follow existing patterns and structure
- Update documentation when changing architecture
- Test mobile responsiveness
- Use semantic HTML
- Add comments for complex Liquid logic
- Attribute AI contributions in commit messages

### DON'T
- Don't add inline styles (use SCSS)
- Don't use JavaScript frameworks (keep it vanilla)
- Don't hardcode content in templates (use YAML data)
- Don't skip validation steps
- Don't merge without review
- Don't remove existing accessibility features

## Configuration

### Key Config Values (`_config.yml`)
- `repository`: GitHub repo path
- `name`: Site owner name
- `title`: Professional title
- `remote_theme`: Jekyll theme
- `darkmode`: Enable/disable dark mode

### Environment Variables
- `JEKYLL_ENV`: Set to `production` for builds
- `GITHUB_TOKEN`: For API access (CI/CD)

## Deployment

Site automatically deploys via GitHub Actions on push to `main`:
1. GitHub Actions triggers
2. Jekyll builds site
3. Validates output
4. Deploys to GitHub Pages
5. Live at: https://enuno.github.io/DynamicCareerCanvas/

## Resources

### Documentation
- Jekyll Docs: https://jekyllrb.com/docs/
- Liquid Syntax: https://shopify.github.io/liquid/
- GitHub Pages: https://docs.github.com/en/pages

### Project Files
- Development Plan: `DEVELOPMENT_PLAN.md`
- Contributing Guide: `CONTRIBUTING.md`
- Security Policy: `SECURITY.md`
- AI Conventions: `.ai/CONVENTIONS.md`

## Contact

**Owner**: Elvis Nuno
**Email**: enuno@proton.me
**GitHub**: @enuno

---

**Last Updated**: 2025-10-21
**Version**: 1.0
**AI Assistants**: Please update this file when project structure changes
