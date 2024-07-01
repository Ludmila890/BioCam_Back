function validarFormulario() {
    const nombre = document.getElementById('nombre').value;
    const email = document.getElementById('email').value;
    const motivo = document.getElementById('motivo').value;
    const mensaje = document.getElementById('mensaje').value;
    
    if (nombre.trim() === '' || email.trim() === '' || motivo.trim() === '' || mensaje.trim() === '') {
        alert('Todos los campos son obligatorios');
        return false;
    }
    
    return true;
}
