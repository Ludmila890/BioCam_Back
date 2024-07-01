import mysql.connector

def obtener_conexion():
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # Deja la contraseña en blanco si no tienes una
        database="biocam_grupo_7"
    )
    return conexion

def obtener_clientes():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Clientes")
    resultados = cursor.fetchall()
    cursor.close()
    conexion.close()
    return resultados
