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

    nuevo_cliente_json = schemas.CrearCliente.model_validate(nuevo_cliente, from_attributes=True)

    nuevo_cliente_dict = nuevo_cliente_json.model_dump()

    return jsonify(nuevo_cliente_dict)


def obtener_cliente(id: int):
    db_session = db.session
    cliente = crud.get_cliente_por_id(db_session, id)
    return cliente


def actualizar_cliente(id: int):
    # se trae la data de la request y se valida con el schema
    data = schemas.ActualizarCliente(**request.json)
    # sesion de la db
    db_session = db.session
    # actualiza el cliente en la db
    cliente_actualizado = crud.actualizar_cliente(db_session, id, data.model_dump(exclude_defaults=True))
    # convierte modelo sqlalchemy en pydantic schema
    cliente_json = schemas.GetCliente.model_validate(cliente_actualizado, from_attributes=True)
    # convierte la instancia de pydantic en diccionario
    cliente_dict = cliente_json.model_dump()

    # retorna el diccionario que se creo en cliente_dict en formato JSON
    return jsonify(cliente_dict)


def eliminar_cliente(id: int):
    db_session = db.session
    delete_cliente = crud.eliminar_cliente(db_session, id)

    return 'cliente eliminado con éxito'
