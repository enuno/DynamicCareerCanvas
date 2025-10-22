# AI Coding Agents - Universal Guidelines

This file contains centralized rules, conventions, and workflows for **all AI coding assistants** working on the DynamicCareerCanvas project.

Individual agent-specific files (CLAUDE.md, CURSOR.md, etc.) should reference this file and only override where necessary.

## Project Overview

**Name**: DynamicCareerCanvas
**Type**: Professional Portfolio & Resume Website
**Tech Stack**: Jekyll, GitHub Pages, YAML, SCSS, Vanilla JS
**Purpose**: Showcase professional experience and projects for Elvis Nuno

## Universal AI Agent Rules

### DO

✓ **Read context files first** - Always check `.ai/CONTEXT.md` before making changes
✓ **Follow existing patterns** - Match the coding style already in the project
✓ **Keep it simple** - Readable code beats clever code
✓ **Test locally** - Build the site before committing (`bundle exec jekyll build`)
✓ **Be responsive** - All changes must work on mobile
✓ **Add alt text** - All images need descriptive alt attributes
✓ **Use CSS variables** - Use existing variables like `var(--color-primary)`
✓ **Attribute AI work** - Include AI attribution in commit messages
✓ **Update docs** - Keep documentation in sync with code changes
✓ **Validate YAML** - Ensure YAML syntax is correct before committing

### DON'T

✗ **Don't add frameworks** - No React, Vue, jQuery, etc. Keep it vanilla
✗ **Don't hardcode content** - Use YAML data files in `_data/`
✗ **Don't skip mobile testing** - Always check responsive behavior
✗ **Don't ignore accessibility** - Maintain semantic HTML and ARIA labels
✗ **Don't commit secrets** - Never add API keys, tokens, or credentials
✗ **Don't break the build** - Always verify Jekyll builds successfully
✗ **Don't use inline styles** - Use SCSS files for all styling
✗ **Don't remove attribution** - Keep existing credits and licenses

## File Structure

### Content (Edit Frequently)
```
_data/
├── experience.yml    # Work experience entries
├── projects.yml      # Portfolio projects
├── skills.yml        # Technical skills
└── publications.yml  # Publications & presentations
```

### Templates (Edit Occasionally)
```
_includes/
├── components/       # Reusable UI components
├── head.html
├── header.html
└── footer.html

_layouts/
├── default.html
├── home.html
└── resume.html
```

### Styles (Edit as Needed)
```
_sass/
├── base/            # Base styles, variables
├── components/      # Component-specific styles
├── layout/          # Layout styles
└── themes/          # Theme definitions
```

### Documentation (Keep Updated)
```
.ai/                 # AI-specific documentation
docs/                # Project documentation
README.md            # Project overview
CONTRIBUTING.md      # Contribution guidelines
```

## Code Conventions

### YAML Data Files

```yaml
# Use quotes, YYYY-MM dates, consistent structure
- company: "Company Name"
  title: "Job Title"
  location: "City, State"
  start_date: "2024-01"
  end_date: "2024-08"
  current: false
  description: |
    Multi-line description here
  highlights:
    - "Achievement one"
    - "Achievement two"
  technologies:
    - "Tech 1"
    - "Tech 2"
```

### HTML/Liquid Templates

```liquid
<!-- Comment explaining what this does -->

<div class="component-name">
  <h3>{{ include.data.title }}</h3>
  <p>{{ include.data.description }}</p>
</div>
```

### SCSS Styles

```scss
// Simple, clear naming

.component-name {
  padding: var(--spacing-md);
  background: var(--color-surface);

  h3 {
    color: var(--color-primary);
  }

  @media (max-width: 768px) {
    padding: var(--spacing-sm);
  }
}
```

### JavaScript

```javascript
// Modern ES6+, vanilla JS only

const initComponent = () => {
  const elements = document.querySelectorAll('[data-component]');
  elements.forEach(el => {
    // Do something
  });
};

document.addEventListener('DOMContentLoaded', initComponent);
```

## Workflow Standards

### Making Changes

1. **Understand the context** - Read `.ai/CONTEXT.md` and relevant docs
2. **Create/checkout branch** - Use descriptive name: `feature-name` or `fix-name`
3. **Make changes** - Follow conventions, keep it simple
4. **Test locally** - `bundle exec jekyll serve --livereload`
5. **Check mobile** - Resize browser or use dev tools
6. **Validate** - Ensure YAML is valid, no build errors
7. **Commit** - Clear message with AI attribution
8. **Push** - Push to your branch
9. **PR** - Create pull request with description

### Testing Checklist

Before committing:
- [ ] Site builds without errors
- [ ] Looks correct in browser
- [ ] Works on mobile (resize to 375px)
- [ ] No JavaScript errors in console
- [ ] Links work (if modified)
- [ ] Images have alt text (if added)

### Commit Message Format

Simple and clear:

```
Add timeline to experience section

- Created visual timeline component
- Made it responsive
- Added dark mode support

AI-Assisted: [Your Name/Tool]
```

Or more formal:

```
feat: add experience timeline component

Interactive timeline showing career progression
with responsive design and dark mode support.

AI-Assisted: [Your Name/Tool]
Co-Authored-By: [AI Name] <email>
```

## Common Tasks

### Adding Work Experience

1. Open `_data/experience.yml`
2. Add entry at top (most recent first)
3. Follow existing structure
4. Test: `bundle exec jekyll build`

### Adding Project

1. Open `_data/projects.yml`
2. Add entry with all required fields
3. Add image to `assets/images/projects/` if needed
4. Set `featured: true` for homepage display

### Creating Component

1. Create `_includes/components/component-name.html`
2. Add header comment explaining usage
3. Create `_sass/components/_component-name.scss`
4. Import in `_sass/components/_index.scss`
5. Test in browser

### Updating Styles

1. Locate relevant SCSS file
2. Use existing CSS variables
3. Test in both light and dark mode
4. Check mobile responsiveness

## Error Handling

### Build Fails

```bash
# Check verbose output
bundle exec jekyll build --verbose

# Common issues:
# - YAML syntax errors
# - Missing include files
# - Invalid Liquid syntax
```

### YAML Validation

```bash
# If you have yamllint
yamllint _data/*.yml

# Or just build - Jekyll will catch errors
bundle exec jekyll build
```

## Performance Guidelines

- **Optimize images** - Use compressed formats, appropriate sizes
- **Minimize CSS/JS** - Keep bundles small
- **Lazy load** - Defer non-critical content
- **Use CSS variables** - Easier theming, better performance
- **Avoid deep nesting** - Both in SCSS and HTML

## Security Guidelines

- **No secrets in code** - Use environment variables
- **Validate input** - Even for YAML data
- **HTTPS only** - All external resources
- **Dependencies** - Keep gems updated
- **Review AI code** - Always review before committing

## Accessibility Standards

- **Semantic HTML** - Use proper elements (`nav`, `main`, `article`)
- **Alt text** - All images need descriptive text
- **Keyboard navigation** - All interactive elements accessible via keyboard
- **Color contrast** - WCAG AA minimum (4.5:1 for text)
- **ARIA labels** - Use when semantic HTML isn't enough
- **Heading hierarchy** - Proper H1-H6 structure

## AI Attribution

Always include in commits:

```
AI-Assisted: [Tool Name]
Tool: [CLI/IDE/Web]
Co-Authored-By: [AI Name] <noreply@...>
```

Update `.ai/CHANGELOG_AI.md` for significant AI contributions.

## Resources

### Project Documentation
- `.ai/CONTEXT.md` - Detailed project context
- `.ai/CONVENTIONS.md` - Coding conventions
- `.ai/PROMPTS.md` - Reusable prompts
- `DEVELOPMENT_PLAN.md` - Project roadmap

### External Resources
- Jekyll Docs: https://jekyllrb.com/docs/
- Liquid Syntax: https://shopify.github.io/liquid/
- GitHub Pages: https://docs.github.com/en/pages

## Getting Help

- **Check docs** - Read `.ai/CONTEXT.md` first
- **Build locally** - See errors in real-time
- **Ask questions** - Open GitHub Discussion
- **Report bugs** - Open GitHub Issue

## Agent-Specific Files

For tool-specific configurations, see:
- `CLAUDE.md` - Claude Code & Claude AI
- `CURSOR.md` - Cursor IDE
- `GEMINI.md` - Google Gemini
- `COPILOT.md` - GitHub Copilot
- `CLINERULES.md` - Cline
- `WINDSURF.md` - Windsurf
- `CODEX.md` - OpenAI Codex

These files reference AGENTS.md and add tool-specific details only where needed.

---

**Version**: 1.0
**Last Updated**: 2025-10-21
**Maintained By**: Elvis Nuno

**Note to AI Agents**: This is your primary reference. Read this before working on the project. Agent-specific files override only where explicitly stated.
