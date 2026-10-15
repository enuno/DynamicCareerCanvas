/**
 * Navigation Toggle
 * Opens and closes the primary menu on narrow screens.
 *
 * The menu is a disclosure: the toggle button carries aria-expanded and
 * aria-controls; the menu gets the .is-open class. Escape, a link click, or
 * a click outside closes it. Escape returns focus to the toggle.
 *
 * Exported for tests (Node); runs automatically in the browser.
 */
(function () {
  'use strict';

  /**
   * Wire up the menu disclosure.
   * @param {Element|null} toggle - the button that opens and closes the menu
   * @param {Element|null} menu - the element that holds the links
   * @param {Document|Element} doc - where global key and click events arrive
   */
  const initNav = (toggle, menu, doc) => {
    if (!toggle || !menu) return;

    const isOpen = () => menu.classList.contains('is-open');

    const setOpen = (open) => {
      menu.classList.toggle('is-open', open);
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    };

    toggle.addEventListener('click', () => setOpen(!isOpen()));

    menu.querySelectorAll('a').forEach((link) => {
      link.addEventListener('click', () => setOpen(false));
    });

    doc.addEventListener('keydown', (event) => {
      if (event.key === 'Escape' && isOpen()) {
        setOpen(false);
        toggle.focus();
      }
    });

    doc.addEventListener('click', (event) => {
      if (isOpen() && !menu.contains(event.target) && !toggle.contains(event.target)) {
        setOpen(false);
      }
    });
  };

  if (typeof module !== 'undefined' && module.exports) {
    module.exports = { initNav };
  } else {
    initNav(document.querySelector('.nav__toggle'), document.getElementById('site-menu'), document);
  }
})();
