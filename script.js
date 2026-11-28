const menuToggle = document.getElementById("menuToggle");
const navLinks = document.getElementById("navLinks");

// Mobile navigation menu
menuToggle.addEventListener("click", function () {
    navLinks.classList.toggle("active");
});

// Close menu after selecting a navigation link
document.querySelectorAll(".nav-links a").forEach(function (link) {
    link.addEventListener("click", function () {
        navLinks.classList.remove("active");
    });
});

// Automatically update copyright year
document.getElementById("year").textContent = new Date().getFullYear();
