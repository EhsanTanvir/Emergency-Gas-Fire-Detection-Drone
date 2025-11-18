const form = document.getElementById('contactForm');
if (form) {
  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const data = new FormData(form);
    const status = document.getElementById('formStatus');
    status.textContent = 'Sending...';
    try {
      const res = await fetch('/contact', { method: 'POST', body: data });
      const json = await res.json();
      if (json.success) {
        status.textContent = 'Message sent — thank you!';
        form.reset();
      } else {
        status.textContent = 'Error: ' + (json.error || 'unknown');
      }
    } catch (err) {
      status.textContent = 'Network error';
    }
  });
}
