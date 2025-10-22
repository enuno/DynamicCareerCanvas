# Cline AI Assistant Configuration

This file contains rules and context specific to **Cline** (formerly Claude Dev).

**Primary Reference**: See [AGENTS.md](AGENTS.md) for universal AI agent guidelines.

## Cline Overview

Cline is an autonomous AI coding assistant that can:
- Edit multiple files
- Run terminal commands
- Browse the web for information
- Create entire features autonomously
- Execute complex multi-step tasks

## Project Context for Cline

**Project**: DynamicCareerCanvas
**Type**: Jekyll static portfolio website
**Stack**: Jekyll, YAML, SCSS, Vanilla JS
**Deployment**: GitHub Pages (automated via GitHub Actions)
**Repository**: enuno/DynamicCareerCanvas

## Cline Capabilities for This Project

### Autonomous Development

Cline can complete full features:

```
Task: Add a filterable project gallery

Cline will:
1. Review _data/projects.yml structure
2. Create gallery component
3. Add filtering JavaScript
4. Style with SCSS
5. Update relevant pages
6. Test the build
7. Commit changes
```

### Multi-File Editing

Cline excels at coordinated changes:

```
Task: Migrate experience data to include company logos

Cline will:
1. Update _data/experience.yml schema
2. Modify experience-card.html component
3. Update SCSS for logo display
4. Document the changes
5. Test the rendering
```

### Terminal Integration

Cline can run commands:

```bash
# Cline can execute:
bundle exec jekyll build
bundle exec jekyll serve
git status
git diff
```

## Cline-Specific Instructions

### When Creating Features

Cline should:
1. **Plan first** - Outline approach before coding
2. **Read context** - Check `.ai/CONTEXT.md` and `AGENTS.md`
3. **Follow patterns** - Match existing code style
4. **Test thoroughly** - Build and preview locally
5. **Document changes** - Update relevant docs
6. **Clean commits** - Clear, atomic commits with attribution

### When Editing Files

Cline should:
- Preserve existing formatting
- Use CSS variables consistently
- Maintain responsive design
- Keep accessibility features
- Test after each change
- Never break the build

### When Running Commands

Cline should:
- Always check command output
- Handle errors gracefully
- Verify success before proceeding
- Use appropriate flags
- Clean up after tasks

## Cline Workflows

### 1. Feature Development

```
Prompt: Implement a dark/light mode toggle

Cline autonomous workflow:
1. Review current theme implementation
2. Create toggle component HTML
3. Add toggle JavaScript
4. Style toggle button
5. Update theme switching logic
6. Test in both modes
7. Document usage
8. Commit with clear message
```

### 2. Bug Fixing

```
Prompt: Fix mobile navigation overflow issue

Cline workflow:
1. Reproduce issue locally
2. Identify root cause in CSS
3. Fix the styles
4. Test on multiple screen sizes
5. Ensure no regression
6. Commit fix
```

### 3. Refactoring

```
Prompt: Refactor SCSS to use CSS Grid

Cline workflow:
1. Analyze current layout system
2. Plan migration approach
3. Update component styles
4. Test responsive behavior
5. Verify visual consistency
6. Update documentation
7. Commit changes
```

### 4. Content Updates

```
Prompt: Add new work experience and project

Cline workflow:
1. Edit _data/experience.yml
2. Edit _data/projects.yml
3. Validate YAML syntax
4. Build and preview
5. Verify rendering
6. Commit updates
```

## Working with Cline

### Effective Task Description

**Good:**
```
Create a timeline component that displays work experience chronologically.
Use data from _data/experience.yml.
Requirements:
- Vertical timeline on desktop
- List view on mobile
- Company logos (if available)
- Smooth scroll animations
- Dark mode support
Follow the pattern from experience-card component.
```

**Better:**
```
Implement experience timeline feature.

Context: Users want a visual timeline of my career.

Requirements:
1. Visual vertical timeline (desktop)
2. Simple list (mobile < 768px)
3. Use _data/experience.yml for data
4. Company logos optional
5. Fade-in on scroll
6. Support dark mode

Design:
- Follow existing component patterns
- Use CSS variables
- BEM naming
- Accessible

Testing:
- Build successfully
- Mobile responsive
- Dark mode works
- No console errors

Files likely affected:
- _includes/components/timeline.html (new)
- _sass/components/_timeline.scss (new)
- assets/js/timeline.js (new)
- Possibly pages/about.md or index.md
```

### Monitoring Cline's Progress

Cline provides updates:
- Planning phase
- File changes
- Commands executed
- Test results
- Completion summary

Review each step and guide if needed.

### Iterating with Cline

```
Prompt: The timeline looks good, but make these adjustments:
- Increase spacing between entries
- Make logos circular instead of square
- Add subtle animation to the connecting line

Cline will apply refinements.
```

## Cline Best Practices

### DO

✓ Give clear, specific tasks
✓ Provide full context upfront
✓ Review Cline's plan before execution
✓ Test after Cline completes tasks
✓ Ask Cline to explain decisions
✓ Use Cline for repetitive tasks
✓ Let Cline handle multi-file changes

### DON'T

✗ Give vague instructions
✗ Skip reviewing Cline's code
✗ Let Cline commit without attribution
✗ Ignore build errors
✗ Rush through Cline's work
✗ Use Cline without understanding output

## Cline Commands

### Common Tasks

```
# Build the site
bundle exec jekyll build

# Serve locally
bundle exec jekyll serve --livereload

# Check git status
git status

# Show changes
git diff

# Validate YAML (if script exists)
./scripts/validate-yaml.sh
```

### Cline Should Run These

Before committing:
1. `bundle exec jekyll build` - Verify build works
2. Visual inspection in browser
3. `git status` - Check what changed
4. `git diff` - Review changes

## Cline Attribution

Cline should include in commits:

```
feat: add experience timeline component

Implemented interactive timeline showing career progression:
- Vertical timeline layout for desktop
- List view for mobile
- Company logo integration
- Scroll animations
- Dark mode support

Files created:
- _includes/components/timeline.html
- _sass/components/_timeline.scss
- assets/js/timeline.js

AI-Assisted: Cline
Autonomous execution with human review
Co-Authored-By: Cline <noreply@anthropic.com>
```

## Handling Errors with Cline

If Cline encounters errors:

```
Error: Build failed with YAML syntax error

Cline should:
1. Read the error message
2. Identify the problematic file
3. Fix the syntax error
4. Re-run build
5. Verify success
6. Continue task
```

If stuck, Cline should:
- Report the blocker
- Suggest alternatives
- Ask for guidance

## Advanced Cline Usage

### Multi-Step Features

```
Prompt: Implement complete blog functionality

Cline workflow:
1. Create _posts/ directory
2. Set up blog collection in _config.yml
3. Create blog post layout
4. Create blog index page
5. Add blog post component
6. Style blog elements
7. Add navigation link
8. Test with sample posts
9. Document blog usage
10. Commit complete feature
```

### Coordinated Updates

```
Prompt: Update color scheme to use new brand colors

Cline will:
1. Update CSS variables in _sass/base/_variables.scss
2. Update light theme values
3. Update dark theme values
4. Check all components visually
5. Adjust any specific overrides
6. Test in both modes
7. Document color changes
```

## Cline Limitations

- **Can't preview visually** - Relies on code analysis
- **Can't test interactions** - Limited to code review
- **May need guidance** - On design decisions
- **Autonomous but supervised** - Always review output

## Resources

- Cline Docs: https://github.com/cline/cline
- Project Context: `.ai/CONTEXT.md`
- Universal Rules: `AGENTS.md`
- Coding Standards: `.ai/CONVENTIONS.md`

## Also See

- `.clinerules` - Quick reference for Cline
- `CLAUDE.md` - Claude-specific (Cline uses Claude)

---

**Version**: 1.0
**Last Updated**: 2025-10-21
**Compatible with**: Cline VS Code Extension

**Note**: Cline is autonomous but requires supervision. Always review its work before accepting.
