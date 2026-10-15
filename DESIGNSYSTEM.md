# Design System

Visual and interaction standards for DynamicCareerCanvas. Tokens live in
`_sass/base/_variables.scss`; components live in `_sass/components/`.

**For AI agents**: use these tokens and patterns. Do not add colors, fonts, or
shadows outside the token set.

## Direction

An editorial engineering portfolio for an infrastructure and systems
engineer. Precise, quiet, and technical:

- Charcoal/slate foundations, one restrained teal accent.
- Strong type hierarchy, generous spacing, ruled lines instead of card grids.
- Monospace only for metadata, labels, and annotations, never for paragraphs.
- Diagrams only when they explain structure (hero stack, agent flow), and
  always labeled as conceptual.

Avoid: gradients, glassmorphism, glow, autoplay or scroll-driven animation,
skill bars or scores, stock imagery, fake terminals.

## Themes

Dark and light share token names. Order of precedence:

1. A stored visitor choice (`data-theme` on `<html>`, set by
   `assets/js/theme-toggle.js` and the inline script in `_includes/head.html`).
2. Otherwise the system `prefers-color-scheme`.
3. Without JavaScript, the system preference still applies (pure CSS).

| Token | Dark | Light | Use |
|---|---|---|---|
| `--color-background` | `#0e1216` | `#f6f7f9` | Page |
| `--color-surface` | `#141a20` | `#ffffff` | Panels |
| `--color-surface-2` | `#1a2129` | `#eef1f4` | Asides, hover |
| `--color-border` | `#26303a` | `#dde2e8` | Rules |
| `--color-border-strong` | `#3a4654` | `#b9c2cd` | Section rules, outlines |
| `--color-text-primary` | `#e7ebef` | `#121820` | Headings, body |
| `--color-text-secondary` | `#aab4bf` | `#44505d` | Paragraphs |
| `--color-text-muted` | `#8a95a2` | `#5b6774` | Metadata |
| `--color-accent` | `#4cc9b9` | `#0d6d66` | Links, labels, primary button |
| `--color-on-accent` | `#04201c` | `#ffffff` | Text on accent |

Aliases kept for older docs: `--color-primary` → accent, `--color-text` →
text-primary.

Measured contrast (WCAG 2.x): every text token passes 4.5:1 on every
background token in both themes; the lowest pair is muted on surface-2
(5.09:1 light, 5.34:1 dark). Primary button text: 8.43:1 dark, 6.18:1 light.

## Typography

System fonts only (no external requests):

```scss
--font-sans: ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, ...;
--font-mono: ui-monospace, "SF Mono", SFMono-Regular, Menlo, Consolas, ...;
```

| Token | Value |
|---|---|
| `--font-size-xs` … `--font-size-xl` | 0.75 / 0.875 / 1 / 1.125 / 1.25 rem |
| `--font-size-2xl` | `clamp(1.375rem, 1.2rem + 0.8vw, 1.75rem)` |
| `--font-size-3xl` | `clamp(1.75rem, 1.4rem + 1.6vw, 2.5rem)` |
| `--font-size-display` | `clamp(2.75rem, 1.9rem + 4.2vw, 5rem)` (hero name) |
| `--measure` | `68ch` (paragraph width) |

`.meta` and `.label` are the mono, uppercase metadata styles.

## Spacing and layout

- Scale: `--spacing-xs` (0.25rem) to `--spacing-3xl` (4.5rem).
- `--spacing-section` and `--spacing-hero` are fluid (`clamp()`).
- `--gutter`: 1rem below 768px, 2rem above. Container max width 1200px.
- Breakpoints (mobile first, `min-width`): 640, 768, 1024, 1280px.
- Section header: mono index (`01 / Work`) in a 3fr column, title and lede in
  9fr, above a strong rule.

**Ruby Sass note:** GitHub Pages compiles with Ruby Sass 3.7, which tries to
evaluate `clamp()`, `min()`, and `max()` arithmetic in ordinary properties.
Put fluid values in custom properties (as above) and use `var()`.

## Component patterns

| Pattern | Files | Notes |
|---|---|---|
| Button | `_button.scss` | 44px minimum target. `--primary` (accent fill), default (outline), `--ghost` |
| Navigation | `_nav.scss`, `nav-toggle.js` | Disclosure below 1024px; `aria-expanded` + `aria-controls`; Escape closes and returns focus |
| Hero + stack diagram | `_hero.scss`, `_stack.scss` | Three layers on a dashed rail; links to featured projects |
| Flagship project | `_project.scss` | Content plus metrics aside; snapshot date shown with metrics |
| Project panel | `_project.scss` | Related pair (Noesis); status line with source and date |
| Agent flow | `_flow.scss` | Ordered list on a rail; checkpoints have square nodes and a badge |
| Ruled lists | `_work-index.scss`, `_timeline.scss`, `_domain.scss`, `_contact.scss` | Lines, not cards |

Shared helpers: `.label`, `.ticks` (dash bullets; `--guard` for safety
controls), `.evidence` (link list), `.tags` (mono outline chips), `.status`,
`.callout`, `.note`.

## Interaction and motion

- Transitions: `--transition` (160ms) on color and border only.
- Smooth scrolling only under `prefers-reduced-motion: no-preference`.
- Reduced motion collapses all transitions and animations.
- External links keep the same tab and carry a decorative `↗`
  (`aria-hidden="true"`). Screen-reader text names the project in repeated
  link labels.

## Accessibility checklist

- One `h1` per page; heading levels do not skip.
- Skip link to `#main`; visible `:focus-visible` outline (2px accent).
- Images have `alt`, `width`, and `height`. Decorative logos use `alt=""`.
- No `aria-label` or `aria-labelledby` on generic `<div>`s.
- `tests/test_built_site.py` checks most of the above on every build.

---

**Version**: 2.0
**Last Updated**: 2026-10-15
**Maintained By**: Elvis Nuno
