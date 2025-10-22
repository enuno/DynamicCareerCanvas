/**
 * Navigation Toggle
 * Handles mobile navigation menu
 */

(function() {
  'use strict';

  const navToggle = document.querySelector('.nav__toggle');
  const navMenu = document.querySelector('.nav__menu');

  if (!navToggle || !navMenu) return;

  const toggleNav = () => {
    const isOpen = navMenu.classList.contains('is-open');

    if (isOpen) {
      navMenu.classList.remove('is-open');
      navToggle.classList.remove('is-active');
      navToggle.setAttribute('aria-expanded', 'false');
    } else {
      navMenu.classList.add('is-open');
      navToggle.classList.add('is-active');
      navToggle.setAttribute('aria-expanded', 'true');
    }
  };

  // Toggle on button click
  navToggle.addEventListener('click', toggleNav);

  // Close on link click (mobile)
  const navLinks = navMenu.querySelectorAll('.nav__link');
  navLinks.forEach(link => {
    link.addEventListener('click', () => {
      if (navMenu.classList.contains('is-open')) {
        toggleNav();
      }
    });
  });

  // Close on escape key
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && navMenu.classList.contains('is-open')) {
      toggleNav();
    }
  });

  // Close when clicking outside
  document.addEventListener('click', (e) => {
    if (navMenu.classList.contains('is-open') &&
        !navMenu.contains(e.target) &&
        !navToggle.contains(e.target)) {
      toggleNav();
    }
  });
})();
