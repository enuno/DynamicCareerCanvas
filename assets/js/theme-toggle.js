/**
 * Theme Toggle
 * Switches between light and dark themes.
 *
 * Without a stored choice, the page follows the system color scheme (CSS).
 * Clicking the button stores an explicit choice in localStorage and sets
 * data-theme on <html>. The inline script in _includes/head.html applies a
 * stored choice before first paint.
 */
(function () {
  'use strict';

  const button = document.getElementById('theme-toggle');
  if (!button) return;

  const root = document.documentElement;
  const systemDark = window.matchMedia('(prefers-color-scheme: dark)');

  const currentTheme = () =>
    root.getAttribute('data-theme') || (systemDark.matches ? 'dark' : 'light');

  const updateLabel = () => {
    const next = currentTheme() === 'dark' ? 'light' : 'dark';
    button.setAttribute('aria-label', `Switch to ${next} theme`);
  };

  button.addEventListener('click', () => {
    const next = currentTheme() === 'dark' ? 'light' : 'dark';
    root.setAttribute('data-theme', next);
    try {
      localStorage.setItem('theme', next);
    } catch (e) {
      // Storage can be unavailable (private mode); the choice lasts for this page only.
    }
    updateLabel();
  });

  systemDark.addEventListener('change', updateLabel);
  updateLabel();
})();
