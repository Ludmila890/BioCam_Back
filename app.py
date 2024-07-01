from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# Inicializar la aplicación Flask
app = Flask(__name__)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/biocam_grupo_7'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar la base de datos
db = SQLAlchemy(app)

# Modelo de Cliente
class Cliente(db.Model):
    __tablename__ = 'Clientes'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), unique=True, nullable=False)
    clave = db.Column(db.String(255), nullable=False)
    telefono = db.Column(db.String(20))
    direccion = db.Column(db.String(255))
    fecha_creacion = db.Column(db.DateTime, default=db.func.current_timestamp())
    ultima_actividad = db.Column(db.DateTime, nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'correo': self.correo,
            'telefono': self.telefono,
            'direccion': self.direccion,
            'fecha_creacion': self.fecha_creacion,
            'ultima_actividad': self.ultima_actividad
        }

# Crear todas las tablas
with app.app_context():
    db.create_all()

# Ruta para obtener clientes
@app.route('/api/clientes', methods=['GET'])
def obtener_clientes():
    clientes = Cliente.query.all()
    return jsonify([cliente.to_dict() for cliente in clientes])

# Ruta para agregar un cliente
@app.route('/api/clientes', methods=['POST'])
def agregar_cliente():
    data = request.get_json()
    nuevo_cliente = Cliente(
        nombre=data['nombre'],
        correo=data['correo'],
        clave=data['clave'],
        telefono=data.get('telefono'),
        direccion=data.get('direccion')
    )
    db.session.add(nuevo_cliente)
    db.session.commit()
    return jsonify({'message': 'Cliente agregado con éxito!'}), 201

# Obtener un cliente por ID
@app.route('/api/clientes/<int:id>', methods=['GET'])
def obtener_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    return jsonify(cliente.to_dict())

# Actualizar un cliente 
@app.route('/api/clientes/<int:id>', methods=['PUT'])
def actualizar_cliente(id):
    data = request.get_json()
    cliente = Cliente.query.get_or_404(id)
    cliente.nombre = data.get('nombre', cliente.nombre)
    cliente.correo = data.get('correo', cliente.correo)
    cliente.clave = data.get('clave', cliente.clave)
    cliente.telefono = data.get('telefono', cliente.telefono)
    cliente.direccion = data.get('direccion', cliente.direccion)
    db.session.commit()
    return jsonify({'message': 'Cliente actualizado con éxito!'})

#Eliminar un cliente 
@app.route('/api/clientes/<int:id>', methods=['DELETE'])
def eliminar_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    db.session.delete(cliente)
    db.session.commit()
    return jsonify({'message': 'Cliente eliminado con éxito!'})

# Manejo de errores
@app.errorhandler(404)
def recurso_no_encontrado(e):
    return jsonify({'error': 'Recurso no encontrado'}), 404

@app.errorhandler(400)
def solicitud_incorrecta(e):
    return jsonify({'error': 'Solicitud incorrecta'}), 400

@app.errorhandler(500)
def error_interno_servidor(e):
    return jsonify({'error': 'Error interno del servidor'}), 500


# Iniciar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
