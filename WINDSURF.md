# Windsurf AI Configuration

This file contains rules and context specific to **Windsurf** IDE with AI assistance.

**Primary Reference**: See [AGENTS.md](AGENTS.md) for universal AI agent guidelines.

## Windsurf Overview

Windsurf is an AI-powered IDE with:
- Integrated AI code assistant
- Context-aware suggestions
- Multi-file editing
- Terminal integration
- Git integration

## Project Setup for Windsurf

**Project**: DynamicCareerCanvas
**Type**: Jekyll static site
**Language**: HTML, SCSS, JavaScript, YAML, Liquid
**Framework**: None (vanilla)
**Build**: Jekyll + GitHub Pages

## Windsurf-Specific Features

### AI Flow Mode

Windsurf's Flow mode for coding:

```
Prompt: Create experience timeline component

Windsurf Flow will:
1. Analyze project structure
2. Review existing components
3. Generate component files
4. Apply consistent styling
5. Test in context
```

### Context Awareness

Windsurf understands:
- Project file structure
- Code relationships
- YAML data schemas
- Jekyll/Liquid syntax
- SCSS patterns

### Quick Actions

- **Cmd+K**: AI edit selection
- **Cmd+L**: AI chat
- **Flow Mode**: Autonomous coding
- **Cascade**: Multi-file changes

## Windsurf Instructions

### When Editing Code

Windsurf should:
- Follow existing patterns in the project
- Use CSS variables from `_sass/base/_variables.scss`
- Maintain responsive design
- Support both light and dark themes
- Keep accessibility features
- Use vanilla JavaScript only (no frameworks)

### When Creating Components

```
Required files:
1. _includes/components/component-name.html
2. _sass/components/_component-name.scss
3. Import in _sass/components/_index.scss

Include:
- Documentation header
- Responsive styles
- Dark mode support
- Accessibility features
```

### When Writing YAML

```yaml
# Windsurf should maintain structure:
- field: "Value"
  date: "YYYY-MM"
  description: |
    Multi-line content
  list:
    - "Item one"
```

## Windsurf Workflows

### 1. Feature Development (Flow Mode)

```
Task: Add project filtering by technology

Windsurf Flow:
1. Review _data/projects.yml structure
2. Create filter UI component
3. Add filtering JavaScript
4. Style filter controls
5. Update projects page
6. Test functionality
```

### 2. Refactoring with Cascade

```
Task: Refactor all components to use CSS Grid

Windsurf Cascade:
1. Identify affected components
2. Update each SCSS file
3. Maintain responsive behavior
4. Test visual consistency
5. Update documentation
```

### 3. Multi-File Editing

```
Task: Add dark mode toggle

Windsurf will edit:
- _includes/header.html (add toggle)
- assets/js/theme.js (toggle logic)
- _sass/components/_theme-toggle.scss (styles)
- _config.yml (if needed)
```

## Best Practices with Windsurf

### DO

✓ Use Flow mode for complex features
✓ Let Windsurf suggest patterns
✓ Review AI changes before accepting
✓ Use Cascade for coordinated changes
✓ Ask Windsurf to explain decisions
✓ Leverage context awareness

### DON'T

✗ Accept all suggestions blindly
✗ Skip testing after AI edits
✗ Let Windsurf add frameworks
✗ Ignore build errors
✗ Forget to attribute AI work

## Windsurf-Specific Commands

### In Chat

```
@workspace: Query entire project
@file: Reference specific file
@code: Find code snippets
@git: Git-related questions

Example:
@workspace How is the experience data structured?
@file _config.yml What's the site title?
```

### In Editor

```
Cmd+K + prompt:
- "Make this responsive"
- "Add dark mode support"
- "Improve accessibility"
- "Optimize performance"
```

## Project-Specific Guidance

### YAML Data Files

When editing `_data/*.yml`:
- Preserve exact formatting
- Use double quotes
- Maintain chronological order (recent first)
- Validate syntax

### Liquid Templates

When editing `.html` files in `_includes/` or `_layouts/`:
- Use semantic HTML
- Add ARIA labels where needed
- Include descriptive comments
- Follow BEM naming for classes

### SCSS Styles

When editing `.scss` files:
- Use existing CSS variables
- Write mobile-first media queries
- Keep nesting under 3 levels
- Support dark mode

### JavaScript

When editing `.js` files:
- ES6+ syntax only
- No external libraries/frameworks
- Progressive enhancement
- Document with JSDoc

## Testing with Windsurf

Windsurf can run tests:

```bash
# Build Jekyll site
bundle exec jekyll build

# Serve with live reload
bundle exec jekyll serve --livereload

# Windsurf can execute these and show results
```

Before committing Windsurf's changes:
- Build succeeds
- Visual check in browser
- Mobile responsive
- No console errors

## Windsurf Attribution

Include in commits:

```
AI-Assisted: Windsurf IDE
Flow Mode: [Yes/No]
Co-Authored-By: Windsurf AI <noreply@windsurf.ai>
```

## Common Windsurf Tasks

### Adding Content

```
Prompt: Add new project to portfolio

Windsurf:
1. Opens _data/projects.yml
2. Suggests entry structure
3. Validates YAML
4. Shows preview
```

### Creating Pages

```
Prompt: Create contact page with form

Windsurf Flow:
1. Creates pages/contact.md
2. Adds front matter
3. Creates form HTML
4. Styles form
5. Adds to navigation
```

### Styling Updates

```
Prompt: Update button styles across the site

Windsurf Cascade:
1. Finds all button styles
2. Updates consistently
3. Maintains responsive behavior
4. Tests visual changes
```

## Windsurf Integration

### Git Workflow

Windsurf integrates with Git:
- Stage changes visually
- Generate commit messages
- Review diffs inline
- Push to remote

Always add AI attribution to commits.

### Terminal Integration

Run commands in Windsurf terminal:
```bash
bundle exec jekyll serve
git status
git diff
```

Windsurf can suggest and execute commands.

## Advanced Windsurf Features

### Smart Autocomplete

Windsurf suggests based on:
- Current file context
- Project patterns
- YAML schemas
- Variable names

### Code Navigation

- Jump to definition
- Find references
- File search
- Symbol search

### Refactoring Tools

- Rename symbol
- Extract component
- Inline variable
- Move file

## Troubleshooting

### Windsurf Slow

- Large files: Split into smaller components
- Clear cache: Restart Windsurf
- Check system resources

### Wrong Suggestions

- Provide more context in prompt
- Reference specific files
- Show examples to follow

### Build Errors

- Check Windsurf terminal output
- Ask Windsurf to explain error
- Review recent changes

## Resources

- Windsurf Docs: https://windsurf.ai/docs
- Project Context: `.ai/CONTEXT.md`
- Universal Rules: `AGENTS.md`
- Quick Reference: `.windsurfrules`

---

**Version**: 1.0
**Last Updated**: 2025-10-21
**Compatible with**: Windsurf IDE

**Note**: See `.windsurfrules` for quick reference. Always follow AGENTS.md for universal guidelines.
