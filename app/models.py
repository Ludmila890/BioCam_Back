from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cliente(db.Model):
    __tablename__ = 'Clientes'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), unique=True, nullable=False)
    clave = db.Column(db.String(255), nullable=False)
    telefono = db.Column(db.String(20))
    direccion = db.Column(db.String(255))
    fecha_creacion = db.Column(db.DateTime, default=db.func.current_timestamp())
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
    fecha_creacion = db.Column(db.DateTime, default=db.func.current_timestamp())
    fecha_actualizacion = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

class Carrito(db.Model):
    __tablename__ = 'Carritos'
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('Clientes.id'), nullable=False)
    fecha_creacion = db.Column(db.DateTime, default=db.func.current_timestamp())
    fecha_actualizacion = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    estado = db.Column(db.Enum('abierto', 'cerrado'), default='abierto')
    cliente = db.relationship('Cliente', backref=db.backref('carritos', lazy=True))

class CarritoItem(db.Model):
    __tablename__ = 'Carrito_Items'
    id = db.Column(db.Integer, primary_key=True)
    carrito_id = db.Column(db.Integer, db.ForeignKey('Carritos.id'), nullable=False)
    componente_id = db.Column(db.Integer, db.ForeignKey('Componentes.id'), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    precio = db.Column(db.Numeric(10, 2), nullable=False)
    fecha_agregado = db.Column(db.DateTime, default=db.func.current_timestamp())
    carrito = db.relationship('Carrito', backref=db.backref('items', lazy=True))
    componente = db.relationship('Componente', backref=db.backref('items', lazy=True))
