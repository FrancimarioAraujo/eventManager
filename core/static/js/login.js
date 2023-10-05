document.getElementById("formLogin").addEventListener("submit", function (event) {
    event.preventDefault();

    const formData = new FormData(this);

    const formDataJSON = {};
    formData.forEach((value, key) => {
      formDataJSON[key] = value;
    });

    console.log(formDataJSON)
    fetch(this.action, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value,
      },
      body: JSON.stringify(formDataJSON),
    })
    .then((response) => response.json())
    .then((data) => {
        console.log("Resposta do servidor:", data);
        if (data.success) {
          window.location.href = "/home/";
        } else if (data.error) {
          const errorMessageElement = document.getElementById("error-message");
          errorMessageElement.textContent = "<p> Credenciais inválidas </p>"; 
          errorMessageElement.style.display = "block";
        }
    });
});
