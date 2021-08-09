let open = document.querySelector('#open')
let close = document.querySelector('#close')
let mobile = document.querySelector('.mobile-menu')
open.addEventListener('click', function() {
    // document.querySelector('.mobile-menu').style.display = 'block'
    document.querySelector('.mobile-menu').style.left = '0px'
    document.querySelector('#close').style.display = 'block'
    document.querySelector('#open').style.display = 'none'

})
close.addEventListener('click', function() {
    // document.querySelector('.mobile-menu').style.display = 'none'

    document.querySelector('.mobile-menu').style.left = '-1600px'
    document.querySelector('#close').style.display = 'none'
    document.querySelector('#open').style.display = 'block'

})