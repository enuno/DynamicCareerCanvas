# GitHub Copilot Configuration

This file contains rules and context specific to **GitHub Copilot**.

**Primary Reference**: See [AGENTS.md](AGENTS.md) for universal AI agent guidelines.

## Copilot-Specific Setup

Copilot automatically reads:
- `.github/copilot-instructions.md` (if exists)
- Comments in code files
- Repository structure
- Recent edits

## Copilot Capabilities

Copilot excels at:
- **Inline code completion** - Real-time suggestions as you type
- **Boilerplate generation** - Quick scaffold of repetitive code
- **Pattern matching** - Follows patterns from your codebase
- **Comment-to-code** - Generates code from comments
- **Test generation** - Creates tests based on functions

## Project Context for Copilot

**Tech Stack**: Jekyll, Liquid, YAML, SCSS, Vanilla JavaScript
**No Frameworks**: Don't suggest React, Vue, jQuery, etc.
**Content**: Stored in YAML files in `_data/`
**Styling**: SCSS with CSS variables
**Mobile-First**: Always responsive

## Using Copilot in This Project

### Inline Completions

Copilot learns from your codebase patterns:

```scss
// Type this:
.experience-card {
  // Copilot suggests based on existing components:
  padding: var(--spacing-md);
  background: var(--color-surface);
  border-radius: var(--radius-md);
}
```

```liquid
<!-- Type this: -->
{% for exp in site.data.experience %}
  <!-- Copilot suggests: -->
  {% include components/experience-card.html experience=exp %}
{% endfor %}
```

### Comment-to-Code

Write comments describing what you want:

```javascript
// Create a function that toggles the mobile navigation menu
// Add/remove 'is-open' class from nav element
// Add/remove 'is-active' class from hamburger button
// Trap focus when menu is open

// Copilot will generate implementation
```

```scss
// Style for experience card
// Use CSS Grid for layout
// 2 columns on desktop, 1 on mobile
// Gap of 1rem between items

// Copilot will generate styles
```

### Copilot Chat

Use Copilot Chat in your editor:

```
/explain
What does this Liquid template do?

/fix
Fix the responsive layout issue in this component

/tests
Generate tests for this JavaScript function

/doc
Add JSDoc comments to this function
```

## Copilot-Specific Instructions

### YAML Files

When working in `.yml` files, Copilot should suggest:

```yaml
# Copilot learns from existing entries:
- company: "Previous Company"
  title: "Previous Title"
  # Start new entry, Copilot suggests structure:
- company: |
```

### Liquid Templates

Copilot understands Jekyll/Liquid:

```liquid
<!-- Suggest proper Liquid syntax -->
{% if include.experience.current %}
  <span class="badge">Current</span>
{% else %}
  <!-- Copilot suggests proper date handling -->
{% endif %}
```

### SCSS Files

Copilot should follow existing patterns:

```scss
// Use CSS variables from _variables.scss
.component {
  color: var(--color-text-primary);
  // Copilot suggests other variables used in project
}
```

### JavaScript Files

No framework suggestions:

```javascript
// ❌ Copilot should NOT suggest:
// import React from 'react';
// import $ from 'jquery';

// ✓ Copilot should suggest:
const toggleMenu = () => {
  document.querySelector('.nav').classList.toggle('is-open');
};
```

## Copilot Workflows

### 1. Creating New Component

```liquid
<!-- Component: Project Card
     Displays project information from YAML data
     Usage: {% include components/project-card.html project=proj %} -->

<!-- Copilot will suggest component structure based on existing components -->
```

### 2. Styling Components

```scss
// Component: Project Card
// Start typing, Copilot suggests based on other component styles

.project-card {
  // Copilot knows to use variables and BEM naming
```

### 3. Adding Functionality

```javascript
/**
 * Initialize scroll animations
 * Use Intersection Observer to fade in elements on scroll
 */
// Copilot will suggest implementation
```

### 4. YAML Data Entry

```yaml
# In _data/projects.yml
# Start new entry:
- name: "
# Copilot suggests structure from existing entries
```

## Copilot Best Practices

### DO

✓ **Accept Helpful Suggestions** - Copilot's inline suggestions save time
✓ **Review Before Accepting** - Always check what Copilot suggests
✓ **Use Comments** - Guide Copilot with descriptive comments
✓ **Follow Patterns** - Copilot learns from your code
✓ **Tab Through Options** - Copilot often has multiple suggestions

### DON'T

✗ **Blindly Accept All** - Review every suggestion
✗ **Skip Testing** - Test Copilot's code before committing
✗ **Ignore Context** - Make sure suggestions fit the project
✗ **Forget Attribution** - Credit Copilot in commits

## Copilot Chat Commands

### In VS Code / Editor

```
# Explain code
/explain How does the Jekyll build process work?

# Fix issues
/fix The mobile menu isn't closing

# Generate tests
/tests Create tests for toggleMenu function

# Optimize code
/optimize Improve performance of experience rendering

# Generate docs
/doc Add documentation to this component
```

## Training Copilot on Project Patterns

Copilot learns from:

1. **Existing code** - Write consistent patterns
2. **Comments** - Add clear comments describing intent
3. **File structure** - Organized files help Copilot understand
4. **Documentation** - README and docs inform suggestions

### Example Training

Create clear patterns Copilot can follow:

```scss
// Pattern: Component styles always use this structure
.component-name {
  // 1. Layout properties
  display: flex;

  // 2. Spacing
  padding: var(--spacing-md);

  // 3. Visual styling
  background: var(--color-surface);

  // 4. Responsive
  @media (max-width: 768px) {
    padding: var(--spacing-sm);
  }
}
```

Then Copilot will suggest similar patterns for new components.

## Copilot Attribution

Include in commits:

```
AI-Assisted: GitHub Copilot
Tool: VS Code / Cursor / JetBrains
Co-Authored-By: GitHub Copilot <noreply@github.com>
```

## Common Copilot Scenarios

### Autocomplete YAML Structure

```yaml
# Type:
- company:
# Press Tab, Copilot completes based on existing entries
```

### Generate Responsive CSS

```scss
// Type comment:
// Make this responsive for mobile, tablet, desktop
.component {
  // Copilot generates media queries
}
```

### Create Liquid Loop

```liquid
<!-- Type: -->
{% for
<!-- Copilot suggests full loop structure -->
```

### Add Event Listener

```javascript
// Type:
document.addEventListener('
// Copilot suggests common events and handlers
```

## Troubleshooting Copilot

### Copilot Suggests Frameworks

If Copilot suggests jQuery, React, etc.:

1. Reject the suggestion
2. Add comment: `// Use vanilla JavaScript only`
3. Start typing vanilla implementation
4. Copilot will adapt

### Copilot Doesn't Match Project Style

1. Open similar existing file
2. Copilot will learn from it
3. Return to your file
4. Suggestions should improve

### Copilot Suggestions Slow

1. Check file size (large files slow Copilot)
2. Restart editor
3. Check internet connection
4. Disable/re-enable Copilot

## Advanced Copilot Usage

### Multi-Line Completions

Start typing, press Tab to accept full multi-line suggestions:

```liquid
<!-- Type just the opening tag: -->
{% for exp in site.data.experience %}
<!-- Press Tab, Copilot suggests entire loop -->
```

### Alternative Suggestions

- Press `Alt+]` (or `Option+]`) for next suggestion
- Press `Alt+[` (or `Option+[`) for previous suggestion

### Copilot Labs (Experimental)

If available:
- **Explain**: Understand complex code
- **Translate**: Convert between languages
- **Brushes**: Refactor code with AI

## Integration with Jekyll

Copilot understands Jekyll patterns:

```liquid
<!-- Front matter -->
---
layout: default
title: {% raw %}{{ page.title }}{% endraw %}
---

<!-- Copilot knows Liquid syntax -->
{{ content }}
```

```ruby
# In _config.yml
# Copilot suggests valid Jekyll configuration
```

## Testing Copilot Suggestions

Always test:

```bash
# After accepting Copilot suggestions:
bundle exec jekyll build

# If errors, review Copilot's code
# Fix or reject suggestion
```

## Resources

- Copilot Docs: https://docs.github.com/copilot
- Project Instructions: `.github/copilot-instructions.md`
- Universal Rules: `AGENTS.md`
- Project Context: `.ai/CONTEXT.md`

---

**Version**: 1.0
**Last Updated**: 2025-10-21
**Compatible with**: GitHub Copilot Individual, Business, Enterprise

**Note**: See `.github/copilot-instructions.md` for repository-wide Copilot configuration.
