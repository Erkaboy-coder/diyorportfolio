// Contact form simulation
document.getElementById('contactForm').addEventListener('submit', function(e) {
  e.preventDefault();
  const statusEl = document.getElementById('formStatus');
  statusEl.textContent = 'Sending…';
  setTimeout(() => {
    statusEl.textContent = 'Thank you! Your message has been sent.';
    this.reset();
  }, 1500);
});

// Smooth scroll for nav links
document.querySelectorAll('.nav-link').forEach(link => {
  link.addEventListener('click', function(e) {
    if (this.hash !== '') {
      e.preventDefault();
      const hash = this.hash;
      document.querySelector(hash).scrollIntoView({ behavior: 'smooth' });
    }
  });
});
