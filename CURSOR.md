# Cursor IDE Configuration

This file contains rules and context specific to **Cursor IDE**.

**Primary Reference**: See [AGENTS.md](AGENTS.md) for universal AI agent guidelines.

## Cursor-Specific Setup

### .cursorrules File

Cursor automatically reads `.cursorrules` in the project root. This file mirrors those rules for documentation.

### Project Context

Cursor should be aware of:
- **Tech Stack**: Jekyll static site generator
- **No Frameworks**: Vanilla HTML, CSS, JavaScript only
- **Data-Driven**: Content in YAML files (`_data/`)
- **Mobile-First**: Responsive design required
- **Dark Mode**: Support light and dark themes

## Cursor Capabilities

Cursor excels at:
- **Inline code completion** - Smart autocomplete in context
- **Multi-file editing** - Cmd+K across files
- **Chat interface** - Ask questions about codebase
- **Terminal integration** - Run commands from Cursor
- **Git integration** - Commit with AI-generated messages

## Key Shortcuts

- `Cmd/Ctrl + K` - AI edit mode
- `Cmd/Ctrl + L` - Open AI chat
- `Cmd/Ctrl + I` - Inline AI autocomplete
- `Cmd/Ctrl + Shift + P` - Command palette

## Recommended Cursor Usage

### Code Completion

Cursor will suggest completions based on:
- Existing code patterns
- YAML data structure
- Jekyll/Liquid syntax
- CSS variables in use

**Example:**
```scss
// Start typing:
.experience-card {
  padding: var(--
  // Cursor suggests: --spacing-md, --spacing-lg, etc.
}
```

### Chat Interface (Cmd+L)

Ask Cursor questions about the project:

```
Q: Where should I add a new work experience entry?
A: Add it to _data/experience.yml at the top of the list

Q: How do I create a new component?
A: 1. Create _includes/components/name.html
   2. Create _sass/components/_name.scss
   3. Import in _sass/components/_index.scss

Q: What CSS variables are available?
A: Check _sass/base/_variables.scss for full list
```

### AI Edit Mode (Cmd+K)

Select code and use Cmd+K to ask Cursor to:

```
- Make this responsive for mobile
- Add dark mode support
- Refactor using CSS Grid
- Add accessibility labels
- Improve performance
```

### Multi-File Edits

Cursor can edit multiple files at once:

```
Prompt: "Update the experience section to include company logos"

Cursor will:
1. Update _data/experience.yml to add logo field
2. Modify _includes/components/experience-card.html to display logos
3. Add styles in _sass/components/_experience-card.scss
4. Update documentation if needed
```

## Cursor Rules for This Project

### When Writing YAML

```yaml
# Cursor should maintain this format:
- company: "Company Name"
  title: "Job Title"
  start_date: "YYYY-MM"
  end_date: "YYYY-MM"
  description: |
    Multi-line description
```

### When Writing Components

```liquid
<!-- Cursor should use this pattern: -->

<!-- Component: Component Name
     Description: What it does
     Usage: {% include components/name.html data=data %} -->

<div class="component-name">
  <!-- content -->
</div>
```

### When Writing Styles

```scss
// Cursor should:
// 1. Use CSS variables
// 2. Include mobile breakpoints
// 3. Nest max 3 levels

.component {
  padding: var(--spacing-md);

  @media (max-width: 768px) {
    padding: var(--spacing-sm);
  }
}
```

## Cursor-Specific Workflows

### 1. Quick Fix with Cmd+K

1. Select problematic code
2. Press `Cmd+K`
3. Type: "Fix mobile overflow issue"
4. Review and accept changes

### 2. Generate Component

1. Create new file: `_includes/components/timeline.html`
2. Press `Cmd+K`
3. Type: "Create a vertical timeline component using experience data"
4. Review generated code
5. Create corresponding SCSS file

### 3. Refactor Across Files

1. Select code in layout file
2. Press `Cmd+K`
3. Type: "Extract this to a reusable component"
4. Cursor will create include file and update references

### 4. Documentation

1. Select function/component
2. Press `Cmd+K`
3. Type: "Add documentation comments"

## Git Integration

### AI Commit Messages

1. Stage changes in Cursor
2. Click commit button
3. Click "Generate" for AI commit message
4. Edit to add AI attribution:

```
feat: add experience timeline

- Created vertical timeline component
- Made it responsive
- Added dark mode support

AI-Assisted: Cursor IDE
```

## Cursor Settings for This Project

Add to Cursor workspace settings:

```json
{
  "cursor.aiInstructions": "Follow AGENTS.md guidelines. Keep code simple. Test mobile responsiveness. Use CSS variables.",
  "cursor.fileContext": [
    "AGENTS.md",
    ".ai/CONTEXT.md",
    "_config.yml"
  ]
}
```

## Common Cursor Commands

### In Chat (Cmd+L)

```
@file _config.yml what is the site title?
@folder _data what data files exist?
@code show me all experience components
@git what changed in the last commit?
```

### In Edit Mode (Cmd+K)

```
Make this mobile responsive
Add error handling
Improve accessibility
Use CSS Grid instead of Flexbox
Add dark mode styles
```

## Best Practices with Cursor

### DO

✓ Use `@file` to reference specific files
✓ Ask Cursor to explain before editing
✓ Review all AI suggestions before accepting
✓ Use Cmd+K for targeted edits
✓ Let Cursor generate commit messages (but add attribution)
✓ Ask Cursor questions about unfamiliar code

### DON'T

✗ Accept all suggestions without review
✗ Let Cursor add external dependencies
✗ Skip testing after Cursor edits
✗ Ignore Cursor's explanations
✗ Forget to add AI attribution

## Troubleshooting

### Cursor Suggests Wrong Pattern

```
Use Cmd+K and specify:
"Follow the pattern in _includes/components/experience-card.html"
```

### Cursor Adds Unwanted Dependencies

```
In chat: "Remove the dependency and use vanilla JavaScript instead"
```

### Build Fails After Cursor Edit

```bash
# Check what changed:
git diff

# Build with verbose output:
bundle exec jekyll build --verbose

# Ask Cursor:
Cmd+L: "The build failed with this error: [paste error]"
```

## Integration with Other Tools

Cursor works alongside:
- **Git**: Built-in version control
- **Terminal**: Integrated terminal for Jekyll commands
- **Browser**: Open in browser for live preview
- **DevTools**: Test responsive design

## File Watching

Cursor can watch for changes:

```bash
# In Cursor terminal:
bundle exec jekyll serve --livereload

# Edit files in Cursor, see changes in browser immediately
```

## Keyboard-Driven Workflow

1. `Cmd+P` - Quick file open
2. Edit file
3. `Cmd+K` - AI edit if needed
4. `Cmd+S` - Save (auto-reload in browser)
5. `Cmd+Shift+G` - Source control
6. Review changes
7. Commit with AI message
8. Add attribution

## Cursor Tips for Jekyll Projects

### Liquid Syntax Awareness

Cursor understands Liquid:
```liquid
{% for exp in site.data.experience %}
  <!-- Cursor will autocomplete exp. fields -->
  {{ exp.company }}
  {{ exp.title }}
{% endfor %}
```

### YAML Validation

Cursor will warn about YAML issues:
- Indentation errors
- Missing quotes
- Invalid syntax

### Jekyll Build Integration

Add task to run Jekyll:
```json
{
  "tasks": [
    {
      "label": "Jekyll Serve",
      "type": "shell",
      "command": "bundle exec jekyll serve --livereload"
    }
  ]
}
```

## Resources

- Cursor Docs: https://cursor.sh/docs
- Project Context: `.ai/CONTEXT.md`
- Universal Rules: `AGENTS.md`
- Keyboard Shortcuts: `Cmd+K Cmd+S` in Cursor

---

**Version**: 1.0
**Last Updated**: 2025-10-21
**Compatible with**: Cursor 0.x

**Note**: Always follow AGENTS.md first, then apply Cursor-specific features.
