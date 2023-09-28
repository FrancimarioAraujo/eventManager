document.getElementById('formRegister').addEventListener('submit', function(event) {
    event.preventDefault();

    const formData = new FormData(this);
    const formDataJSON = {};

    formData.forEach((value, key) => {
        formDataJSON[key] = value;

    });

    //console.log('Dados a serem enviados:', JSON.stringify(formDataJSON));

    // Envia os dados como JSON usando uma requisição AJAX
    fetch(this.action, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
        },
        body: JSON.stringify(formDataJSON)
    })
    .then(response => response.json())  
    .then(data => {
        console.log('Resposta do servidor:', data);
        if (data.success) {
            window.location.href = "/login/";
        }
    })
})