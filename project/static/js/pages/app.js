var swiper = new Swiper(".mySwiper", {
    slidesPerView: 1,
    spaceBetween: 1, 
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
  });


// Make navbar responsive 

burgerMenu = document.querySelector('#burger-menu')

burgerMenu.addEventListener('click', () => {
  document.querySelectorAll('header .container nav').forEach((nav) => {
    nav.classList.toggle('show') 
  })
})