function showSuccessMessage(message) {
    const successMessage = document.getElementById('success-message');
    successMessage.innerHTML = message;
    successMessage.classList.remove('hidden');
    successMessage.classList.add('visible');
    

    setTimeout(function() {
        successMessage.classList.remove('visible');
        successMessage.classList.add('hidden'); 
        setTimeout(function() {
            window.location.href = "/eventos/myevents/";
        }, 500); 
    }, 3000); 
}

showSuccessMessage('Evento Criado com com sucesso.');