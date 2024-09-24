from datetime import datetime
from . import db


class Cliente(db.Model):
    __tablename__ = 'Clientes'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), nullable=False, unique=True)
    clave = db.Column(db.String(255), nullable=False)
    telefono = db.Column(db.String(20))
    direccion = db.Column(db.String(255))
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    ultima_actividad = db.Column(db.DateTime, nullable=True)

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
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text)
    precio = db.Column(db.Numeric(10, 2), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    categoria = db.Column(db.String(50))
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    fecha_actualizacion = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

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


class Carrito(db.Model):
    __tablename__ = 'Carritos'
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('Clientes.id'), nullable=False)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    fecha_actualizacion = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    estado = db.Column(db.Enum('abierto', 'cerrado'), default='abierto')
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
    id = db.Column(db.Integer, primary_key=True)
    carrito_id = db.Column(db.Integer, db.ForeignKey('Carritos.id'), nullable=False)
    componente_id = db.Column(db.Integer, db.ForeignKey('Componentes.id'), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    fecha_agregado = db.Column(db.DateTime, default=datetime.utcnow)
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
