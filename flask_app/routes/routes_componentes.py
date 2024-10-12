from flask import request, jsonify
from flask_app.models.session import db
from flask_app.controllers import crud
from flask_app.models import schemas


# Rutas para Componentes
def obtener_componentes():
    db_session = db.session
    componentes = crud.get_componentes(db_session)

    return componentes


def agregar_componente():
    data = schemas.CrearComponente(**request.json)
    db_session = db.session
    nuevo_componente = crud.crear_componente(db_session, data.nombre, data.precio, data.stock, data.categoria)
    nuevo_componente_json = schemas.CrearComponente.model_validate(nuevo_componente, from_attributes=True)
    nuevo_componente_dict = nuevo_componente_json.model_dump()

    return jsonify(nuevo_componente_dict)


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