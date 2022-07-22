document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.u-nav').forEach(navlink => {
        navlink.onclick = (event) => {
            event.stopPropagation();
            umenu = document.querySelector('.u-menu');
            if (navlink.classList.value.includes('active') && umenu.classList.value.includes('open-drawer')) {
                closeDrawer(umenu);
            } else {
                openDrawer(umenu);
                removeAllActive ('.nav-link');
                navlink.classList.add('active');
            }
            clearUmenu(umenu);
            showLinks(umenu, navlink.getAttribute('data-section'));
        
        };
    });
    document.querySelector('.u-menu').onclick = (event) => {
        event.stopPropagation();
    }
    
    if(window.innerWidth <= 500) {
        document.querySelector('.u-bar-mobile-toggler').onclick = () => {
            document.querySelectorAll('.u-nav-desktop').forEach(element => {
                if(element.style.display == 'none') {
                    element.style.display = 'block'
                }
                else {
                    element.style.display = 'none'
                }
            })
        }
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
    removeAllActive ('.nav-link');
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

function clearUmenu(umenu) {
    umenu.querySelectorAll('.umenu-row').forEach(element => element.style.display = 'none')
}

function showLinks(umenu, linkId) {
    umenu.querySelector(`#${linkId}`).style.display = 'block'
}