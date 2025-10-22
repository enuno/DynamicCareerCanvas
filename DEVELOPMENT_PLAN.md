# Development Plan: DynamicCareerCanvas Rebuild

## Project Overview

**Objective**: Rebuild the DynamicCareerCanvas GitHub Pages site with:
- Modern, attractive, and dynamic design
- Easy editing workflow (Cursor IDE, VIM, CLI-friendly)
- AI coding best practices implementation
- Proper documentation and structure
- Professional portfolio presentation

**Timeline**: Phased approach over 4 sprints

---

## Phase 1: Foundation & Structure (Week 1)

### 1.1 Directory Structure Reorganization

```
DynamicCareerCanvas/
├── .github/
│   ├── workflows/
│   │   ├── jekyll.yml
│   │   ├── security-scan.yml
│   │   └── lighthouse-ci.yml
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   ├── feature_request.md
│   │   └── ai_contribution.md
│   └── PULL_REQUEST_TEMPLATE.md
├── .ai/
│   ├── CONTEXT.md              # AI context about project
│   ├── CONVENTIONS.md          # Coding conventions for AI
│   ├── PROMPTS.md              # Useful AI prompts
│   └── CHANGELOG_AI.md         # AI contribution tracking
├── docs/
│   ├── architecture/
│   │   ├── DECISIONS.md        # Architecture decision records
│   │   └── DIAGRAMS/
│   ├── contributing/
│   │   ├── CONTRIBUTING.md
│   │   ├── CODE_OF_CONDUCT.md
│   │   ├── AI_COLLABORATION.md
│   │   └── STYLE_GUIDE.md
│   └── deployment/
│       ├── DEPLOYMENT.md
│       └── TROUBLESHOOTING.md
├── _data/
│   ├── experience.yml          # Work experience data
│   ├── projects.yml            # Projects data
│   ├── skills.yml              # Skills data
│   ├── publications.yml        # Publications data
│   └── social.yml              # Social links data
├── _includes/
│   ├── head.html
│   ├── header.html
│   ├── footer.html
│   ├── nav.html
│   └── components/
│       ├── experience-card.html
│       ├── project-card.html
│       └── skill-badge.html
├── _layouts/
│   ├── default.html
│   ├── home.html
│   ├── page.html
│   └── resume.html
├── _sass/
│   ├── base/
│   ├── components/
│   ├── layout/
│   └── themes/
├── assets/
│   ├── css/
│   │   └── main.scss
│   ├── js/
│   │   ├── main.js
│   │   └── animations.js
│   └── images/
│       ├── profile/
│       ├── projects/
│       └── icons/
├── pages/
│   ├── about.md
│   ├── projects.md
│   ├── resume.md
│   └── contact.md
├── scripts/
│   ├── validate-yaml.sh
│   ├── build-local.sh
│   └── update-resume.sh
├── tests/
│   ├── yaml/
│   └── link-checker/
├── .gitignore
├── .editorconfig
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── DEVELOPMENT_PLAN.md         # This file
├── LICENSE
├── README.md
├── SECURITY.md
├── _config.yml
├── Gemfile
└── index.md
```

### 1.2 Documentation Files to Create

1. **AI-Specific Documentation**
   - `.ai/CONTEXT.md` - Project context for AI assistants
   - `.ai/CONVENTIONS.md` - Coding conventions and patterns
   - `.ai/PROMPTS.md` - Reusable prompts for common tasks
   - `.ai/CHANGELOG_AI.md` - Track AI vs human contributions

2. **Contribution Guidelines**
   - `CONTRIBUTING.md` - How to contribute
   - `docs/contributing/AI_COLLABORATION.md` - AI-human collaboration guide
   - `CODE_OF_CONDUCT.md` - Community standards
   - `SECURITY.md` - Security policies

3. **Technical Documentation**
   - `docs/architecture/DECISIONS.md` - Architecture decisions
   - `docs/deployment/DEPLOYMENT.md` - Deployment procedures
   - `README.md` - Enhanced with badges, quick start

---

## Phase 2: Branching Strategy & Workflow (Week 1-2)

### 2.1 Git Branching Model

**Main Branches:**
- `main` - Production-ready code (protected)
- `develop` - Integration branch for features

**Supporting Branches:**
- `feature/*` - New features (e.g., `feature/new-design`)
- `fix/*` - Bug fixes (e.g., `fix/mobile-layout`)
- `docs/*` - Documentation updates (e.g., `docs/add-contributing`)
- `ai/*` - AI-assisted changes (e.g., `ai/redesign-homepage`)
- `release/*` - Release preparation (e.g., `release/v2.0.0`)

### 2.2 Workflow Rules

**Branch Protection (main):**
- Require pull request reviews (1 reviewer)
- Require status checks to pass
- Require branches to be up to date
- Require signed commits (optional but recommended)
- No direct pushes to main

**Commit Message Convention:**
```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:**
- `feat` - New feature
- `fix` - Bug fix
- `docs` - Documentation only
- `style` - Formatting, missing semicolons, etc.
- `refactor` - Code restructuring
- `test` - Adding tests
- `chore` - Maintenance tasks
- `ai` - AI-assisted changes

**AI Attribution:**
```
feat(homepage): redesign hero section with dynamic animations

Implemented new hero section with:
- Animated background gradient
- Typewriter effect for tagline
- Responsive design for mobile

AI-Assisted: Claude Code
Co-Authored-By: Claude <noreply@anthropic.com>
```

---

## Phase 3: AI-Specific Practices (Week 2)

### 3.1 AI Context Files

**`.ai/CONTEXT.md` Template:**
```markdown
# Project Context for AI Assistants

## Project Overview
Portfolio website for Elvis Nuno showcasing professional experience,
projects, and expertise in systems architecture and DePIN technologies.

## Tech Stack
- Jekyll static site generator
- GitHub Pages hosting
- YAML data files for content
- Liquid templating
- SCSS for styling

## Key Patterns
1. All content data in `_data/` directory
2. Reusable components in `_includes/components/`
3. Each section has dedicated YAML file
4. Mobile-first responsive design

## Common Tasks
- Adding experience: Edit `_data/experience.yml`
- Adding project: Edit `_data/projects.yml`
- Updating skills: Edit `_data/skills.yml`

## Testing Commands
- Local build: `./scripts/build-local.sh`
- Validate YAML: `./scripts/validate-yaml.sh`
```

### 3.2 AI Collaboration Guidelines

**Best Practices:**
1. Always check `.ai/CONTEXT.md` before making changes
2. Follow conventions in `.ai/CONVENTIONS.md`
3. Document AI contributions in commit messages
4. Use `ai/*` branches for AI-assisted work
5. Human review required for all AI changes
6. Update `.ai/CHANGELOG_AI.md` monthly

### 3.3 AI-Friendly File Structure

**Principles:**
- YAML data files (easy to edit with AI/vim)
- Clear separation of content and presentation
- Consistent naming conventions
- Inline documentation for complex logic
- Schema validation for data files

---

## Phase 4: Security & Collaboration (Week 2-3)

### 4.1 Security Measures

**GitHub Security Features:**
- Dependabot enabled for dependency updates
- Security scanning (CodeQL)
- Secret scanning enabled
- Branch protection rules
- Signed commits encouraged

**`SECURITY.md` Template:**
```markdown
# Security Policy

## Reporting Vulnerabilities
Report security issues to: enuno@proton.me

## Supported Versions
| Version | Supported |
|---------|-----------|
| 2.x     | ✓         |
| 1.x     | ✗         |

## Security Practices
- Dependencies updated weekly via Dependabot
- All PRs scanned with CodeQL
- No secrets in repository
```

### 4.2 Collaboration Workflow

**Pull Request Process:**
1. Create feature branch from `develop`
2. Make changes following style guide
3. Add tests if applicable
4. Update documentation
5. Create PR with description
6. Request review
7. Address feedback
8. Merge to `develop`
9. Delete feature branch

**Review Checklist:**
- [ ] Code follows style guide
- [ ] Documentation updated
- [ ] No security vulnerabilities
- [ ] Tests pass
- [ ] AI contributions properly attributed
- [ ] YAML files validated

---

## Phase 5: Modern Design Implementation (Week 3-4)

### 5.1 Design Goals

**Visual Design:**
- Modern, clean, professional aesthetic
- Dark mode support
- Smooth animations and transitions
- Interactive elements
- Card-based layouts
- Color scheme: Professional blues/grays with accent colors

**User Experience:**
- Mobile-first responsive design
- Fast page loads (<2s)
- Accessible (WCAG 2.1 AA)
- Intuitive navigation
- Print-friendly resume view

### 5.2 Component Library

**Core Components:**
1. **Hero Section** - Animated introduction
2. **Experience Cards** - Timeline-based layout
3. **Project Showcase** - Interactive grid with filters
4. **Skills Matrix** - Categorized skill badges
5. **Publications** - Card layout with links
6. **Contact Form** - Formspree integration

### 5.3 Technology Enhancements

**Frontend:**
- Vanilla JavaScript (no heavy frameworks)
- CSS Grid & Flexbox
- CSS Custom Properties for theming
- Intersection Observer for scroll animations
- Service Worker for offline support (optional)

**Build Process:**
- SCSS compilation
- Asset minification
- Image optimization
- Lighthouse CI integration

---

## Phase 6: Content Migration (Week 4)

### 6.1 Data File Structure

**`_data/experience.yml`:**
```yaml
- company: "Centric Internet Services"
  title: "Director of Network Operations"
  location: "Missoula, Montana"
  start_date: "2024-01"
  end_date: "2024-08"
  current: false
  description: |
    Led the successful integration of two distinct ISP networks...
  highlights:
    - "Led successful integration of two ISP networks"
    - "Enhanced network reliability and performance"
    - "Advanced wireless ISP and DePIN technology"
  technologies:
    - "BGP"
    - "OSPF"
    - "Wireless ISP"
```

**`_data/projects.yml`:**
```yaml
- name: "Community ISP Handbook"
  description: "Comprehensive guide for rural communities..."
  url: "https://bsi-mt.notion.site/..."
  featured: true
  status: "published"
  year: 2023
  technologies:
    - "Documentation"
    - "Community Development"
  image: "/assets/images/projects/isp-handbook.png"
```

### 6.2 Migration Script

Create `scripts/migrate-content.sh`:
- Extract data from `_config.yml`
- Generate YAML data files
- Validate structure
- Create backup of original

---

## Phase 7: CI/CD Pipeline (Week 4)

### 7.1 GitHub Actions Workflows

**`jekyll.yml` (Build & Deploy):**
- Checkout code
- Setup Ruby
- Install dependencies
- Build Jekyll site
- Deploy to GitHub Pages
- Run on: push to main, PR to main

**`security-scan.yml`:**
- Dependency scanning
- YAML validation
- Link checking
- Security audit
- Run on: PR, weekly schedule

**`lighthouse-ci.yml`:**
- Performance testing
- Accessibility audit
- SEO check
- Best practices
- Run on: PR to main

### 7.2 Pre-commit Hooks

Create `.githooks/pre-commit`:
```bash
#!/bin/bash
# Validate YAML files
./scripts/validate-yaml.sh

# Check for secrets
git secrets --pre-commit

# Lint markdown
markdownlint **/*.md
```

---

## Implementation Timeline

### Week 1: Foundation
- [x] Analyze current structure
- [ ] Create directory structure
- [ ] Create AI documentation files
- [ ] Set up branching strategy
- [ ] Create contribution guidelines

### Week 2: Documentation & Security
- [ ] Complete all documentation files
- [ ] Set up security policies
- [ ] Configure branch protection
- [ ] Set up Dependabot
- [ ] Create issue/PR templates

### Week 3: Design & Development
- [ ] Design new theme
- [ ] Implement component library
- [ ] Create data file structure
- [ ] Migrate content to YAML files
- [ ] Implement responsive layouts

### Week 4: Testing & Deployment
- [ ] Set up CI/CD pipelines
- [ ] Performance testing
- [ ] Accessibility audit
- [ ] Cross-browser testing
- [ ] Deploy to production

---

## Success Criteria

1. **Functionality**
   - [ ] Site loads in <2 seconds
   - [ ] Mobile responsive (all devices)
   - [ ] All links functional
   - [ ] Accessibility score >90

2. **Maintainability**
   - [ ] Content editable via YAML files
   - [ ] Clear documentation for all processes
   - [ ] AI context files complete
   - [ ] Automated testing in place

3. **Collaboration**
   - [ ] Branch protection enabled
   - [ ] PR template in use
   - [ ] Security policies documented
   - [ ] AI attribution guidelines followed

4. **Design**
   - [ ] Modern, professional appearance
   - [ ] Dark mode functional
   - [ ] Smooth animations
   - [ ] Print-friendly resume view

---

## Maintenance Plan

### Daily
- Monitor GitHub Actions
- Review dependabot alerts

### Weekly
- Update dependencies
- Review analytics

### Monthly
- Content updates via YAML files
- Review and update AI changelog
- Security audit

### Quarterly
- Design refresh if needed
- Performance optimization
- Documentation review

---

## Risk Mitigation

| Risk | Impact | Mitigation |
|------|--------|------------|
| Breaking changes in dependencies | High | Pin versions, test updates |
| GitHub Pages downtime | Medium | Monitor status, have backup |
| Data loss during migration | High | Backup before changes, version control |
| Poor mobile performance | Medium | Mobile-first development, testing |
| Accessibility issues | Medium | Regular audits, automated testing |

---

## Resources

### Tools
- **Jekyll**: https://jekyllrb.com/
- **GitHub Pages**: https://pages.github.com/
- **Lighthouse CI**: https://github.com/GoogleChrome/lighthouse-ci
- **YAML Lint**: https://www.yamllint.com/

### References
- Modern Resume Theme: https://github.com/sproogen/modern-resume-theme
- Jekyll SEO Tag: https://github.com/jekyll/jekyll-seo-tag
- GitHub Actions: https://docs.github.com/en/actions

---

**Document Version**: 1.0
**Last Updated**: 2025-10-21
**Author**: Elvis Nuno (with AI assistance from Claude Code)
