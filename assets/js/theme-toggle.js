/**
 * Theme Toggle
 * Handles light/dark mode switching
 */

(function() {
  'use strict';

  const themeToggle = document.getElementById('theme-toggle');
  const html = document.documentElement;

  // Get saved theme or default to light
  const getCurrentTheme = () => {
    return localStorage.getItem('theme') || 'light';
  };

  // Set theme
  const setTheme = (theme) => {
    html.setAttribute('data-theme', theme);
    localStorage.setItem('theme', theme);
    updateToggleIcon(theme);
  };

  // Update toggle button icon
  const updateToggleIcon = (theme) => {
    const icon = themeToggle.querySelector('.theme-toggle__icon');
    if (icon) {
      icon.textContent = theme === 'dark' ? '☀️' : '🌙';
    }
  };

  // Toggle theme
  const toggleTheme = () => {
    const currentTheme = getCurrentTheme();
    const newTheme = currentTheme === 'light' ? 'dark' : 'light';
    setTheme(newTheme);
  };

  // Initialize
  if (themeToggle) {
    // Set initial icon
    updateToggleIcon(getCurrentTheme());

    // Add event listener
    themeToggle.addEventListener('click', toggleTheme);
  }
})();
