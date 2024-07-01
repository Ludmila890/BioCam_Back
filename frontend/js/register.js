document.addEventListener("DOMContentLoaded", function() {
    const registerLink = document.getElementById("registerLink");
    const registerContainer = document.getElementById("registerContainer");

    registerLink.addEventListener("click", function(event) {
        event.preventDefault();
        registerContainer.style.display = "block";
    });

    const registerForm = document.createElement("form");
    registerForm.id = "registerForm";
    registerForm.innerHTML = `
        <p>
            <label for="usernameRegister">Usuario:</label>
            <input type="text" id="usernameRegister" name="usernameRegister" required>
        </p>
        <p>
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>
        </p>
        <p>
            <label for="passwordRegister">Contraseña:</label>
            <input type="password" id="passwordRegister" name="passwordRegister" required>
        </p>
        <p>
            <label for="termsCheckbox">
                <input type="checkbox" id="termsCheckbox" name="termsCheckbox" required>
                Acepto los términos y condiciones
            </label>
        </p>
        <p class="sign-in-btn">
            <button type="submit" class="button-primary">Registrarse</button>
        </p>
    `;
    registerContainer.appendChild(registerForm);

    registerForm.addEventListener("submit", function(event) {
        event.preventDefault();

        const username = document.getElementById("usernameRegister").value;
        const email = document.getElementById("email").value;
        const password = document.getElementById("passwordRegister").value;

        // Verificar si el checkbox está marcado
        const termsCheckbox = document.getElementById("termsCheckbox");
        if (!termsCheckbox.checked) {
            alert("Debes aceptar los términos y condiciones para registrarte.");
            return;
        }

        const formData = {
            username: username,
            email: email,
            password: password
        };

        // Simulando una respuesta de API
        setTimeout(() => {
            console.log("Usuario registrado correctamente:", formData);
            alert("Usuario registrado correctamente");
            registerForm.reset();
            registerContainer.style.display = "none"; // Ocultar el formulario de registro después del registro
        }, 1000);

        /*
        // Código para enviar datos a una API real
        fetch("URL_DEL_API", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(formData)
        })
        .then(response => {
            if (!response.ok) {
                throw new Error("Ocurrió un error al registrar el usuario");
            }
            return response.json();
        })
        .then(data => {
            console.log("Usuario registrado correctamente:", data);
            registerForm.reset();
            registerContainer.style.display = "none"; // Ocultar el formulario de registro después del registro
        })
        .catch(error => {
            console.error("Error:", error);
        });
        */
    });
});
