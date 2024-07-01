from flask import Flask, send_from_directory, request, jsonify
from app.conexion_db import obtener_clientes

app = Flask(__name__, static_folder='../frontend', static_url_path='', template_folder='../frontend')


@app.route('/')
def index():
    clientes = obtener_clientes()
    # return render_template('index.html', clientes=clientes)
    return send_from_directory(app.static_folder, 'index.html')


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    return jsonify({'message': 'Login exitoso'})

