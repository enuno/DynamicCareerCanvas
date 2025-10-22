# Coding Conventions for AI Assistants

## General Principles

1. **Keep it simple**: Readable code beats clever code
2. **Be consistent**: Follow existing patterns when you see them
3. **Make it work first**: Optimize later if needed
4. **Comment when needed**: Explain the "why", not the "what"
5. **Attribute AI work**: Give credit where it's due

## File Organization

### Directory Structure

```
Component Files: _includes/components/component-name.html
Styles: _sass/components/_component-name.scss
Data: _data/category.yml
Pages: pages/page-name.md
Scripts: scripts/action-name.sh
```

### File Naming Conventions

| Type | Convention | Example |
|------|-----------|---------|
| YAML Data | lowercase_underscore | `experience.yml` |
| HTML Includes | lowercase-hyphen | `experience-card.html` |
| SCSS Partials | _lowercase-hyphen | `_variables.scss` |
| JavaScript | lowercase-hyphen | `scroll-animations.js` |
| Markdown Pages | lowercase-hyphen | `about-me.md` |
| Shell Scripts | lowercase-hyphen | `build-local.sh` |

## YAML Conventions

### Basic Rules

```yaml
# Just keep it consistent with existing files
- company: "Company Name"
  title: "Job Title"
  location: "City, State"
  start_date: "2024-01"
  end_date: "2024-08"
  current: false
  description: |
    Multi-line text goes here
  highlights:
    - "Bullet point one"
    - "Bullet point two"
```

### Guidelines (not strict rules)

1. **Strings**: Use quotes (double preferred, but single is fine)
2. **Dates**: `YYYY-MM` format is easiest to read
3. **Booleans**: `true` or `false` (no quotes)
4. **Multi-line**: Use `|` for longer text
5. **Order**: Recent stuff first makes sense

### Quick Check

If site builds, your YAML is probably fine:
```bash
bundle exec jekyll build
```

## HTML/Liquid Conventions

### Basic Template

```liquid
<!-- What this component does and how to use it -->

<div class="component-name">
  <h3>{{ include.data.title }}</h3>
  <p>{{ include.data.description }}</p>
</div>
```

### Simple Guidelines

1. **Add a comment** at the top explaining what it does
2. **Use descriptive class names** (component-name, not c-n-1)
3. **Use semantic HTML** when obvious (`<nav>`, `<main>`, `<article>`)
4. **Add alt text** to images
5. **Indent consistently** (2 spaces is fine)

### Accessibility Basics

Just remember:
- Alt text on images
- Proper heading hierarchy (h1, h2, h3)
- Links that make sense out of context
- Good color contrast

## SCSS Conventions

### Keep It Simple

```scss
// Styles for whatever component

.component-name {
  padding: 1rem;
  margin-bottom: 1rem;
  background: white;
  border-radius: 0.5rem;

  h3 {
    margin: 0;
    font-size: 1.25rem;
  }

  // Mobile
  @media (max-width: 768px) {
    padding: 0.5rem;
  }
}
```

### Practical Tips

1. **Use CSS variables** when they exist (like `var(--color-primary)`)
2. **Nest sparingly** - don't go too deep
3. **Mobile first** usually makes sense
4. **Group similar styles** together
5. **Add comments** for non-obvious stuff

Don't stress about perfect organization - if it works and looks good, ship it.

### CSS Variables

Define in `_sass/base/_variables.scss`:

```scss
:root {
  // Colors
  --color-primary: #2c3e50;
  --color-accent: #3498db;
  --color-surface: #ffffff;
  --color-background: #f8f9fa;
  --color-text-primary: #2c3e50;
  --color-text-secondary: #7f8c8d;

  // Spacing
  --spacing-xs: 0.25rem;
  --spacing-sm: 0.5rem;
  --spacing-md: 1rem;
  --spacing-lg: 1.5rem;
  --spacing-xl: 2rem;

  // Typography
  --font-size-sm: 0.875rem;
  --font-size-base: 1rem;
  --font-size-lg: 1.125rem;
  --font-size-xl: 1.25rem;
  --font-size-2xl: 1.5rem;

  // Shadows
  --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.1);
  --shadow-md: 0 4px 6px rgba(0, 0, 0, 0.1);
  --shadow-lg: 0 10px 15px rgba(0, 0, 0, 0.1);

  // Border radius
  --radius-sm: 0.25rem;
  --radius-md: 0.5rem;
  --radius-lg: 1rem;
}

// Dark mode
[data-theme="dark"] {
  --color-surface: #1e2a3a;
  --color-background: #0f1419;
  --color-text-primary: #e1e8ed;
  --color-text-secondary: #8899a6;
}
```

## JavaScript Conventions

### Structure

```javascript
/**
 * Scroll Animations
 * Handles fade-in animations on scroll using Intersection Observer
 */

(function() {
  'use strict';

  // Configuration
  const config = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  };

  // Initialize observer
  const observer = new IntersectionObserver(handleIntersection, config);

  /**
   * Handle element intersection
   * @param {Array} entries - Intersection observer entries
   */
  function handleIntersection(entries) {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        observer.unobserve(entry.target);
      }
    });
  }

  /**
   * Initialize animations
   */
  function init() {
    const elements = document.querySelectorAll('[data-animate]');
    elements.forEach(el => observer.observe(el));
  }

  // Run on DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
```

### Rules

1. **IIFE**: Wrap in immediately invoked function expression
2. **Strict Mode**: Use `'use strict'`
3. **JSDoc**: Document functions with comments
4. **Constants**: Use `const` by default, `let` when reassignment needed
5. **ES6+**: Use modern syntax (arrow functions, template literals)
6. **No jQuery**: Vanilla JavaScript only
7. **Progressive Enhancement**: Site works without JavaScript

## Git Conventions

### Commit Messages

Keep it simple and clear:

```
Add timeline to experience section

- Added visual timeline
- Made it responsive
- Works in dark mode
```

Or if you want to be more formal:

```
feat: add experience timeline

Interactive timeline showing career progression.

AI-Assisted: Claude Code
```

**The important parts:**
- First line describes what changed
- Add details if it's not obvious
- Mention AI if you used it

### Branch Naming

Just use a descriptive name:

```
timeline-feature
fix-mobile-nav
update-docs
redesign-homepage
```

Format doesn't matter much - clarity does.

## Documentation Conventions

### Markdown Structure

```markdown
# Page Title

Brief description of what this document covers.

## Section Title

Content for this section.

### Subsection

More detailed content.

#### Code Example

```language
code here
```

### Best Practices

- Use ATX-style headers (#)
- One blank line before/after headers
- Use fenced code blocks with language
- Link to related docs
- Keep line length under 100 characters
- Use tables for structured data
```

### Code Documentation

Always include:
1. Purpose of the code
2. Parameters and their types
3. Return values
4. Usage examples
5. Edge cases or limitations

## Testing

### Before You Commit

Quick checklist:
- [ ] Does it build? (`bundle exec jekyll build`)
- [ ] Does it look right? (Check in browser)
- [ ] Mobile okay? (Resize browser or use dev tools)

That's usually enough. Deep testing can come later.

### Quick Test

```bash
# Build and check for errors
bundle exec jekyll build

# See it in browser with auto-reload
bundle exec jekyll serve --livereload
```

If it builds and looks good, you're probably fine.

## AI Attribution

### In Commit Messages

```
<type>(<scope>): <subject>

<body>

AI-Assisted: Claude Code
Tool: Cursor IDE / CLI
Co-Authored-By: Claude <noreply@anthropic.com>
```

### In Code Comments

```html
<!--
  Component: Experience Timeline
  Created: 2025-10-21
  AI-Assisted: Claude Code

  Interactive timeline visualization of career progression
  Uses Intersection Observer for scroll animations
-->
```

```javascript
/**
 * Initialize timeline animations
 * AI-Assisted implementation using Intersection Observer API
 * Created: 2025-10-21 with Claude Code
 */
```

### In Documentation

```markdown
## Timeline Visualization

_This feature was implemented with AI assistance (Claude Code) on 2025-10-21_

The timeline component provides...
```

## Error Handling

### YAML Errors

```bash
# Always validate before committing
./scripts/validate-yaml.sh

# If errors found:
# 1. Check line number in error message
# 2. Verify indentation (2 spaces, not tabs)
# 3. Check quotes and special characters
# 4. Validate online: yamllint.com
```

### Build Errors

```bash
# Check Jekyll build output
bundle exec jekyll build --verbose

# Common issues:
# - Missing front matter
# - Invalid Liquid syntax
# - Broken includes
# - Missing files
```

## Performance Guidelines

1. **Images**: Optimize before adding (use ImageOptim, TinyPNG)
2. **CSS**: Minimize nesting, use CSS variables
3. **JavaScript**: Defer non-critical scripts
4. **Fonts**: Subset fonts, use font-display: swap
5. **Build**: Exclude unnecessary files in _config.yml

## Security Guidelines

1. **No Secrets**: Never commit API keys, tokens, passwords
2. **Dependencies**: Keep updated via Dependabot
3. **XSS**: Sanitize user input (though static site, minimal risk)
4. **HTTPS**: Always use HTTPS for external resources
5. **Validation**: Validate all data inputs

---

**Last Updated**: 2025-10-21
**Version**: 1.0
**Maintained By**: Elvis Nuno with AI assistance
