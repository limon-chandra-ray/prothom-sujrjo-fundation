var nav_profile = document.getElementById('nav-profile');
var nav_profile_detail = document.getElementById('nav-profile-detail');

nav_profile.addEventListener('click',()=>{
    nav_profile_detail.classList.toggle("hidden")
})