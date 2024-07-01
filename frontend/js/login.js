document.addEventListener("DOMContentLoaded", function() {
    const userIconLink = document.querySelector("#area-users a");
    const loginContainer = document.getElementById("loginContainer");

    userIconLink.addEventListener("click", function(event) {
        event.preventDefault();
        
        // Oculta el formulario si ya está visible
        if (loginContainer.innerHTML.trim().length > 0) {
            loginContainer.innerHTML = "";
        } else {
            // Crea y agrega el formulario de inicio de sesión al contenedor
            const loginForm = document.createElement("form");
            loginForm.id = "loginForm";
            loginForm.innerHTML = `
                <label for="usernameLogin">Usuario:</label>
                <input type="text" id="usernameLogin" name="usernameLogin" required><br><br>
                <label for="passwordLogin">Contraseña:</label>
                <input type="password" id="passwordLogin" name="passwordLogin" required><br><br>
                <button type="submit">Iniciar Sesión</button>
            `;
            
            loginContainer.appendChild(loginForm);
        }
    });

    // Resto de tu código para el inicio de sesión...
});
