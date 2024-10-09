from flask import request, jsonify
from flask_app.models.session import db
from flask_app.controllers import crud
from flask_app.models import schemas


# Rutas para Clientes
def obtener_clientes():
    db_session = db.session
    clientes = crud.get_clientes(db_session)

    return clientes


def agregar_cliente():
    data = schemas.CrearCliente(**request.json)
    db_session = db.session
    nuevo_cliente = crud.crear_cliente(db_session, data.nombre, data.email, data.clave)


def obtener_cliente(id: int):
    db_session = db.session
    cliente = crud.get_cliente_por_id(db_session, id)
    return cliente


def actualizar_cliente(id: int):
    data = schemas.ActualizarCliente(**request.json)
    db_session = db.session
    cliente_actualizado = crud.actualizar_cliente(db_session, id, data.model_dump(exclude_defaults=True))


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
