from models import models
from sqlalchemy.orm import Session
from flask_app.utils.utils import hash_password
from flask_app.models.schemas import GetCliente


def get_clientes(session: Session, skip: int = 0, limit: int = 100) -> dict:
    clientes = session.query(models.Cliente).offset(skip).limit(limit).all()

    for cliente in clientes:
        cliente_serializado = GetCliente.model_validate(cliente).model_dump()

        return cliente_serializado


def get_cliente_por_email(session: Session, email: str) -> models.Cliente:
    result = session.query(models.Cliente).filter(models.Cliente.email == email).first()

    return result


def get_cliente_por_nombre(session: Session, nombre: str) -> models.Cliente:
    result = session.query(models.Cliente).filter(models.Cliente.nombre == nombre).first()

    return result


def get_cliente_por_id(session: Session, id: int) -> models.Cliente:
    result = session.query(models.Cliente).filter(models.Cliente.id == id).first()

    return result


def crear_cliente(session: Session, nombre: str, email: str, clave: str):
    password = hash_password(clave)
    nuevo_cliente = models.Cliente(nombre=nombre, email=email, clave=password)

    session.add(nuevo_cliente)
    session.commit()
    session.refresh(nuevo_cliente)

    return nuevo_cliente


def get_componentes(session: Session, skip: int = 0, limit: int = 100) -> list[type(models.Componente)]:
    result = session.query(models.Componente).offset(skip).limit(limit).all()

    return result


def get_componente_por_id(session: Session, id: int) -> models.Componente:
    result = session.query(models.Componente).filter(models.Componente.id == id).first()

    return result
