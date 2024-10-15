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


def obtener_componente(id):
    db_session = db.session
    componente = crud.get_componente_por_id(db_session, id)

    return componente


def actualizar_componente(id):
    data = schemas.ActualizarComponente(**request.json)
    db_session = db.session
    comp_actualizado = crud.actualizar_componente(db_session, id, data.model_dump(exclude_defaults=True))
    comp_validate = schemas.ActualizarComponente.model_validate(comp_actualizado)
    result = comp_validate.model_dump()

    return result


def eliminar_componente(id):
    db_session = db.session
    comp_eliminado = crud.eliminar_componente(db_session, id)

    return 'componente eliminado con éxito'
