from flask import request, jsonify
from flask_app.models.session import db
from flask_app.controllers import crud
from flask_app.models import schemas


def obtener_carritos():
    pass


def agregar_carrito():
    pass

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
