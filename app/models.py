from app import db

class Cliente(db.Model):
    __tablename__ = 'clientes'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), nullable=False, unique=True)
    clave = db.Column(db.String(255), nullable=False)
    telefono = db.Column(db.String(20))
    direccion = db.Column(db.String(255))
    fecha_creacion = db.Column(db.DateTime, default=db.func.current_timestamp())
    ultima_actividad = db.Column(db.DateTime, nullable=True)

class Componente(db.Model):
    __tablename__ = 'componentes'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text)
    precio = db.Column(db.Numeric(10, 2), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    categoria = db.Column(db.String(50))
    fecha_creacion = db.Column(db.DateTime, default=db.func.current_timestamp())
    fecha_actualizacion = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

class Carrito(db.Model):
    __tablename__ = 'carritos'
    
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'), nullable=False)
    fecha_creacion = db.Column(db.DateTime, default=db.func.current_timestamp())
    fecha_actualizacion = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    estado = db.Column(db.Enum('abierto', 'cerrado'), default='abierto')

class CarritoItem(db.Model):
    __tablename__ = 'carrito_items'
    
    id = db.Column(db.Integer, primary_key=True)
    carrito_id = db.Column(db.Integer, db.ForeignKey('carritos.id'), nullable=False)
    componente_id = db.Column(db.Integer, db.ForeignKey('componentes.id'), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    precio = db.Column(db.Numeric(10, 2), nullable=False)
    fecha_agregado = db.Column(db.DateTime, default=db.func.current_timestamp())
