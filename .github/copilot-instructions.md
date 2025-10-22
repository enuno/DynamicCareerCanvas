# GitHub Copilot Instructions

Repository-wide instructions for GitHub Copilot.

## Project Type
Jekyll static site generator for professional portfolio

## Tech Stack
- Jekyll 4.x
- Liquid templating
- YAML data files (_data/)
- SCSS styling with CSS variables
- Vanilla JavaScript (ES6+)
- GitHub Pages hosting

## Critical Rules

### Always Follow
- NO JavaScript frameworks (React, Vue, Angular, jQuery, etc.)
- Content comes from YAML files, never hardcoded
- Use CSS variables from _sass/base/_variables.scss
- Mobile-first responsive design
- Support light and dark modes
- Maintain accessibility (WCAG AA)
- Test builds before suggesting: `bundle exec jekyll build`

### File Patterns

**YAML Data** (_data/*.yml):
```yaml
- field: "Value in quotes"
  date: "YYYY-MM"
  description: |
    Multi-line with pipe
  list:
    - "Item one"
    - "Item two"
```

**Liquid Templates** (_includes/, _layouts/):
```liquid
<!-- Comment explaining component -->
<div class="component-name">
  {{ include.data.field }}
</div>
```

**SCSS** (_sass/):
```scss
.component-name {
  padding: var(--spacing-md);
  background: var(--color-surface);

  @media (max-width: 768px) {
    padding: var(--spacing-sm);
  }
}
```

**JavaScript** (assets/js/):
```javascript
// Vanilla JS, ES6+, no frameworks
const init = () => {
  document.querySelector('.element').addEventListener('click', handler);
};
document.addEventListener('DOMContentLoaded', init);
```

## Component Structure

New components need:
1. HTML template: `_includes/components/name.html`
2. Styles: `_sass/components/_name.scss`
3. Import in: `_sass/components/_index.scss`
4. Documentation comment at top of file

## CSS Variables Available

Colors:
- `--color-primary`
- `--color-accent`
- `--color-surface`
- `--color-background`
- `--color-text-primary`
- `--color-text-secondary`

Spacing:
- `--spacing-xs` through `--spacing-xl`

Typography:
- `--font-size-sm` through `--font-size-2xl`

## Common Tasks

**Add experience**: Edit `_data/experience.yml`
**Add project**: Edit `_data/projects.yml`
**New component**: Create in `_includes/components/`
**Style changes**: Edit in `_sass/components/`
**New page**: Create in `pages/` with front matter

## Testing
Build: `bundle exec jekyll build`
Serve: `bundle exec jekyll serve --livereload`

## More Information
See COPILOT.md, AGENTS.md, and .ai/CONTEXT.md for detailed instructions.
