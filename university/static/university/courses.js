function loadDegree(degree_id){
    fetch(`/courses/degree/${degree_id}`)
        .then(response => response.json())
        .then(data => {
            showDegree(data)
        }
    )
}

function showDegree(data) {
    degreedetails = `<div class="container section-home degree-details">
        <div class="row">
            <div class="col-sm-3 degree-details-center">
                <div class="card mx-auto degree-card">
                    <div class="card-body">
                        <h6 class="card-title">${data.degreeCode}<br>${data.degree}</h6>
                        <p class="card-text">Credits Achieved: ${data.credits_achieved}</p>
                        <p class="card-text">Status: ${data.status}</p>
                        <p class="card-text">CGPA: ${data.cgpa}</p>
                    </div>
                </a>
            </div>
        </div>
    </div>`;
    document.querySelector('.degree-modal').innerHTML = degreedetails;
    document.querySelector('.degree-home').style.filter = 'blur(2px)';
    document.querySelector('.degree-home').onclick = closeDegree;
}

function closeDegree() {
    document.querySelector('.degree-modal').innerHTML = "";
    document.querySelector('.degree-home').style.filter = 'blur(0px)';
}