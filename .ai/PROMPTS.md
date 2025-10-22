# Reusable AI Prompts for DynamicCareerCanvas

This document contains pre-written prompts for common tasks to ensure consistency and efficiency when working with AI coding assistants.

## Content Management Prompts

### Adding Work Experience

```
Add a new work experience entry to _data/experience.yml with the following information:

Company: [Company Name]
Title: [Job Title]
Location: [City, State/Country]
Start Date: [YYYY-MM]
End Date: [YYYY-MM or "Present"]
Description: [Brief description of role]
Highlights:
- [Key achievement 1]
- [Key achievement 2]
- [Key achievement 3]
Technologies: [List of technologies used]

Follow the existing YAML structure and validate the file after adding.
```

### Adding New Project

```
Add a new project to _data/projects.yml:

Name: [Project Name]
Description: [Project description]
URL: [Project URL or repository]
Status: [active/completed/published]
Year: [YYYY]
Technologies: [List of technologies]
Featured: [true/false - should it appear on homepage?]

Also add a project image to assets/images/projects/ if available.
Validate YAML after completion.
```

### Updating Skills

```
Update the skills section in _data/skills.yml:

Category: [Networking/Systems Engineering/DevOps/Blockchain/Leadership]
Action: [add/remove/update]
Skills: [List of skills to add/remove/update]

Maintain alphabetical order within categories and follow existing formatting.
```

### Adding Publication or Presentation

```
Add a new publication/presentation to _data/publications.yml:

Title: [Publication/Presentation Title]
Type: [publication/presentation/media/project]
Description: [Brief description or quote]
URL: [Link to publication/video/project]
Date: [YYYY-MM]
Featured: [true/false]

Validate YAML structure after adding.
```

## Design & Development Prompts

### Creating New Component

```
Create a new component for [component purpose]:

Name: [component-name]
Location: _includes/components/[component-name].html
Styling: _sass/components/_[component-name].scss

Requirements:
- Use BEM naming convention
- Include component documentation header
- Make it responsive (mobile-first)
- Use CSS variables for theming
- Support dark mode
- Include accessibility features (ARIA labels, semantic HTML)
- Follow the pattern from existing components

Parameters the component should accept:
- [param1]: [description]
- [param2]: [description]

Please create both the HTML template and SCSS file.
```

### Implementing New Page

```
Create a new page for [page purpose]:

Filename: pages/[page-name].md
Layout: [default/page/custom]
Navigation: [Yes/No - add to main navigation?]

Content sections:
1. [Section 1]
2. [Section 2]
3. [Section 3]

Requirements:
- Responsive design
- Accessible
- SEO-optimized front matter
- Use existing components where possible
```

### Styling Modifications

```
Update the styling for [component/section]:

Target: [specific component or section]
Changes needed:
- [Change 1]
- [Change 2]
- [Change 3]

Requirements:
- Maintain existing CSS variable usage
- Ensure dark mode compatibility
- Test on mobile and desktop
- Follow BEM naming convention
- Use CSS Grid/Flexbox for layout
```

## Code Quality Prompts

### Code Review

```
Please review the following code/changes and check for:

1. Adherence to project conventions (.ai/CONVENTIONS.md)
2. Accessibility issues (WCAG 2.1 AA compliance)
3. Responsive design considerations
4. Performance implications
5. Security concerns
6. Code documentation quality
7. Consistency with existing codebase

Files to review:
- [file1]
- [file2]

Provide specific suggestions for improvements.
```

### Refactoring

```
Refactor [file/component] to improve:
- Code readability
- Performance
- Maintainability
- Accessibility

Current file: [path/to/file]

Requirements:
- Maintain existing functionality
- Follow project conventions
- Add comments for complex logic
- Update documentation if needed
- Ensure backward compatibility
```

### Optimization

```
Optimize [component/page] for:
- Page load speed
- Mobile performance
- Accessibility score
- SEO ranking

Current implementation: [description]

Analyze and suggest:
1. Image optimization opportunities
2. CSS/JS minification
3. Render-blocking resource handling
4. Lazy loading implementation
5. Caching strategies
```

## Documentation Prompts

### Updating Documentation

```
Update [documentation file] to reflect recent changes:

File: [path/to/doc]
Changes made:
- [Change 1]
- [Change 2]
- [Change 3]

Please:
1. Update relevant sections
2. Add new information where needed
3. Maintain existing formatting style
4. Update "Last Updated" date
5. Ensure accuracy and clarity
```

### Creating Architecture Decision Record

```
Create an Architecture Decision Record (ADR) for:

Decision: [What was decided]
Date: [YYYY-MM-DD]
Status: [Proposed/Accepted/Deprecated/Superseded]

Context: [Why was this decision needed?]
Decision: [What is the change?]
Consequences: [What becomes easier/harder?]
Alternatives: [What else was considered?]

Save to: docs/architecture/DECISIONS.md
```

### Generating Changelog Entry

```
Generate a changelog entry for version [version number]:

Changes:
- [Change 1]
- [Change 2]
- [Change 3]

Categories:
- Added: [new features]
- Changed: [changes to existing]
- Deprecated: [soon-to-be removed]
- Removed: [removed features]
- Fixed: [bug fixes]
- Security: [security fixes]

Follow Keep a Changelog format.
```

## Testing & Validation Prompts

### Comprehensive Testing

```
Perform comprehensive testing on [feature/page/component]:

Test areas:
1. Functionality - Does it work as expected?
2. Responsiveness - Test on mobile (320px), tablet (768px), desktop (1200px+)
3. Accessibility - Check with screen reader, keyboard navigation, color contrast
4. Performance - Page load time, Lighthouse score
5. Cross-browser - Chrome, Firefox, Safari, Edge
6. Data validation - YAML structure, required fields

Provide test results and any issues found.
```

### Accessibility Audit

```
Perform an accessibility audit on [page/component]:

Check:
- [ ] Semantic HTML usage
- [ ] ARIA labels where needed
- [ ] Keyboard navigation
- [ ] Focus indicators
- [ ] Color contrast (WCAG AA: 4.5:1 for text, 3:1 for large text)
- [ ] Alt text for images
- [ ] Form labels
- [ ] Heading hierarchy
- [ ] Screen reader compatibility

Provide WCAG 2.1 compliance report and remediation steps.
```

### Performance Audit

```
Conduct a performance audit:

Target: [URL or component]

Analyze:
- Page load time
- Time to Interactive (TTI)
- First Contentful Paint (FCP)
- Largest Contentful Paint (LCP)
- Cumulative Layout Shift (CLS)
- Total page weight
- Number of requests
- Render-blocking resources

Provide Lighthouse report summary and optimization recommendations.
```

## Troubleshooting Prompts

### Debug Build Issues

```
Debug the following Jekyll build error:

Error message:
[paste error message]

Context:
- Recent changes: [describe what was changed]
- Files modified: [list files]
- Branch: [branch name]

Please:
1. Identify the root cause
2. Explain why it's happening
3. Provide fix with explanation
4. Suggest prevention strategies
```

### Fix Responsive Design Issues

```
Fix responsive design issues on [component/page]:

Issue: [description of problem]
Affected breakpoints: [mobile/tablet/desktop]
Current behavior: [what's happening]
Expected behavior: [what should happen]

Please:
1. Identify CSS causing the issue
2. Provide corrected styles
3. Test on multiple screen sizes
4. Ensure no regression on other breakpoints
```

### Resolve Merge Conflicts

```
Help resolve merge conflicts in:

Files with conflicts:
- [file1]
- [file2]

Branches being merged:
- Source: [branch name]
- Target: [branch name]

Context of changes:
- [describe what each branch was doing]

Please:
1. Analyze the conflicts
2. Suggest resolution strategy
3. Explain trade-offs if any
4. Provide final merged version
```

## Git & Version Control Prompts

### Create Meaningful Commit Message

```
Create a commit message for the following changes:

Files changed:
- [file1]: [what changed]
- [file2]: [what changed]

Purpose of changes: [why these changes were made]

Follow conventional commits format:
<type>(<scope>): <subject>

<body>

<footer>

Include AI attribution if applicable.
```

### Create Pull Request Description

```
Create a pull request description for:

Branch: [feature/fix/docs branch name]
Target: develop

Changes made:
- [change 1]
- [change 2]
- [change 3]

Purpose: [why these changes]

Template should include:
## Summary
## Changes Made
## Testing Done
## Screenshots (if UI changes)
## Checklist
## Related Issues

AI attribution where applicable.
```

### Generate Release Notes

```
Generate release notes for version [version number]:

Commits since last release:
[list commits or provide git log]

Format:
# Release v[version]

## What's New
## Improvements
## Bug Fixes
## Documentation
## Dependencies
## Breaking Changes (if any)

Thank contributors and include deployment notes.
```

## Analytics & Reporting Prompts

### Generate Progress Report

```
Generate a project progress report:

Period: [date range]
Focus areas:
- Features completed
- Bugs fixed
- Performance improvements
- Documentation updates

Include:
- Summary of achievements
- Metrics (if available)
- Challenges faced
- Next steps
- Resource needs
```

### Analyze Content Updates Needed

```
Analyze the portfolio content and suggest updates:

Review:
- _data/experience.yml - Are all positions current?
- _data/projects.yml - Are there completed projects to add?
- _data/skills.yml - Any new skills to include?
- _data/publications.yml - Recent publications or presentations?

Provide recommendations for keeping the portfolio current and impactful.
```

## Miscellaneous Prompts

### SEO Optimization

```
Optimize SEO for [page]:

Current page: [URL or page name]

Analyze and improve:
- Title tag (50-60 characters)
- Meta description (150-160 characters)
- Heading structure (H1, H2, H3 hierarchy)
- Image alt text
- Internal linking
- Schema markup opportunities
- Open Graph tags
- Twitter Card tags

Provide optimized front matter and content recommendations.
```

### Improve Loading Performance

```
Improve loading performance for:

Target: [page/component]
Current metrics: [if known]

Optimize:
- Critical rendering path
- Image loading (lazy loading, WebP)
- CSS delivery (inline critical CSS)
- JavaScript execution (defer, async)
- Font loading (font-display: swap)
- Third-party scripts
- Browser caching

Provide implementation steps and expected improvements.
```

---

## How to Use These Prompts

1. **Copy the relevant prompt** from this document
2. **Fill in the bracketed placeholders** with specific information
3. **Paste into your AI assistant** (Claude Code, Cursor, etc.)
4. **Review and refine** the AI's response
5. **Test the implementation** before committing

## Adding New Prompts

When you create a useful prompt, add it to this document:

1. Choose the appropriate category (or create new one)
2. Give it a clear, descriptive title
3. Include the full prompt text with placeholders
4. Add usage notes if needed
5. Document any prerequisites or follow-up actions

## Prompt Best Practices

- **Be Specific**: Include file paths, exact requirements, constraints
- **Provide Context**: Reference existing patterns, related files
- **Set Expectations**: Specify output format, quality standards
- **Include Validation**: Ask AI to validate/test its output
- **Request Attribution**: Remind to include AI attribution

---

**Last Updated**: 2025-10-21
**Version**: 1.0
**Contributions**: Feel free to add prompts that work well for you
