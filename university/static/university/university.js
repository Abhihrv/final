document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.u-nav').forEach(navlink => {
        navlink.onclick = (event) => {
            event.stopPropagation();
            umenu = document.querySelector('.u-menu');
            if (navlink.classList.value.includes('active') && umenu.classList.value.includes('open-drawer')) {
                closeDrawer(umenu);
            } else {
                openDrawer(umenu);
            }
            removeAllActive ('.nav-link');
            navlink.classList.add('active');
            document.querySelector('.tab-content').innerHTML = `<h1>${navlink.getAttribute('data-section')} </h1>`
        };
    });

    document.querySelector('.u-menu').onclick = (event) => {
        event.stopPropagation();
    }
})

/* Make all the elements inactive */
function removeAllActive (className) {
    document.querySelectorAll(className).forEach(element => element.classList.remove('active'))
}

/* Close navigation menu */
function closeDrawer(element) {
    element.classList.remove('open-drawer');
    element.classList.add('close-drawer');
    document.querySelector('.body').style.opacity = 1;
    document.querySelector('.body').setAttribute('style','filter: blur(0px)') ;
}

/* Open navigation menu */
function openDrawer(element) {
    element.classList.remove('close-drawer');
    element.classList.add('open-drawer');
    document.querySelector('.body').style.opacity = 0.2;
    document.querySelector('.body').setAttribute('style','filter: blur(2px)') ;
}

/* Close navigation menu if user clicks outside it */
window.addEventListener('click', function(event) {
    umenu = document.querySelector('.u-menu');
    closeDrawer(umenu);
});