const themeToggle = document.querySelector('.theme-toggle');
const icon = document.querySelector('.theme-toggle__icon');
const text = document.querySelector('.theme-toggle__text');
const prefersLight = window.matchMedia('(prefers-color-scheme: light)').matches;
const savedTheme = localStorage.getItem('aios-theme');

const applyTheme = (theme) => {
  document.body.setAttribute('data-theme', theme);
  if (theme === 'light') {
    icon.textContent = '☀️';
    text.textContent = 'Light';
  } else {
    icon.textContent = '🌙';
    text.textContent = 'Dark';
  }
};

const initialTheme = savedTheme || (prefersLight ? 'light' : 'dark');
applyTheme(initialTheme);

themeToggle?.addEventListener('click', () => {
  const current = document.body.getAttribute('data-theme') === 'light' ? 'dark' : 'light';
  applyTheme(current);
  localStorage.setItem('aios-theme', current);
});

const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  },
  { threshold: 0.12 }
);

document.querySelectorAll('.reveal').forEach((item) => observer.observe(item));

document.getElementById('year').textContent = new Date().getFullYear();
