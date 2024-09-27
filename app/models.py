from datetime import datetime
from . import db
from sqlalchemy.orm import Mapped
from sqlalchemy import Column, Integer, String
from decimal import Decimal
from enum import Enum


class Cliente(db.Model):
    __tablename__ = 'Clientes'
    id: Mapped[int] = Column(Integer, primary_key=True)
    nombre: Mapped[str] = Column(String(100), nullable=False)
    correo: Mapped[str] = Column(String(100), nullable=False, unique=True)
    clave: Mapped[str] = Column(String(255), nullable=False)
    telefono: Mapped[str] = Column(String(20))
    direccion: Mapped[str] = Column(String(255))
    fecha_creacion: Mapped[datetime] = Column(db.DateTime, default=datetime.utcnow)
    ultima_actividad: Mapped[datetime] = Column(db.DateTime, nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'correo': self.correo,
            'clave': self.clave,
            'telefono': self.telefono,
            'direccion': self.direccion,
            'fecha_creacion': self.fecha_creacion,
            'ultima_actividad': self.ultima_actividad
        }


class Componente(db.Model):
    __tablename__ = 'Componentes'
    id: Mapped[int] = Column(Integer, primary_key=True)
    nombre: Mapped[str] = Column(String(100), nullable=False)
    descripcion: Mapped[str] = Column(db.Text)
    precio: Mapped[Decimal] = Column(db.Numeric(10, 2), nullable=False)
    stock: Mapped[int] = Column(Integer, nullable=False)
    categoria: Mapped[str] = Column(String(50))
    fecha_creacion: Mapped[datetime] = Column(db.DateTime, default=datetime.utcnow)
    fecha_actualizacion: Mapped[datetime] = Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'precio': self.precio,
            'stock': self.stock,
            'categoria': self.categoria,
            'fecha_creacion': self.fecha_creacion,
            'fecha_actualizacion': self.fecha_actualizacion
        }


class Status(Enum):
    ABIERTO = 'abierto'
    CERRADO = 'cerrado'
    VACIO = 'vacio'


class Carrito(db.Model):
    __tablename__ = 'Carritos'
    id: Mapped[int] = Column(Integer, primary_key=True)
    cliente_id: Mapped[int] = Column(Integer, db.ForeignKey('Clientes.id'), nullable=False)
    fecha_creacion: Mapped[datetime] = Column(db.DateTime, default=datetime.utcnow)
    fecha_actualizacion: Mapped[datetime] = Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    estado: Mapped[Status] = Column(db.Enum(Status), default=Status.ABIERTO)
    cliente = db.relationship('Cliente', backref=db.backref('carritos', lazy=True))

    def to_dict(self):
        return {
            'id': self.id,
            'cliente_id': self.cliente_id,
            'fecha_creacion': self.fecha_creacion,
            'fecha_actualizacion': self.fecha_actualizacion,
            'estado': self.estado
        }


class CarritoItem(db.Model):
    __tablename__ = 'Carrito_Items'
    id: Mapped[int] = Column(Integer, primary_key=True)
    carrito_id: Mapped[int] = Column(Integer, db.ForeignKey('Carritos.id'), nullable=False)
    componente_id: Mapped[int] = Column(Integer, db.ForeignKey('Componentes.id'), nullable=False)
    cantidad: Mapped[int] = Column(Integer, nullable=False)
    fecha_agregado: Mapped[datetime] = Column(db.DateTime, default=datetime.utcnow)
    carrito = db.relationship('Carrito', backref=db.backref('items', lazy=True))
    componente = db.relationship('Componente', backref=db.backref('carrito_items', lazy=True))

    def to_dict(self):
        return {
            'id': self.id,
            'carrito_id': self.carrito_id,
            'componente_id': self.componente_id,
            'cantidad': self.cantidad,
            'fecha_agregado': self.fecha_agregado
        }
