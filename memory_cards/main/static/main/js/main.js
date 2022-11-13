const footerYearSpan = document.querySelector('.y')
const year = new Date().getFullYear();
footerYearSpan.textContent = `${year}`

const burgerBtn = document.querySelector('.burger-btn')
const navMobile = document.querySelector('.nav-mobile')



burgerBtn.addEventListener('click', )


//CARDS
const search = document.querySelector('.search-cards')

const li = document.querySelectorAll('.card-item')

const searchDrinks = (e) =>{
    const text = e.target.value.toLowerCase();

    li.forEach(el => {
        if (el.textContent.toLowerCase().indexOf(text) !== -1){
            el.style.display = 'block'
        } else {
            el.style.display = 'none'
        }
    })
}

search.addEventListener('keyup', searchDrinks)