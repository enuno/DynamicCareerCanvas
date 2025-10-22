# OpenAI Codex Configuration

This file contains rules and context specific to **OpenAI Codex** and GPT-based coding assistants.

**Primary Reference**: See [AGENTS.md](AGENTS.md) for universal AI agent guidelines.

## Codex Overview

Codex (and GPT-4/GPT-3.5 based tools) can:
- Generate code from natural language
- Complete code snippets
- Explain existing code
- Refactor and optimize
- Write tests
- Generate documentation

## Project Context for Codex

**Project**: DynamicCareerCanvas
**Repository**: enuno/DynamicCareerCanvas
**Type**: Static portfolio website
**Technology**: Jekyll, GitHub Pages
**Languages**: HTML (Liquid), SCSS, JavaScript, YAML
**Constraints**: No frameworks, data-driven, responsive

## Using Codex for This Project

### Code Generation

Provide clear context:

```
Language: Liquid (Jekyll templating)
Task: Create a component that displays work experience from YAML data

Context: We use _data/experience.yml for content. Each entry has:
- company (string)
- title (string)
- location (string)
- start_date (YYYY-MM)
- end_date (YYYY-MM or null if current)
- description (multi-line string)
- highlights (array of strings)
- technologies (array of strings)

Requirements:
- Semantic HTML
- BEM class naming
- Responsive design
- Accessible (ARIA labels)
- Support dark mode

Generate: _includes/components/experience-card.html
```

### Code Completion

Codex excels at completing patterns:

```liquid
<!-- Start typing: -->
{% for exp in site.data.experience %}
  <div class="experience-card">
    <!-- Codex completes based on YAML structure -->
```

```scss
// Start typing:
.experience-card {
  // Codex suggests properties
  padding: var(--
  // Codex knows CSS variables from project
```

### Code Explanation

```
Explain this Jekyll configuration:

[paste _config.yml section]

What does each setting do and how does it affect the build?
```

### Refactoring

```
Refactor this component to use CSS Grid instead of Flexbox:

[paste SCSS]

Requirements:
- Same responsive behavior
- Maintain browser support
- Use existing CSS variables
- Keep it readable
```

## Codex-Specific Instructions

### When Generating HTML/Liquid

Codex should produce:
```liquid
<!-- Component: Experience Card
     Displays work experience entry from YAML data
     Usage: {% include components/experience-card.html experience=exp %} -->

<article class="experience-card">
  <header class="experience-card__header">
    <h3 class="experience-card__title">{{ include.experience.title }}</h3>
    <p class="experience-card__company">{{ include.experience.company }}</p>
  </header>

  <div class="experience-card__meta">
    <time class="experience-card__dates">
      {{ include.experience.start_date | date: "%b %Y" }} -
      {% if include.experience.current %}Present{% else %}{{ include.experience.end_date | date: "%b %Y" }}{% endif %}
    </time>
    <span class="experience-card__location">{{ include.experience.location }}</span>
  </div>

  <div class="experience-card__description">
    {{ include.experience.description | markdownify }}
  </div>

  {% if include.experience.highlights %}
  <ul class="experience-card__highlights">
    {% for highlight in include.experience.highlights %}
    <li>{{ highlight }}</li>
    {% endfor %}
  </ul>
  {% endif %}

  {% if include.experience.technologies %}
  <div class="experience-card__technologies">
    {% for tech in include.experience.technologies %}
    <span class="badge">{{ tech }}</span>
    {% endfor %}
  </div>
  {% endif %}
</article>
```

### When Generating SCSS

Codex should use:
```scss
// Component: Experience Card
// Styles for work experience display

.experience-card {
  // Layout
  display: flex;
  flex-direction: column;
  gap: var(--spacing-md);

  // Spacing
  padding: var(--spacing-lg);
  margin-bottom: var(--spacing-md);

  // Visual
  background-color: var(--color-surface);
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-sm);

  // Interaction
  transition: transform 0.2s ease, box-shadow 0.2s ease;

  &:hover {
    transform: translateY(-2px);
    box-shadow: var(--shadow-md);
  }

  // BEM Elements
  &__header {
    display: flex;
    flex-direction: column;
    gap: var(--spacing-xs);
  }

  &__title {
    margin: 0;
    font-size: var(--font-size-xl);
    font-weight: var(--font-weight-bold);
    color: var(--color-text-primary);
  }

  &__company {
    margin: 0;
    font-size: var(--font-size-lg);
    color: var(--color-accent);
  }

  // Responsive
  @media (max-width: 768px) {
    padding: var(--spacing-md);
    gap: var(--spacing-sm);

    &__title {
      font-size: var(--font-size-lg);
    }
  }
}
```

### When Generating JavaScript

Codex should produce vanilla JavaScript:

```javascript
/**
 * Experience Timeline
 * Handles timeline animations and interactions
 */

(function() {
  'use strict';

  /**
   * Initialize timeline
   */
  const initTimeline = () => {
    const timeline = document.querySelector('.timeline');
    if (!timeline) return;

    const entries = timeline.querySelectorAll('.timeline-entry');

    // Intersection Observer for scroll animations
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
        }
      });
    }, {
      threshold: 0.1,
      rootMargin: '0px 0px -50px 0px'
    });

    // Observe each entry
    entries.forEach(entry => observer.observe(entry));
  };

  // Initialize on DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initTimeline);
  } else {
    initTimeline();
  }
})();
```

### When Generating YAML

Codex should maintain structure:

```yaml
# Work Experience Entry
- company: "Company Name"
  title: "Job Title"
  location: "City, State/Country"
  start_date: "2024-01"
  end_date: "2024-08"  # or null if current
  current: false
  description: |
    Brief description of the role and responsibilities.
    Can span multiple lines.
  highlights:
    - "Key achievement or responsibility one"
    - "Key achievement or responsibility two"
    - "Key achievement or responsibility three"
  technologies:
    - "Technology 1"
    - "Technology 2"
    - "Technology 3"
```

## Codex Workflows

### 1. Feature Implementation

```
Prompt: Implement a skills section that displays technical skills
organized by category (Networking, Systems, DevOps, etc.).

Requirements:
- Data from _data/skills.yml
- Grid layout (responsive)
- Skill badges/tags
- Category headers
- Filterable (optional)
- Dark mode support

Generate:
1. YAML structure for _data/skills.yml
2. Component template
3. SCSS styling
4. JavaScript for filtering (if needed)
```

### 2. Bug Fixing

```
Prompt: Fix this navigation bug where mobile menu doesn't close
when clicking outside.

Current code:
[paste code]

Expected behavior: Menu should close when clicking outside the nav

Generate the fix with explanation.
```

### 3. Optimization

```
Prompt: Optimize this SCSS for better performance and maintainability.

Current code:
[paste SCSS]

Improve:
- Remove redundancy
- Use CSS variables consistently
- Better organization
- Add comments
```

### 4. Testing

```
Prompt: Generate test cases for the theme toggle functionality.

Code:
[paste theme toggle code]

Generate:
- Test scenarios
- Expected behaviors
- Edge cases
- Manual test instructions
```

## Best Practices with Codex

### DO

✓ Provide full context in prompts
✓ Specify language/framework clearly
✓ Show examples of desired output
✓ Request explanations
✓ Ask for multiple alternatives
✓ Validate generated code

### DON'T

✗ Assume Codex knows project specifics
✗ Use generated code without review
✗ Skip testing
✗ Forget to specify constraints
✗ Miss error handling

## Codex Attribution

Include in commits:

```
AI-Assisted: OpenAI Codex / GPT-4
Tool: [API / ChatGPT / etc.]
Co-Authored-By: OpenAI Codex <noreply@openai.com>
```

## Common Codex Prompts

### Generate Component

```
Create a [component name] component for Jekyll.

Data source: _data/[file].yml
Structure: [describe data structure]
Requirements: [list requirements]
Style: [design notes]

Generate both HTML template and SCSS.
```

### Explain Code

```
Explain this code in detail:

[paste code]

What does it do?
How does it work?
Are there any issues?
How could it be improved?
```

### Refactor

```
Refactor this code to be more [maintainable/performant/readable]:

[paste code]

Constraints: [list constraints]
Requirements: [list requirements]
```

### Debug

```
This code has a bug:

[paste code]

Error message:
[paste error]

What's wrong and how to fix it?
```

## Integration with Jekyll

Codex understands Jekyll/Liquid:

```
Generate a Jekyll layout that:
- Extends default layout
- Has a sidebar
- Includes navigation
- Responsive
- Supports page front matter variables
```

## Testing Codex Output

Always test generated code:

```bash
# Build Jekyll site
bundle exec jekyll build

# Check for errors
# Validate YAML syntax
# Test in browser
# Check responsive design
# Verify accessibility
```

## Codex Limitations

- May suggest frameworks (reject if inappropriate)
- Doesn't know project-specific patterns (provide examples)
- Can't test code (you must test)
- May not optimize for accessibility (review carefully)
- Doesn't see final rendered output

## Resources

- OpenAI Docs: https://platform.openai.com/docs
- Project Context: `.ai/CONTEXT.md`
- Universal Rules: `AGENTS.md`
- Code Examples: Review existing components

---

**Version**: 1.0
**Last Updated**: 2025-10-21
**Compatible with**: GPT-4, GPT-3.5-turbo, Codex

**Note**: Codex is powerful but requires clear instructions. Always review and test generated code.
