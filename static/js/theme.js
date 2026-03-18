(function () {
  var STORAGE_KEY = 'theme';
  var root = document.documentElement;

  function getPreferred() {
    var stored = localStorage.getItem(STORAGE_KEY);
    if (stored === 'dark' || stored === 'light') return stored;
    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }

  function apply(theme) {
    root.setAttribute('data-theme', theme);
    localStorage.setItem(STORAGE_KEY, theme);
  }

  // Apply immediately in <head> — no flash of wrong theme
  apply(getPreferred());

  function handleToggle() {
    root.classList.add('theme-transitioning');
    var next = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
    apply(next);
    setTimeout(function () {
      root.classList.remove('theme-transitioning');
    }, 400);
  }

  document.addEventListener('DOMContentLoaded', function () {
    var btns = document.querySelectorAll('#theme-toggle, #theme-toggle-mobile');
    for (var i = 0; i < btns.length; i++) {
      btns[i].addEventListener('click', handleToggle);
    }
  });
})();
