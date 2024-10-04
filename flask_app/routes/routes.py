from flask import jsonify, request, send_from_directory
# from main import app
from flask_app.models.session import db
from models.models import Cliente, Componente, Carrito
from sqlalchemy.exc import IntegrityError
from flask_app.controllers import crud
from sqlalchemy.orm import Session
#
#
# @app.route('/login')
# def login():
#     return send_from_directory('../frontend/sitio', 'login.html')
#
#
# @app.route('/css/<path:filename>')
# def css(filename):
#     return send_from_directory('../frontend/css', filename)
#
#
# @app.route('/img/<path:filename>')
# def img(filename):
#     return send_from_directory('../frontend/img', filename)
#
#
# @app.route('/js/<path:filename>')
# def js(filename):
#     return send_from_directory('../frontend/js', filename)
#
#
# # Rutas para Clientes
# #@app.route('/api/clientes', methods=['GET'])
def obtener_clientes():
    _request = request
    print(request)
    db_session = db.session
    clientes = crud.get_clientes(db_session)

    return clientes
#
#
# @app.route('/api/clientes', methods=['POST'])
# def agregar_cliente():
#     data = request.get_json()
#     if not data:
#         return jsonify({'message': 'No input data provided'}), 400
#
#     required_fields = ['nombre', 'correo', 'clave']
#     for field in required_fields:
#         if field not in data:
#             return jsonify({'message': f'Field {field} is missing'}), 400
#
#     nuevo_cliente = Cliente(
#         nombre=data['nombre'],
#         correo=data['correo'],
#         clave=data['clave'],
#         telefono=data.get('telefono'),
#         direccion=data.get('direccion')
#     )
#
#     try:
#         db.session.add(nuevo_cliente)
#         db.session.commit()
#         return jsonify({'message': 'Cliente agregado con éxito!'}), 201
#     except IntegrityError:
#         db.session.rollback()
#         return jsonify({'message': 'Error: El correo ya existe'}), 400
#     except Exception as e:
#         db.session.rollback()
#         return jsonify({'message': f'Error al agregar cliente: {str(e)}'}), 500
#
#
# @app.route('/api/clientes/<int:id>', methods=['GET'])
# def obtener_cliente(id):
#     cliente = Cliente.query.get_or_404(id)
#     return jsonify(cliente.to_dict())
#
#
# @app.route('/api/clientes/<int:id>', methods=['PUT'])
# def actualizar_cliente(id):
#     cliente = Cliente.query.get(id)
#     if cliente is None:
#         return jsonify({'mensaje': 'Cliente no encontrado'}), 404
#
#     datos = request.get_json()
#     nuevo_correo = datos.get('correo')
#
#     if Cliente.query.filter(Cliente.correo == nuevo_correo, Cliente.id != id).first():
#         return jsonify({'mensaje': 'El correo ya está en uso por otro cliente'}), 400
#
#     cliente.nombre = datos.get('nombre', cliente.nombre)
#     cliente.correo = datos.get('correo', cliente.correo)
#     cliente.clave = datos.get('clave', cliente.clave)
#     cliente.telefono = datos.get('telefono', cliente.telefono)
#     cliente.direccion = datos.get('direccion', cliente.direccion)
#
#     try:
#         db.session.commit()
#         return jsonify({'mensaje': 'Cliente actualizado correctamente'})
#     except IntegrityError as e:
#         db.session.rollback()
#         return jsonify({'mensaje': 'Error de integridad: ' + str(e)}), 500
#
#
# @app.route('/api/clientes/<int:id>', methods=['DELETE'])
# def eliminar_cliente(id):
#     cliente = Cliente.query.get(id)
#     if cliente is None:
#         return jsonify({'mensaje': 'Cliente no encontrado'}), 404
#
#     db.session.delete(cliente)
#     db.session.commit()
#     return jsonify({'mensaje': 'Cliente eliminado correctamente'})
#
#
# # Rutas para Componentes
# @app.route('/api/componentes', methods=['GET'])
# def obtener_componentes():
#     componentes = Componente.query.all()
#     return jsonify([componente.to_dict() for componente in componentes])
#
#
# @app.route('/api/componentes', methods=['POST'])
# def agregar_componente():
#     data = request.get_json()
#     nuevo_componente = Componente(
#         nombre=data['nombre'],
#         descripcion=data.get('descripcion'),
#         precio=data['precio'],
#         stock=data['stock'],
#         categoria=data.get('categoria')
#     )
#     db.session.add(nuevo_componente)
#     db.session.commit()
#     return jsonify({'message': 'Componente agregado con éxito!'}), 201
#
#
# @app.route('/api/componentes/<int:id>', methods=['GET'])
# def obtener_componente(id):
#     componente = Componente.query.get_or_404(id)
#     return jsonify(componente.to_dict())
#
#
# @app.route('/api/componentes/<int:id>', methods=['PUT'])
# def actualizar_componente(id):
#     componente = Componente.query.get(id)
#     if componente is None:
#         return jsonify({'mensaje': 'Componente no encontrado'}), 404
#
#     datos = request.get_json()
#     componente.nombre = datos.get('nombre', componente.nombre)
#     componente.descripcion = datos.get('descripcion', componente.descripcion)
#     componente.precio = datos.get('precio', componente.precio)
#     componente.stock = datos.get('stock', componente.stock)
#     componente.categoria = datos.get('categoria', componente.categoria)
#
#     try:
#         db.session.commit()
#         return jsonify({'mensaje': 'Componente actualizado correctamente'})
#     except IntegrityError as e:
#         db.session.rollback()
#         return jsonify({'mensaje': 'Error de integridad: ' + str(e)}), 500
#
#
# @app.route('/api/componentes/<int:id>', methods=['DELETE'])
# def eliminar_componente(id):
#     componente = Componente.query.get(id)
#     if componente is None:
#         return jsonify({'mensaje': 'Componente no encontrado'}), 404
#
#     db.session.delete(componente)
#     db.session.commit()
#     return jsonify({'mensaje': 'Componente eliminado correctamente'})
#
#
# # Rutas para Carritos
# @app.route('/api/carritos', methods=['GET'])
# def obtener_carritos():
#     carritos = Carrito.query.all()
#     return jsonify([carrito.to_dict() for carrito in carritos])
#
#
# @app.route('/api/carritos', methods=['POST'])
# def agregar_carrito():
#     data = request.get_json()
#     nuevo_carrito = Carrito(
#         cliente_id=data['cliente_id']
#     )
#     db.session.add(nuevo_carrito)
#     db.session.commit()
#     return jsonify({'message': 'Carrito agregado con éxito!'}), 201
#
#
# @app.route('/api/carritos/<int:id>', methods=['GET'])
# def obtener_carrito(id):
#     carrito = Carrito.query.get_or_404(id)
#     return jsonify(carrito.to_dict())
#
#
# @app.route('/api/carritos/<int:id>', methods=['PUT'])
# def actualizar_carrito(id):
#     carrito = Carrito.query.get(id)
#     if carrito is None:
#         return jsonify({'mensaje': 'Carrito no encontrado'}), 404
#
#     datos = request.get_json()
#     carrito.cliente_id = datos.get('cliente_id', carrito.cliente_id)
#     carrito.estado = datos.get('estado', carrito.estado)
#
#     try:
#         db.session.commit()
#         return jsonify({'mensaje': 'Carrito actualizado correctamente'})
#     except IntegrityError as e:
#         db.session.rollback()
#         return jsonify({'mensaje': 'Error de integridad: ' + str(e)}), 500
#
#
# @app.route('/api/carritos/<int:id>', methods=['DELETE'])
# def eliminar_carrito(id):
#     carrito = Carrito.query.get(id)
#     if carrito is None:
#         return jsonify({'mensaje': 'Carrito no encontrado'}), 404
#
#     db.session.delete(carrito)
#     db.session.commit()
#     return jsonify({'mensaje': 'Carrito eliminado correctamente'})
