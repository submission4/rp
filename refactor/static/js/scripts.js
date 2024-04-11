const menuButton = document.getElementById('menuBtn')
const menuButtontwo = document.getElementById('menuBtntwo')
const closeBtn = document.getElementById('closeBtn')
const closeBtntwo = document.getElementById('closeBtntwo')

closeBtn.addEventListener('click', () => {
    const menu = document.getElementById('offcanvasMenu')
    menu.classList.toggle('open-menu')
    console.log('close clicked')
    })
menuButton.addEventListener('click', () => {
    const menu = document.getElementById('offcanvasMenu')
    menu.classList.toggle('open-menu')
    console.log('clicked')
    })
menuButtontwo.addEventListener('click', () => {
    const menu = document.getElementById('offcanvasMenutwo')
    menu.classList.toggle('open-menu-two')
    console.log('clicked two')
})

closeBtntwo.addEventListener('click', () => {
    const menu = document.getElementById('offcanvasMenutwo')
    menu.classList.toggle('open-menu-two')
    console.log('close clicked two')
})
