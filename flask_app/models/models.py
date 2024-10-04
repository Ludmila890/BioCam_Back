from datetime import datetime
from flask_app.models.session import db
from sqlalchemy.orm import Mapped
from sqlalchemy import Column, Integer, String
from decimal import Decimal
from enum import Enum


class Cliente(db.Model):
    __tablename__ = 'Clientes'
    id: Mapped[int] = Column(Integer, primary_key=True)
    nombre: Mapped[str] = Column(String(100))
    email: Mapped[str] = Column(String(100), unique=True)
    clave: Mapped[str] = Column(String(255))
    telefono: Mapped[str] = Column(String(20))
    direccion: Mapped[str] = Column(String(255))
    fecha_creacion: Mapped[datetime] = Column(db.DateTime, default=datetime.utcnow)
    ultima_actividad: Mapped[datetime] = Column(db.DateTime)


class Componente(db.Model):
    __tablename__ = 'Componentes'
    id: Mapped[int] = Column(Integer, primary_key=True)
    nombre: Mapped[str] = Column(String(100))
    descripcion: Mapped[str] = Column(db.Text)
    precio: Mapped[Decimal] = Column(db.Numeric(10, 2))
    stock: Mapped[int] = Column(Integer)
    categoria: Mapped[str] = Column(String(50))
    fecha_creacion: Mapped[datetime] = Column(db.DateTime, default=datetime.utcnow)
    fecha_actualizacion: Mapped[datetime] = Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Estado(Enum):
    ABIERTO = 'abierto'
    CERRADO = 'cerrado'
    VACIO = 'vacio'


class Carrito(db.Model):
    __tablename__ = 'Carritos'
    id: Mapped[int] = Column(Integer, primary_key=True)
    cliente_id: Mapped[int] = Column(Integer, db.ForeignKey('Clientes.id'))
    fecha_creacion: Mapped[datetime] = Column(db.DateTime, default=datetime.utcnow)
    fecha_actualizacion: Mapped[datetime] = Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    estado: Mapped[Estado] = Column(db.Enum(Estado), default=Estado.ABIERTO)
    cliente = db.relationship('Cliente', backref=db.backref('carritos', lazy=True))


class CarritoItem(db.Model):
    __tablename__ = 'Carrito_Items'
    id: Mapped[int] = Column(Integer, primary_key=True)
    carrito_id: Mapped[int] = Column(Integer, db.ForeignKey('Carritos.id'))
    componente_id: Mapped[int] = Column(Integer, db.ForeignKey('Componentes.id'))
    cantidad: Mapped[int] = Column(Integer)
    fecha_agregado: Mapped[datetime] = Column(db.DateTime, default=datetime.utcnow)
    carrito = db.relationship('Carrito', backref=db.backref('items', lazy=True))
    componente = db.relationship('Componente', backref=db.backref('carrito_items', lazy=True))
