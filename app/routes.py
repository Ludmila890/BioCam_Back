

from flask import Flask, render_template
from app.conexion_db import obtener_clientes

app = Flask(__name__)

@app.route('/')
def index():
    clientes = obtener_clientes()
    return render_template('index.html', clientes=clientes)
