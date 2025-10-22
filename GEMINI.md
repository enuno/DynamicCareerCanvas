# Google Gemini AI Configuration

This file contains rules and context specific to **Google Gemini** coding assistants.

**Primary Reference**: See [AGENTS.md](AGENTS.md) for universal AI agent guidelines.

## Gemini-Specific Capabilities

Gemini excels at:
- **Multi-modal understanding** - Can process images, code, and text together
- **Long context** - Handles large codebases well
- **Code explanation** - Great at explaining complex code
- **Pattern recognition** - Identifies code patterns and suggests improvements
- **Integration suggestions** - Good at API and service integration ideas

## Project Context for Gemini

**Project**: DynamicCareerCanvas
**Type**: Jekyll static portfolio site
**Stack**: Jekyll, YAML, SCSS, Vanilla JS
**Deployment**: GitHub Pages
**Owner**: Elvis Nuno

### Key Constraints
- No JavaScript frameworks (React, Vue, etc.)
- Content in YAML files, not hardcoded
- Mobile-first responsive design
- Support light and dark modes
- Maintain accessibility (WCAG AA)

## Using Gemini for This Project

### Code Review

Ask Gemini to review code for:
```
Review _includes/components/experience-card.html for:
- Accessibility issues
- Responsive design improvements
- Performance optimizations
- Code quality

Context: This is a Jekyll component that displays work experience
from YAML data. It should work on mobile and desktop, support
dark mode, and be accessible.
```

### Component Generation

```
Create a new Jekyll component for displaying project cards.

Requirements:
- Data from _data/projects.yml
- Responsive grid layout
- Featured projects highlighted
- Technology tags
- Links to project URLs
- Dark mode support

Follow patterns in _includes/components/experience-card.html
```

### Documentation

```
Generate comprehensive documentation for the component system.

Include:
- How components are structured
- How to create new components
- How to use data from YAML files
- Examples of common patterns
- Troubleshooting tips
```

### Refactoring

```
Refactor _sass/components/_experience-card.scss to use CSS Grid
instead of Flexbox for better layout control.

Keep:
- Existing responsive breakpoints
- CSS variable usage
- Dark mode support
- Animation timing

Improve:
- Layout flexibility
- Code organization
- Performance
```

## Gemini Workflows

### 1. Understanding Existing Code

```
Explain how the Jekyll build process works in this project.
What happens from YAML data to rendered HTML?
```

Gemini will:
- Analyze _config.yml
- Trace data flow from YAML to templates
- Explain Liquid template processing
- Show the build pipeline

### 2. Suggesting Improvements

```
Analyze _sass/ directory and suggest organizational improvements.
```

Gemini will:
- Review current structure
- Identify inconsistencies
- Suggest better organization
- Provide migration plan

### 3. Accessibility Audit

```
Audit the site for accessibility issues.

Check:
- Semantic HTML
- ARIA labels
- Keyboard navigation
- Color contrast
- Screen reader compatibility

Provide specific fixes for any issues found.
```

### 4. Performance Analysis

```
Analyze the site's performance and suggest optimizations.

Focus on:
- Page load time
- Render-blocking resources
- Image optimization
- CSS/JS bundle size
```

## Integration with Development Workflow

### Before Starting

Provide Gemini with context:
```
I'm working on DynamicCareerCanvas, a Jekyll portfolio site.
Please read AGENTS.md and .ai/CONTEXT.md for project details.

Current task: [describe what you want to do]
```

### During Development

Ask for help:
```
I'm stuck on [problem]. Here's what I've tried: [attempts]

The error is: [error message]

How should I fix this?
```

### After Changes

Request review:
```
I've made these changes: [description]

Please review for:
- Code quality
- Potential issues
- Improvements
- Testing recommendations
```

## Gemini-Specific Instructions

### When Editing YAML

Gemini should:
- Maintain exact indentation (2 spaces)
- Use double quotes for strings
- Keep dates in YYYY-MM format
- Preserve chronological order
- Validate syntax before suggesting changes

### When Writing Templates

Gemini should:
- Use semantic HTML5 elements
- Add descriptive comments
- Include ARIA labels where needed
- Make responsive by default
- Support dark mode
- Follow BEM naming for classes

### When Writing Styles

Gemini should:
- Use existing CSS variables
- Write mobile-first media queries
- Keep nesting under 3 levels
- Group related properties
- Add comments for complex selectors
- Support both light and dark themes

### When Writing JavaScript

Gemini should:
- Use modern ES6+ syntax
- Avoid external dependencies
- Progressive enhancement approach
- Document with JSDoc
- Handle edge cases
- Include error handling

## Common Gemini Tasks

### Adding Features

```
Add a "View Resume" button to the homepage that:
- Links to /resume
- Has hover animation
- Works on mobile
- Matches existing design

Use the button pattern from _includes/components/button.html
if it exists, or create a new one following project conventions.
```

### Fixing Bugs

```
The mobile navigation menu isn't closing when a link is clicked.

File: _includes/nav.html
Related JS: assets/js/nav.js

Please identify the issue and provide a fix.
```

### Optimizing Code

```
The experience section loads slowly with many entries.

Optimize:
- _data/experience.yml processing
- _includes/components/experience-card.html rendering
- _sass/components/_experience-card.scss

Without changing functionality or appearance.
```

## Gemini Attribution

Include in commits:

```
AI-Assisted: Google Gemini
Tool: [Gemini API / Google AI Studio / IDE Extension]
Co-Authored-By: Gemini <noreply@google.com>
```

## Tips for Better Results

1. **Provide Full Context**: Share relevant files and background
2. **Be Specific**: Detailed requirements get better results
3. **Show Examples**: Reference existing patterns to follow
4. **Ask for Explanations**: Request reasoning behind suggestions
5. **Iterate**: Refine through follow-up questions
6. **Test Suggestions**: Always validate Gemini's code locally

## Handling Errors

If Gemini's suggestion doesn't work:

```
The code you suggested produces this error:
[paste error]

The issue seems to be: [your analysis]

Please provide a corrected version and explain what was wrong.
```

## Advanced Gemini Features

### Multi-File Analysis

```
Analyze the relationship between:
- _data/experience.yml
- _includes/components/experience-card.html
- _layouts/default.html
- _sass/components/_experience-card.scss

Show how data flows through these files.
```

### Pattern Extraction

```
Review all component files and extract common patterns.
Create a component template that follows these patterns.
```

### Migration Planning

```
I want to migrate from the current theme to a custom design.

Analyze:
- Current dependencies
- Files that need changes
- Potential issues
- Step-by-step migration plan
```

## Testing with Gemini

```
Generate a test plan for the timeline component including:
- Functional tests
- Responsive tests
- Accessibility tests
- Browser compatibility tests
- Edge cases to check
```

## Documentation with Gemini

```
Generate documentation for _data/experience.yml:
- Field definitions
- Required vs optional fields
- Format specifications
- Examples
- Common mistakes to avoid
```

## Resources

- Gemini Docs: https://ai.google.dev/docs
- Project Context: `.ai/CONTEXT.md`
- Universal Rules: `AGENTS.md`
- Coding Standards: `.ai/CONVENTIONS.md`

---

**Version**: 1.0
**Last Updated**: 2025-10-21
**Compatible with**: Gemini Pro, Gemini Ultra

**Note**: Always reference AGENTS.md first for universal guidelines.
