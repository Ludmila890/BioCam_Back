from datetime import datetime
from typing import List
from flask_app.models.session import db
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from decimal import Decimal
from enum import Enum


class Estado(Enum):
    ABIERTO = 'abierto'
    CERRADO = 'cerrado'
    VACIO = 'vacio'


class Cliente(db.Model):
    __tablename__ = 'clientes'
    id: Mapped[int] = Column('idcliente', Integer, primary_key=True, autoincrement=True)
    nombre: Mapped[str] = Column(String(100))
    email: Mapped[str] = Column(String(100), unique=True)
    clave: Mapped[str] = Column(String(255))
    telefono: Mapped[str] = Column(String(20))
    fecha_creacion: Mapped[datetime] = Column(db.DateTime, default=datetime.utcnow)
    ordenes: Mapped[List["Orden"]] = relationship('Orden', backref='cliente', lazy=True)
    direcciones: Mapped[List["Direccion"]] = relationship('Direccion', backref='cliente', lazy=True)


class Orden(db.Model):
    __tablename__ = 'orden'
    id: Mapped[int] = Column('idorden', Integer, primary_key=True)
    metodo_pago: Mapped[str] = Column(String(45), nullable=False)
    estado_orden: Mapped[str] = Column(String(45), nullable=False)
    fecha_orden: Mapped[datetime] = Column(db.DateTime, nullable=False, default=datetime.utcnow)
    costo_total: Mapped[int] = Column(Integer, nullable=False)
    cliente_id: Mapped[int] = Column('cliente_idcliente', Integer, ForeignKey('clientes.idcliente'), nullable=False)

    pagos: Mapped[List["Pago"]] = relationship('Pago', backref='orden', lazy=True)
    items: Mapped[List["OrdenItems"]] = relationship('OrdenItems', backref='orden', lazy=True)


class Categoria(db.Model):
    __tablename__ = 'categoria'
    id: Mapped[int] = Column('idcategoria', Integer, primary_key=True)
    nombre: Mapped[str] = Column(String(45), nullable=False)

    componentes: Mapped[List["Componente"]] = relationship('Componente', backref='categoria', lazy=True)


class Componente(db.Model):
    __tablename__ = 'componentes'
    id: Mapped[int] = Column('idcomponente', Integer, primary_key=True)
    nombre: Mapped[str] = Column(String(100))
    descripcion: Mapped[str] = Column(db.Text)
    precio: Mapped[Decimal] = Column(db.Numeric(10, 2))
    stock: Mapped[int] = Column(Integer)
    categoria_id: Mapped[int] = Column('categoria_idcategoria', Integer, ForeignKey('categoria.idcategoria'),
                                       nullable=False)
    carrito_items: Mapped[List["CarritoItems"]] = relationship('CarritoItems', backref='componente', lazy=True)
    orden_items: Mapped[List["OrdenItems"]] = relationship('OrdenItems', backref='componente', lazy=True)


class Carrito(db.Model):
    __tablename__ = 'carritos'
    id: Mapped[int] = Column('idcarrito', Integer, primary_key=True)
    estado: Mapped[Estado] = Column(db.Enum(Estado), default=Estado.ABIERTO)


class CarritoItem(db.Model):
    __tablename__ = 'carrito_items'
    id: Mapped[int] = Column(Integer, primary_key=True)
    cantidad: Mapped[int] = Column(Integer)
    items: Mapped[List["CarritoItems"]] = relationship('CarritoItems', backref='carrito', lazy=True)
    sesiones: Mapped[List["SesionUsuario"]] = relationship('SesionUsuario', backref='carrito', lazy=True)


class Direccion(db.Model):
    __tablename__ = 'direccion'
    id: Mapped[int] = Column('iddireccion', Integer, primary_key=True)
    calle: Mapped[str] = Column(String(45), nullable=False)
    ciudad: Mapped[str] = Column(String(45), nullable=False)
    provincia: Mapped[str] = Column(String(45), nullable=False)
    codigo_postal: Mapped[str] = Column(String(45), nullable=False)
    cliente_id: Mapped[int] = Column('cliente_idcliente', Integer, ForeignKey('clientes.idcliente'), nullable=False)


class OrdenItems(db.Model):
    __tablename__ = 'ordenitems'
    id: Mapped[int] = Column('idordenitems', Integer, primary_key=True)
    cantidad: Mapped[int] = Column(Integer, nullable=False)
    precio_al_comprar: Mapped[int] = Column(Integer, nullable=False)
    # orden_id: Mapped[int] = Column('orden_idorden', Integer, ForeignKey('orden.idorden'), nullable=False)
    componente_id: Mapped[int] = Column('componente_idcomponente', Integer, ForeignKey('componentes.idcomponente'),
                                        nullable=False)


class Pago(db.Model):
    __tablename__ = 'pago'
    id: Mapped[int] = Column('idpago', Integer, primary_key=True)
    orden_id: Mapped[int] = Column('orden_idorden', Integer, ForeignKey('orden.idorden'), nullable=False)


class SesionUsuario(db.Model):
    __tablename__ = 'sesion_usuario'
    id: Mapped[int] = Column('idsesion_usuario', Integer, primary_key=True)
    cliente_id: Mapped[int] = Column('cliente_idcliente', Integer, ForeignKey('clientes.idcliente'), nullable=False)
    carrito_id: Mapped[int] = Column('carrito_idcarrito', Integer, ForeignKey('carritos.idcarrito'), nullable=False)
