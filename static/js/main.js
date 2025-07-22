// Animate form elements on focus
document.querySelectorAll('.form-control, .form-select').forEach(el => {
  el.addEventListener('focus', () => {
    el.parentElement.classList.add('focused');
  });
  
  el.addEventListener('blur', () => {
    el.parentElement.classList.remove('focused');
  });
});

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    e.preventDefault();
    document.querySelector(this.getAttribute('href')).scrollIntoView({
      behavior: 'smooth'
    });
  });
});