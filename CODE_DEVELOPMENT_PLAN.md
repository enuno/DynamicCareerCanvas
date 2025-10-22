# Code Development Plan

**Project**: DynamicCareerCanvas
**Type**: Single-page professional portfolio
**Approach**: Simple, practical, AI-friendly

This plan uses relaxed standards appropriate for a personal GitHub Pages site. It's meant to guide both human developers and AI coding assistants without unnecessary complexity.

---

## Project Overview

### What This Is

A professional portfolio website showcasing Elvis Nuno's work experience, projects, skills, and publications. Built with Jekyll, hosted on GitHub Pages, designed to be easy to edit and maintain.

### Goals

- **Simple**: Easy to understand and modify
- **Professional**: Clean, polished appearance
- **Accessible**: Works for everyone, all devices
- **Maintainable**: Content updates via YAML files, not code
- **Fast**: Loads quickly, performs well

### Not Goals

- Complex web app functionality
- Database integration
- Heavy JavaScript frameworks
- User authentication
- Real-time features

---

## System Architecture

### Technology Stack

```
Content (YAML) → Jekyll → Static HTML → GitHub Pages
```

**Components:**
- YAML files (_data/) - Content storage
- Liquid templates (_includes/, _layouts/) - HTML structure
- SCSS (_sass/) - Styling
- Vanilla JS (assets/js/) - Minimal interactivity
- GitHub Actions - Automated deployment

**That's it. Keep it simple.**

---

## AI Agent Roles

For AI coding assistants working on this project:

### Primary Tasks

1. **Content Management** - Update YAML files with new experience, projects, skills
2. **Component Creation** - Build reusable UI components following existing patterns
3. **Styling** - Write responsive SCSS using CSS variables
4. **Bug Fixes** - Fix layout, responsive, or functionality issues
5. **Documentation** - Keep docs in sync with code changes

### Agent Boundaries

**DO:**
- Follow existing patterns
- Use CSS variables
- Keep it simple
- Test mobile responsiveness
- Maintain accessibility

**DON'T:**
- Add frameworks (React, Vue, etc.)
- Hardcode content
- Skip testing
- Break the build
- Over-engineer solutions

### Agent Instructions

All AI agents should:
1. Read `AGENTS.md` first (universal rules)
2. Check tool-specific file (CLAUDE.md, CURSOR.md, etc.)
3. Review `.ai/CONTEXT.md` for project details
4. Follow `.ai/CONVENTIONS.md` for code style

---

## Coding Standards

### The Simple Rules

**YAML:**
- Use quotes on strings
- Dates in YYYY-MM format
- Keep it consistent

**HTML/Liquid:**
- Semantic elements where obvious
- Descriptive class names
- Alt text on images

**SCSS:**
- Use CSS variables
- Mobile-first media queries
- Keep it readable

**JavaScript:**
- ES6+ syntax
- No frameworks
- Progressive enhancement

**General:**
- If it builds and looks good, ship it
- Test on mobile (resize browser)
- Don't over-think it

### File Organization

```
_data/              # Content (edit frequently)
├── experience.yml
├── projects.yml
├── skills.yml
└── publications.yml

_includes/          # Templates
├── components/     # Reusable UI pieces
├── head.html
├── header.html
└── footer.html

_layouts/           # Page layouts
├── default.html
├── home.html
└── resume.html

_sass/              # Styles
├── base/           # Variables, resets
├── components/     # Component styles
├── layout/         # Layout styles
└── themes/         # Light/dark themes

assets/             # Static files
├── css/
├── js/
└── images/

pages/              # Site pages
└── *.md
```

---

## Implementation Approach

### Phase 1: Foundation (✓ Completed)

- [x] Project structure
- [x] AI documentation
- [x] Contribution guidelines
- [x] Security policies
- [x] Agent configuration files

### Phase 2: Data & Components (Current)

- [ ] Create YAML data structure
- [ ] Migrate content to YAML
- [ ] Build reusable components
- [ ] Set up CSS variables
- [ ] Implement base styles

### Phase 3: Design & Polish

- [ ] Implement modern design
- [ ] Add animations/interactions
- [ ] Optimize images
- [ ] Test cross-browser
- [ ] Verify accessibility

### Phase 4: Deployment

- [ ] Update CI/CD workflows
- [ ] Add utility scripts
- [ ] Performance testing
- [ ] Final documentation
- [ ] Launch!

### Ongoing

- Content updates via YAML
- Component improvements
- Performance monitoring
- Dependency updates

---

## Development Workflow

### Making Changes

Simple process for all contributors (human or AI):

1. **Understand what you're changing**
   - Read relevant docs
   - Check existing patterns

2. **Make the change**
   - Edit files
   - Follow conventions (loosely)

3. **Test it**
   ```bash
   bundle exec jekyll build
   bundle exec jekyll serve --livereload
   # Check in browser, especially mobile
   ```

4. **Commit it**
   ```
   Clear description of what changed

   AI-Assisted: [Tool Name] (if AI helped)
   ```

5. **Done**
   - That's it
   - No complicated process

### When Things Break

1. Check the error message
2. Build with verbose: `bundle exec jekyll build --verbose`
3. Common issues:
   - YAML syntax error
   - Missing include file
   - Invalid Liquid syntax
4. Fix it and try again

---

## Testing Strategy

### Required Testing

**Always do:**
- Does it build? (`bundle exec jekyll build`)
- Does it look right? (Check in browser)
- Mobile okay? (Resize to ~375px width)

**That covers 90% of issues.**

### Additional Testing (When Needed)

Do more thorough testing for:
- Major design changes
- New JavaScript features
- Accessibility-critical updates
- Before major releases

**Tests include:**
- Multiple screen sizes
- Light and dark mode
- Keyboard navigation
- Different browsers

### Performance

Quick checks:
- Page loads in < 2 seconds
- No huge images
- Minimal JavaScript

Use Lighthouse if you want detailed metrics, but don't obsess over perfect scores.

---

## Deployment & Operations

### Automated Deployment

GitHub Actions handles everything:

```
Push to main → Build → Deploy to GitHub Pages
```

**Current workflow:**
1. Jekyll builds site
2. GitHub Actions validates
3. Deploys to GitHub Pages
4. Live in ~2 minutes

### Manual Testing Before Merge

```bash
# Local build
bundle exec jekyll build

# Check output
bundle exec jekyll serve

# Visual inspection
# Mobile check
# Commit if good
```

### Rollback

If something breaks:
```bash
git revert <commit>
# or
git reset --hard <previous-commit>
```

---

## Security & Compliance

### Security Basics

**Never commit:**
- API keys
- Passwords
- Tokens
- .env files with secrets

**Always:**
- Use HTTPS for external resources
- Keep dependencies updated (Dependabot)
- Review AI-generated code
- Validate YAML input

### Accessibility

Maintain WCAG AA compliance:
- Alt text on images
- Semantic HTML
- Keyboard navigation
- Color contrast
- Heading hierarchy

Don't need to be perfect, but be thoughtful.

### Privacy

This is a public portfolio:
- No user data collection
- No cookies
- No analytics (unless explicitly added)
- No PII in commits

---

## AI Agent Guidelines

### For All AI Coding Assistants

**Before you code:**
1. Read `AGENTS.md` (universal rules)
2. Check your tool's file (CLAUDE.md, CURSOR.md, etc.)
3. Review `.ai/CONTEXT.md` (project context)
4. Understand what you're changing

**While coding:**
1. Follow existing patterns
2. Keep it simple
3. Use CSS variables
4. Make it responsive
5. Test as you go

**After coding:**
1. Build the site
2. Check in browser
3. Test mobile view
4. Commit with attribution

### Common AI Tasks

**Content Updates:**
```yaml
# Edit _data/experience.yml or similar
# Follow existing structure
# Build to verify
```

**New Components:**
```
1. Create _includes/components/name.html
2. Create _sass/components/_name.scss
3. Import SCSS
4. Test responsive
5. Document usage
```

**Bug Fixes:**
```
1. Reproduce issue
2. Identify cause
3. Fix with minimal changes
4. Test thoroughly
5. Commit fix
```

**Styling:**
```scss
// Use variables
.component {
  color: var(--color-primary);
  padding: var(--spacing-md);

  @media (max-width: 768px) {
    padding: var(--spacing-sm);
  }
}
```

### Attribution

Always include in commits when AI assisted:

```
AI-Assisted: [Tool Name]
Co-Authored-By: [AI Name] <email>
```

---

## Change Management

### Updating This Plan

This plan evolves with the project:

**When to update:**
- Architecture changes
- New conventions adopted
- Tool/process changes
- Phase completions

**How to update:**
1. Edit this file
2. Keep it simple
3. Commit changes
4. Note in `.ai/CHANGELOG_AI.md` if AI helped

### Communication

For this single-person project:
- Document decisions in code comments
- Update relevant .md files
- Keep `.ai/CONTEXT.md` current
- Note breaking changes in commits

---

## Quick Reference

### Essential Commands

```bash
# Build site
bundle exec jekyll build

# Serve locally with auto-reload
bundle exec jekyll serve --livereload

# Check git status
git status

# View changes
git diff
```

### Essential Files

- `AGENTS.md` - Universal AI rules
- `.ai/CONTEXT.md` - Project context
- `.ai/CONVENTIONS.md` - Code standards
- `DESIGNSYSTEM.md` - Visual standards
- `[TOOL].md` - Tool-specific guides

### Quick Checklist

Before committing:
- [ ] Builds successfully
- [ ] Looks right in browser
- [ ] Mobile responsive
- [ ] No console errors
- [ ] Attribution included (if AI)

---

## Success Criteria

### How We Know It's Working

**Functionality:**
- Site builds without errors
- All links work
- Forms work (if any)
- Mobile friendly

**Performance:**
- Loads in < 2 seconds
- Smooth interactions
- No janky animations

**Maintainability:**
- Easy to add content
- Clear where things are
- AI agents can help effectively
- Humans can edit without AI

**Quality:**
- Professional appearance
- Accessible to all users
- Works across browsers
- Good enough to ship

**Not perfection, but solid quality.**

---

## Troubleshooting

### Build Fails

```bash
# Verbose build
bundle exec jekyll build --verbose

# Common fixes:
# - Fix YAML syntax
# - Check include paths
# - Validate Liquid syntax
```

### AI Agent Issues

**Agent suggests frameworks:**
- Reject suggestion
- Remind: vanilla JavaScript only

**Agent's code doesn't match style:**
- Point to similar existing code
- Reference CONVENTIONS.md

**Agent breaks build:**
- Revert changes
- Try again with more specific instructions

### Design Issues

**Not responsive:**
- Check media queries
- Test at multiple sizes
- Use CSS Grid/Flexbox

**Dark mode broken:**
- Verify CSS variables used
- Check both themes

---

## Resources

### Documentation

- **AGENTS.md** - Universal AI agent rules
- **.ai/CONTEXT.md** - Detailed project context
- **.ai/CONVENTIONS.md** - Coding conventions
- **.ai/PROMPTS.md** - Reusable AI prompts
- **DESIGNSYSTEM.md** - Visual design standards
- **DEVELOPMENT_PLAN.md** - Overall project plan

### External Resources

- [Jekyll Docs](https://jekyllrb.com/docs/)
- [Liquid Syntax](https://shopify.github.io/liquid/)
- [GitHub Pages](https://docs.github.com/en/pages)
- [WCAG Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)

### Getting Help

- Check existing docs first
- Build locally to see errors
- Ask specific questions in GitHub Discussions
- Open issues for bugs

---

## Philosophy

### Keep It Simple

This is a portfolio site, not a complex application:
- Simple solutions beat clever ones
- Readable code beats concise code
- Working code beats perfect code
- Ship good enough, iterate later

### AI-Human Collaboration

AI agents are helpful assistants:
- They follow patterns
- They generate boilerplate
- They help with repetitive tasks
- But humans review everything

### Continuous Improvement

The site evolves:
- Content gets updated
- Design gets refined
- Code gets improved
- But it's never "done"

And that's okay.

---

**Version**: 1.0
**Last Updated**: 2025-10-21
**Status**: Active Development
**Next Phase**: Data structure & component creation

**Remember**: This is meant to be helpful, not restrictive. Use good judgment. Keep it simple. Ship it.
