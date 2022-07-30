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
    document.querySelector('.u-menu-mobile').onclick = (event) => {
        event.stopPropagation();
    }
    document.querySelector('.u-menu-link-mobile').onclick = (event) => {
        event.stopPropagation();
        umenuMobile = document.querySelector('.u-menu-mobile');
        if (umenuMobile.classList.value.includes('open-mobile-drawer')) {
            closeMobileDrawer(umenuMobile);
        } else {
            openMobileDrawer(umenuMobile);
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

/* Close navigation menu on mobile */
function closeMobileDrawer(element) {
    element.classList.remove('open-mobile-drawer');
    element.classList.add('close-mobile-drawer');
    document.querySelector('.body').style.opacity = 1;
    document.querySelector('.body').setAttribute('style','filter: blur(0px)') ;
}

/* Open navigation menu on mobile */
function openMobileDrawer(element) {
    element.classList.remove('close-mobile-drawer');
    element.classList.add('open-mobile-drawer');
    document.querySelector('.body').style.opacity = 0.2;
    document.querySelector('.body').setAttribute('style','filter: blur(2px)') ;
}

/* Close navigation menu if user clicks outside it */
window.addEventListener('click', function(event) {
    closeDrawer(document.querySelector('.u-menu'));
    closeMobileDrawer(document.querySelector('.u-menu-mobile'));
});

function clearUmenu(umenu) {
    umenu.querySelectorAll('.umenu-row').forEach(element => element.style.display = 'none')
}

function showLinks(umenu, linkId) {
    umenu.querySelector(`#${linkId}`).style.display = 'block'
}