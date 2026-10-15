// Tests for assets/js/nav-toggle.js (run: node --test tests/)
// Uses small DOM stand-ins so the real controller logic runs without a browser.

const test = require('node:test');
const assert = require('node:assert/strict');
const { initNav } = require('../assets/js/nav-toggle.js');

class FakeElement {
  constructor(children = []) {
    this.attrs = {};
    this.classes = new Set();
    this.listeners = {};
    this.children = children;
    this.focused = false;
    this.classList = {
      add: (c) => this.classes.add(c),
      remove: (c) => this.classes.delete(c),
      contains: (c) => this.classes.has(c),
      toggle: (c, force) => (force ? this.classes.add(c) : this.classes.delete(c), force),
    };
  }
  setAttribute(name, value) { this.attrs[name] = String(value); }
  getAttribute(name) { return this.attrs[name] ?? null; }
  addEventListener(type, fn) { (this.listeners[type] ||= []).push(fn); }
  dispatch(type, event = {}) { (this.listeners[type] || []).forEach((fn) => fn({ target: this, ...event })); }
  contains(node) { return node === this || this.children.some((c) => c === node || c.contains(node)); }
  querySelectorAll() { return this.children; }
  focus() { this.focused = true; }
}

const setup = () => {
  const links = [new FakeElement(), new FakeElement()];
  const menu = new FakeElement(links);
  const toggle = new FakeElement();
  const doc = new FakeElement();
  toggle.setAttribute('aria-expanded', 'false');
  initNav(toggle, menu, doc);
  return { toggle, menu, links, doc, outside: new FakeElement() };
};

const isOpen = ({ toggle, menu }) => {
  assert.equal(toggle.getAttribute('aria-expanded') === 'true', menu.classList.contains('is-open'),
    'aria-expanded and the menu class must agree');
  return menu.classList.contains('is-open');
};

test('starts closed with aria-expanded="false"', () => {
  const nav = setup();
  assert.equal(isOpen(nav), false);
  assert.equal(nav.toggle.getAttribute('aria-expanded'), 'false');
});

test('toggle button opens and closes the menu', () => {
  const nav = setup();
  nav.toggle.dispatch('click');
  assert.equal(isOpen(nav), true);
  nav.toggle.dispatch('click');
  assert.equal(isOpen(nav), false);
});

test('Escape closes an open menu and returns focus to the toggle', () => {
  const nav = setup();
  nav.toggle.dispatch('click');
  nav.doc.dispatch('keydown', { key: 'Escape' });
  assert.equal(isOpen(nav), false);
  assert.equal(nav.toggle.focused, true);
});

test('Escape does nothing when the menu is closed', () => {
  const nav = setup();
  nav.doc.dispatch('keydown', { key: 'Escape' });
  assert.equal(isOpen(nav), false);
  assert.equal(nav.toggle.focused, false);
});

test('choosing a link closes the menu', () => {
  const nav = setup();
  nav.toggle.dispatch('click');
  nav.links[1].dispatch('click');
  assert.equal(isOpen(nav), false);
});

test('a click outside closes the menu; a click inside does not', () => {
  const nav = setup();
  nav.toggle.dispatch('click');
  nav.doc.dispatch('click', { target: nav.menu });
  assert.equal(isOpen(nav), true);
  nav.doc.dispatch('click', { target: nav.outside });
  assert.equal(isOpen(nav), false);
});

test('missing elements are ignored without throwing', () => {
  assert.doesNotThrow(() => initNav(null, null, new FakeElement()));
});
