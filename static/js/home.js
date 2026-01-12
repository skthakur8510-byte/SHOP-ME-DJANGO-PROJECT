let slideIndex = 0;
        const slides = document.querySelectorAll(".slide");
        const next = document.querySelector(".next");
        const prev = document.querySelector(".prev");

        function showSlide(index) {
            slides.forEach((slide, i) => {
                slide.style.display = (i === index) ? "block" : "none";
            });
        }

        function nextSlide() {
            slideIndex = (slideIndex + 1) % slides.length;
            showSlide(slideIndex);
        }

        function prevSlide() {
            slideIndex = (slideIndex - 1 + slides.length) % slides.length;
            showSlide(slideIndex);
        }

        next.addEventListener("click", nextSlide);
        prev.addEventListener("click", prevSlide);

        setInterval(nextSlide, 2000);
        showSlide(slideIndex);



        const ham = document.querySelector(".hamburger");
        const nav = document.querySelector(".nav");
    
        ham.addEventListener("click", () => {
            nav.classList.toggle("mobile_active");
        });