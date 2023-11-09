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
//  faq html
const question1 = document.getElementById("question1");
const answer1 = document.getElementById("answer1");
const sign1 = document.getElementById("sign1");
question1.addEventListener("click", function() {
    answer1.classList.toggle("hidden");
    question1.classList.remove("text-[#54595F]");
    question1.classList.add("text-black");
    sign1.innerHTML = '<i class="fas fa-minus"></i>';
    });
window.addEventListener("click", function(event) {
        if (!question1.contains(event.target) && !answer1.contains(event.target)) {
        answer1.classList.add("hidden");
        question1.classList.remove("text-black");
        question1.classList.add("text-[#54595F]");
        sign1.innerHTML = '<i class="fas fa-plus"></i>';
        }
    });
const question2 = document.getElementById("question2");
const answer2 = document.getElementById("answer2");
const sign2 = document.getElementById("sign2");
question2.addEventListener("click", function() {
    answer2.classList.toggle("hidden");
    question2.classList.remove("text-[#54595F]");
    question2.classList.add("text-black");
    sign2.innerHTML = '<i class="fas fa-minus"></i>';
    });
window.addEventListener("click", function(event) {
        if (!question2.contains(event.target) && !answer2.contains(event.target)) {
        answer2.classList.add("hidden");
        question2.classList.remove("text-black");
        question2.classList.add("text-[#54595F]");
        sign2.innerHTML = '<i class="fas fa-plus"></i>';
        }
    });