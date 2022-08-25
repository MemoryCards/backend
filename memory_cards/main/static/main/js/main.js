const q = document.querySelector('.question')
const r = document.querySelector('.response')
const btn = document.querySelector('.check')

function show_response (){
    r.style.display = "block";
}

btn.addEventListener('click', show_response )