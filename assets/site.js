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
      count.textContent = `${visible} ${visible === 1 ? 'project' : 'projects'}`;
    });
  }
}
