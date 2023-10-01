document.getElementById("formRegister").addEventListener("submit", function (event) {
    event.preventDefault();

    const formData = new FormData(this);
    const formDataJSON = {};

    formData.forEach((value, key) => {
      formDataJSON[key] = value;
    });

    fetch(this.action, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]")
          .value,
      },
      body: JSON.stringify(formDataJSON),
    })
    .then((response) => response.json())
    .then((data) => {
        console.log("Resposta do servidor:", data);
        if (data.success) {
            function showSuccessMessage(message) {
                const successMessage = document.getElementById('success-message');
                successMessage.innerHTML = message;
                successMessage.classList.remove('hidden');
                successMessage.classList.add('visible');
                

                document.getElementById('username').value = '';
                document.getElementById('fullname').value = '';
                document.getElementById('phone').value = '';
                document.getElementById('email').value = '';
                document.getElementById('password').value = '';

                setTimeout(function() {
                    successMessage.classList.remove('visible');
                    successMessage.classList.add('hidden'); // Remove a classe para tornar a mensagem invisível
                    setTimeout(function() {
                        window.location.href = "/login/";
                    }, 500); // Redireciona após a transição
                }, 3000); 
            }
            showSuccessMessage('Cadastro realizado com sucesso.');

        } else if (data.error) {
            displayErrors(data.error);
        }
      });

    function displayErrors(error) {
      // Clear previous error messages
      $(".error-message").text("");

      // Display error messages for each field
      for (const field in error) {
        const errorMessage = error[field];
        $(`#${field}-error`).text(errorMessage);
      }
    }
  });
