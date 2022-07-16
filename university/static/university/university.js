document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.nav-link').forEach(navlink => {
        navlink.onclick = () => {
            umenu = document.querySelector('.u-menu');
            if (navlink.classList.value.includes('active') && umenu.style.opacity > 0) {
                umenu.style.opacity = '0'
            } else {
                umenu.style.opacity = '0.7'
            }
            removeActive ('.nav-link');
            navlink.classList.add('active');
            document.querySelector('.tab-content').innerHTML = `<h1>${navlink.getAttribute('data-section')} </h1>`
        };
    });
})

function removeActive (className) {
    document.querySelectorAll(className).forEach(element => element.classList.remove('active'))
}