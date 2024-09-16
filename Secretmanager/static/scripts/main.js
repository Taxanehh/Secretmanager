// static/scripts/main.js

// Simple script to convert the navbar to a hamburger menu
// in case the user is on phone, tablet or any smaller screen
document.addEventListener('DOMContentLoaded', () => {
    const menuToggle = document.getElementById('menu-toggle');
    const navLinks = document.querySelector('.nav-links');

    menuToggle.addEventListener('click', () => {
        navLinks.classList.toggle('active');
    });
});