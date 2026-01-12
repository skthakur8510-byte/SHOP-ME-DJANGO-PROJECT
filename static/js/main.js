document.addEventListener("DOMContentLoaded", () => {

    const hamburger = document.querySelector(".hamburger");
    const navLinks = document.querySelector(".nav_link");
    const closeBtn = document.querySelector(".close_btn");

    // Open slider
    hamburger.addEventListener("click", () => {
        navLinks.classList.add("active");
        document.body.classList.add("menu_open");
    });

    // Close slider
    closeBtn.addEventListener("click", () => {
        navLinks.classList.remove("active");
        document.body.classList.remove("menu_open");
    });


    document.querySelectorAll(".nav_link > li").forEach(item => {
        item.addEventListener("click", () => {
            item.classList.toggle("active");
        });
    });
    
});
