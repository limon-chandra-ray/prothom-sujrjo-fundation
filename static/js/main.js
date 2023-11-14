$('.carousel1').owlCarousel({
    loop:true,
    // margin:10,
    nav:true,
    dots:false,
    autoplay:true,
    animateOut:true,
    animateIn:true,
    responsive:{
        0:{
            items:1
        },
        600:{
            items:1
        },
        1000:{
            items:1
        }
    }
})
$('.carousel2').owlCarousel({
    loop:true,
    // margin:10,
    nav:true,
    dots:false,
    autoplay:false,
    responsive:{
        0:{
            items:1
        },
        600:{
            items:1
        },
        1000:{
            items:1
        }
    }
})
$('.carousel3').owlCarousel({
    loop:true,
    margin:10,
    nav:true,
    dots:true,
    autoplay:true,
    responsive:{
        0:{
            items:1
        },
        600:{
            items:1
        },
        1000:{
            items:3
        }
    }
})
//navbar show-hide
 // JavaScript code to handle the dropdown functionality 
 const dropdownButton = document.getElementById("dropdownButton");
 const dropdownMenu = document.getElementById("dropdownMenu");

 dropdownButton.addEventListener("click", function() {
     dropdownMenu.classList.toggle("hidden");
 });

 // Close the dropdown menu when clicking outside of it
 window.addEventListener("click", function(event) {
     if (!dropdownButton.contains(event.target) && !dropdownMenu.contains(event.target)) {
         dropdownMenu.classList.add("hidden");
     }
 });
// Sponser page js

function openLightbox(number) {
    const question = document.getElementById(`question${number}`);
    const answer = document.getElementById(`answer${number}`);
    const sign = document.getElementById(`sign${number}`);
    answer.classList.toggle("hidden");
    question.classList.remove("text-[#54595F]");
    question.classList.add("text-[#FFCB05]");
    sign.innerHTML = '<i class="fas fa-minus"></i>';
    window.addEventListener("click", function(event) {
        if (!question.contains(event.target) && !answer.contains(event.target)) {
            answer.classList.add("hidden");
            question.classList.remove("text-[#FFCB05]");
            question.classList.add("text-[#54595F]");
            sign.innerHTML = '<i class="fas fa-plus"></i>';
        }
    });
}