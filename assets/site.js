const filters = document.querySelectorAll('[data-filter]');
const projects = document.querySelectorAll('[data-category]');
const count = document.querySelector('#project-count');
if (filters.length && projects.length) {
  document.querySelector('.filters').hidden = false;
  for (const button of filters) {
    button.addEventListener('click', () => {
      for (const filter of filters) filter.setAttribute('aria-pressed', String(filter === button));
      let visible = 0;
      for (const project of projects) {
        project.hidden = button.dataset.filter !== 'all' && !project.dataset.category.split(' ').includes(button.dataset.filter);
        if (!project.hidden) visible++;
      }
      const german = document.documentElement.lang === 'de';
      const noun = german ? (visible === 1 ? 'Projekt' : 'Projekte') : (visible === 1 ? 'project' : 'projects');
      count.textContent = `${visible} ${noun}`;
    });
  }
}

// Explicit navigation only: English at the root always stays the default.
// Matching IDs let visitors keep their section when switching language.
for (const link of document.querySelectorAll('[data-language]')) {
  link.addEventListener('click', () => {
    const destination = new URL(link.href);
    destination.hash = window.location.hash;
    link.href = destination.href;
  });
}

for (const menu of document.querySelectorAll('.language-menu')) {
  menu.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') {
      menu.open = false;
      menu.querySelector('summary').focus();
    }
  });
  document.addEventListener('click', (event) => {
    if (!menu.contains(event.target)) menu.open = false;
  });
}

const exampleButtons = document.querySelectorAll('[data-example]');
const examplePanels = document.querySelectorAll('[data-example-panel]');
if (exampleButtons.length && examplePanels.length) {
  const selectExample = (id) => {
    for (const button of exampleButtons) button.setAttribute('aria-pressed', String(button.dataset.example === id));
    for (const panel of examplePanels) panel.hidden = panel.dataset.examplePanel !== id;
  };
  document.querySelector('.example-controls').hidden = false;
  for (const button of exampleButtons) button.addEventListener('click', () => selectExample(button.dataset.example));
  selectExample(exampleButtons[0].dataset.example);
}
