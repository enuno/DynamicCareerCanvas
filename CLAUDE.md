# Claude AI Agent Configuration

This file contains rules and context specific to **Claude** (including Claude Code CLI and Claude.ai chat interface).

**Primary Reference**: See [AGENTS.md](AGENTS.md) for universal AI agent guidelines. This file only adds Claude-specific details.

## Claude-Specific Capabilities

Claude excels at:
- **Long-form content editing** - Great for updating YAML data files
- **Documentation writing** - Excellent for markdown files
- **Code refactoring** - Strong at improving existing code
- **Accessibility review** - Good at checking WCAG compliance
- **Complex reasoning** - Helpful for architectural decisions

## Claude Code CLI

### Initialization

When starting a Claude Code session:

```bash
# Claude automatically reads these files:
# - .claude/settings.local.json (if exists)
# - README.md
# - CLAUDE.md (this file)
```

### Recommended Workflow

1. **Start session** - Claude reads project context
2. **Read context** - "Read .ai/CONTEXT.md to understand the project"
3. **Specific task** - Give Claude a clear, specific task
4. **Review changes** - Always review Claude's changes before committing
5. **Test** - Build locally and verify in browser

### Effective Prompts for Claude

**For Content Updates:**
```
Add this work experience to _data/experience.yml:
Company: XYZ Corp
Title: Senior Engineer
Location: Seattle, WA
Dates: 2024-01 to Present
[details...]

Follow the existing YAML structure.
```

**For Component Creation:**
```
Create a new timeline component in _includes/components/timeline.html
that displays work experience in chronological order.
Use the experience data from _data/experience.yml.
Make it responsive and support dark mode.
```

**For Documentation:**
```
Update the README.md to reflect the new directory structure
and add a quick start guide for local development.
```

**For Refactoring:**
```
Refactor _sass/components/_experience-card.scss to:
- Use CSS Grid instead of Flexbox
- Improve mobile responsiveness
- Use existing CSS variables
Follow the conventions in .ai/CONVENTIONS.md
```

### Claude's Strengths in This Project

**YAML Editing**: Claude is excellent at maintaining YAML structure
```
# Claude will properly format and validate:
- experience.yml
- projects.yml
- skills.yml
- publications.yml
```

**Documentation**: Claude writes clear, comprehensive docs
```
# Ask Claude to create/update:
- README sections
- API documentation
- Architecture decision records
- Inline code comments
```

**Liquid Templates**: Claude understands Jekyll/Liquid syntax well
```
# Claude can help with:
- Creating new layouts
- Writing component includes
- Adding conditional logic
- Using filters and tags
```

## Claude.ai Chat Interface

### Best Practices

**Provide Context:**
```
I'm working on a Jekyll portfolio site (DynamicCareerCanvas).
Tech stack: Jekyll, YAML, SCSS, vanilla JS.
Read AGENTS.md and .ai/CONTEXT.md for project details.

Task: [your specific request]
```

**Ask for Explanations:**
```
Explain why you chose this approach and what alternatives exist.
```

**Request Tests:**
```
After making changes, provide instructions for testing this locally.
```

### Multi-Turn Conversations

Claude maintains context across conversation:

1. **Session 1**: "Review my _config.yml and suggest improvements"
2. **Session 2**: "Implement the suggestions you made earlier"
3. **Session 3**: "Now update the documentation to reflect these changes"

### Code Review with Claude

```
Review this component for:
- Accessibility issues
- Responsive design problems
- Performance concerns
- Code quality improvements

[paste code]
```

## Project-Specific Claude Instructions

### Content Management

**When editing YAML files:**
- Preserve existing structure exactly
- Use double quotes for strings
- Maintain chronological order (recent first)
- Validate before committing

**When creating components:**
- Add documentation header
- Use descriptive class names
- Include responsive styles
- Support dark mode
- Test on mobile

### Documentation

**When writing docs:**
- Use clear, concise language
- Include code examples
- Add tables for structured data
- Link to related documentation
- Keep under 100 char line length (markdown)

### Code Generation

**When writing HTML/Liquid:**
- Semantic HTML5 elements
- BEM-style class naming
- Include ARIA labels where needed
- Comment complex logic

**When writing SCSS:**
- Use CSS variables
- Mobile-first media queries
- Nest max 3 levels
- Group related properties

**When writing JavaScript:**
- Modern ES6+ syntax
- No frameworks/libraries
- Progressive enhancement
- Document with JSDoc comments

## Claude Attribution

Include in all commits with Claude assistance:

```
AI-Assisted: Claude Code (Sonnet 4.5)
Tool: Claude Code CLI
Co-Authored-By: Claude <noreply@anthropic.com>
```

or for chat interface:

```
AI-Assisted: Claude.ai (Sonnet 4.5)
Tool: Claude Web Interface
Co-Authored-By: Claude <noreply@anthropic.com>
```

## Common Claude Workflows

### 1. Adding Experience Entry

```
Prompt: Add this work experience to _data/experience.yml:
[provide details]

Claude will:
1. Read existing structure
2. Format new entry
3. Insert at correct position
4. Validate YAML
5. Show you the changes
```

### 2. Creating New Page

```
Prompt: Create a new "Contact" page at pages/contact.md
with a contact form using Formspree.

Claude will:
1. Create page with front matter
2. Add semantic HTML form
3. Style with existing patterns
4. Make it responsive
5. Provide testing instructions
```

### 3. Refactoring Styles

```
Prompt: Refactor the navigation styles in _sass/layout/_nav.scss
to improve mobile experience.

Claude will:
1. Analyze current styles
2. Suggest improvements
3. Implement changes
4. Explain the reasoning
5. Note what to test
```

### 4. Documentation Updates

```
Prompt: Update README.md with:
- New directory structure
- Updated setup instructions
- Badge for GitHub Actions status

Claude will:
1. Preserve existing content
2. Add new sections
3. Format consistently
4. Update table of contents if present
```

## Claude Limitations to Be Aware Of

**Image Processing**: Claude can see images but can't create/edit them
**File Size**: Large files may need to be processed in chunks
**Real-Time Data**: Claude's knowledge cutoff is January 2025
**External APIs**: Claude can't directly test API integrations

## Tips for Better Results

1. **Be Specific**: "Add dark mode to nav" vs "Make nav better"
2. **Provide Examples**: Show existing patterns to follow
3. **Set Constraints**: "Keep under 50 lines", "Mobile-first only"
4. **Request Explanations**: "Explain your approach"
5. **Iterate**: Refine through follow-up questions

## Error Handling

If Claude makes an error:

```
Prompt: The YAML you generated has a syntax error on line 15.
The description field is missing the pipe (|) for multi-line.
Please fix this.
```

Claude will:
- Acknowledge the error
- Fix the specific issue
- Explain what went wrong
- Provide the corrected version

## Integration with Project Workflow

### Pre-Commit

```bash
# Before committing Claude's changes:
bundle exec jekyll build
bundle exec jekyll serve --livereload
# Check in browser, especially mobile
```

### Review Checklist

After Claude makes changes:
- [ ] Does it build?
- [ ] Looks good in browser?
- [ ] Mobile responsive?
- [ ] No console errors?
- [ ] Attribution included?

## Resources

- Claude Code Docs: https://docs.claude.com/claude-code
- Project Context: `.ai/CONTEXT.md`
- Universal Rules: `AGENTS.md`
- Coding Conventions: `.ai/CONVENTIONS.md`

---

**Version**: 1.0
**Last Updated**: 2025-10-21
**Tool Versions**: Claude Sonnet 4.5

**Note**: Claude should always reference AGENTS.md first, then use this file for Claude-specific guidance.
