# Design System

This document defines the visual and interaction design standards for DynamicCareerCanvas.

**For AI Agents**: Follow these design guidelines when creating or modifying UI components.

## Design Principles

1. **Simple & Clean** - Minimal, focused design
2. **Professional** - Polished and credible
3. **Accessible** - WCAG AA compliant
4. **Responsive** - Mobile-first approach
5. **Consistent** - Unified visual language

## Color System

### Light Theme

```scss
--color-primary: #2c3e50;      // Dark blue-gray
--color-accent: #3498db;       // Bright blue
--color-surface: #ffffff;      // White
--color-background: #f8f9fa;   // Light gray
--color-text-primary: #2c3e50; // Dark text
--color-text-secondary: #7f8c8d; // Gray text
--color-border: #e1e4e8;       // Light border
--color-success: #27ae60;      // Green
--color-warning: #f39c12;      // Orange
--color-error: #e74c3c;        // Red
```

### Dark Theme

```scss
--color-primary: #3498db;      // Bright blue
--color-accent: #5dade2;       // Light blue
--color-surface: #1e2a3a;      // Dark blue-gray
--color-background: #0f1419;   // Very dark
--color-text-primary: #e1e8ed; // Light text
--color-text-secondary: #8899a6; // Gray text
--color-border: #2a3f54;       // Dark border
--color-success: #2ecc71;      // Bright green
--color-warning: #f1c40f;      // Bright orange
--color-error: #e67e22;        // Bright red
```

## Typography

### Font Stack

```scss
--font-family-base: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
--font-family-mono: 'SF Mono', Monaco, 'Cascadia Code', 'Roboto Mono', Consolas, 'Courier New', monospace;
```

### Font Sizes

```scss
--font-size-xs: 0.75rem;   // 12px
--font-size-sm: 0.875rem;  // 14px
--font-size-base: 1rem;    // 16px
--font-size-lg: 1.125rem;  // 18px
--font-size-xl: 1.25rem;   // 20px
--font-size-2xl: 1.5rem;   // 24px
--font-size-3xl: 1.875rem; // 30px
--font-size-4xl: 2.25rem;  // 36px
```

### Font Weights

```scss
--font-weight-normal: 400;
--font-weight-medium: 500;
--font-weight-semibold: 600;
--font-weight-bold: 700;
```

### Line Heights

```scss
--line-height-tight: 1.25;
--line-height-normal: 1.5;
--line-height-relaxed: 1.75;
```

## Spacing Scale

```scss
--spacing-xs: 0.25rem;   // 4px
--spacing-sm: 0.5rem;    // 8px
--spacing-md: 1rem;      // 16px
--spacing-lg: 1.5rem;    // 24px
--spacing-xl: 2rem;      // 32px
--spacing-2xl: 3rem;     // 48px
--spacing-3xl: 4rem;     // 64px
```

## Border Radius

```scss
--radius-sm: 0.25rem;  // 4px
--radius-md: 0.5rem;   // 8px
--radius-lg: 1rem;     // 16px
--radius-full: 9999px; // Fully rounded
```

## Shadows

```scss
--shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.1);
--shadow-md: 0 4px 6px rgba(0, 0, 0, 0.1);
--shadow-lg: 0 10px 15px rgba(0, 0, 0, 0.1);
--shadow-xl: 0 20px 25px rgba(0, 0, 0, 0.1);
```

## Breakpoints

```scss
// Mobile first approach
$breakpoint-sm: 576px;   // Small devices (phones)
$breakpoint-md: 768px;   // Medium devices (tablets)
$breakpoint-lg: 992px;   // Large devices (desktops)
$breakpoint-xl: 1200px;  // Extra large devices
```

Usage:
```scss
.component {
  // Mobile styles first
  padding: var(--spacing-sm);

  @media (min-width: 768px) {
    // Tablet
    padding: var(--spacing-md);
  }

  @media (min-width: 992px) {
    // Desktop
    padding: var(--spacing-lg);
  }
}
```

## Component Patterns

### Cards

Standard card pattern:

```scss
.card {
  background: var(--color-surface);
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-sm);
  padding: var(--spacing-lg);
  transition: transform 0.2s ease, box-shadow 0.2s ease;

  &:hover {
    transform: translateY(-2px);
    box-shadow: var(--shadow-md);
  }
}
```

### Buttons

Button styles:

```scss
.button {
  display: inline-flex;
  align-items: center;
  gap: var(--spacing-sm);
  padding: var(--spacing-sm) var(--spacing-lg);
  background: var(--color-primary);
  color: var(--color-surface);
  border: none;
  border-radius: var(--radius-md);
  font-weight: var(--font-weight-medium);
  text-decoration: none;
  transition: background 0.2s ease, transform 0.1s ease;
  cursor: pointer;

  &:hover {
    background: var(--color-accent);
    transform: scale(1.02);
  }

  &:active {
    transform: scale(0.98);
  }

  &--secondary {
    background: transparent;
    color: var(--color-primary);
    border: 1px solid var(--color-border);
  }

  &--small {
    padding: var(--spacing-xs) var(--spacing-md);
    font-size: var(--font-size-sm);
  }
}
```

### Badges/Tags

```scss
.badge {
  display: inline-block;
  padding: var(--spacing-xs) var(--spacing-sm);
  background: var(--color-background);
  color: var(--color-text-primary);
  border-radius: var(--radius-sm);
  font-size: var(--font-size-sm);
  font-weight: var(--font-weight-medium);
}
```

## Layout Patterns

### Container

```scss
.container {
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 var(--spacing-md);

  @media (min-width: 768px) {
    padding: 0 var(--spacing-lg);
  }
}
```

### Grid

```scss
.grid {
  display: grid;
  gap: var(--spacing-md);
  grid-template-columns: 1fr;

  @media (min-width: 768px) {
    grid-template-columns: repeat(2, 1fr);
  }

  @media (min-width: 992px) {
    grid-template-columns: repeat(3, 1fr);
  }
}
```

## Animation

### Timing Functions

```scss
--timing-ease: ease;
--timing-ease-in: ease-in;
--timing-ease-out: ease-out;
--timing-ease-in-out: ease-in-out;
```

### Durations

```scss
--duration-fast: 0.1s;
--duration-normal: 0.2s;
--duration-slow: 0.3s;
```

### Common Animations

```scss
// Fade in
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

// Slide in
@keyframes slideIn {
  from {
    transform: translateX(-20px);
    opacity: 0;
  }
  to {
    transform: translateX(0);
    opacity: 1;
  }
}
```

## Accessibility Guidelines

### Color Contrast

- Text: Minimum 4.5:1 ratio
- Large text (18px+): Minimum 3:1 ratio
- UI components: Minimum 3:1 ratio

### Focus States

```scss
:focus-visible {
  outline: 2px solid var(--color-accent);
  outline-offset: 2px;
}
```

### Reduced Motion

```scss
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

## Icons

- Use SVG icons where possible
- Ensure icons have labels (aria-label or sr-only text)
- Decorative icons: `aria-hidden="true"`
- Icon size: 16px, 20px, 24px (use CSS variables)

## Images

- Optimize all images before adding
- Use appropriate formats (WebP with fallback)
- Always include alt text
- Responsive images with srcset

## Forms

### Input Fields

```scss
.input {
  width: 100%;
  padding: var(--spacing-sm) var(--spacing-md);
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  font-size: var(--font-size-base);
  color: var(--color-text-primary);
  transition: border-color 0.2s ease, box-shadow 0.2s ease;

  &:focus {
    outline: none;
    border-color: var(--color-accent);
    box-shadow: 0 0 0 3px rgba(52, 152, 219, 0.1);
  }

  &::placeholder {
    color: var(--color-text-secondary);
  }
}
```

## Usage for AI Agents

When creating new components:

1. **Use CSS Variables** - Always use defined variables
2. **Follow Patterns** - Match existing component styles
3. **Mobile First** - Start with mobile, expand for larger screens
4. **Accessibility** - Include ARIA labels, keyboard navigation
5. **Dark Mode** - Use color variables that support both themes
6. **Consistent Spacing** - Use spacing scale
7. **Smooth Transitions** - Add subtle animations
8. **Test Contrast** - Ensure readable color combinations

### Example Component

```scss
.new-component {
  // Layout
  display: flex;
  flex-direction: column;
  gap: var(--spacing-md);

  // Spacing
  padding: var(--spacing-lg);
  margin-bottom: var(--spacing-md);

  // Visual
  background: var(--color-surface);
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-sm);

  // Typography
  font-size: var(--font-size-base);
  line-height: var(--line-height-normal);
  color: var(--color-text-primary);

  // Animation
  transition: transform var(--duration-normal) var(--timing-ease);

  &:hover {
    transform: translateY(-2px);
  }

  // Responsive
  @media (min-width: 768px) {
    flex-direction: row;
    padding: var(--spacing-xl);
  }
}
```

---

**Version**: 1.0
**Last Updated**: 2025-10-21
**Maintained By**: Elvis Nuno

**Note to AI Agents**: Use this design system as your guide for all visual components. Consistency is key!
