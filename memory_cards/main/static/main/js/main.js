// const q = document.querySelector('.question')
const response = document.querySelector('.response')
const btn = document.querySelector('.check')

function show_response (){
    response.style.display = "block";
   // response.classList.toggle("d-block")
}

btn.addEventListener('click', show_response )




$('.my-carousel').slick({
    infinite: true,
    slidesToShow: 2,
    slidesToScroll: 1,
    arrows: false,
    autoplay: true,
     arrows: true,

});