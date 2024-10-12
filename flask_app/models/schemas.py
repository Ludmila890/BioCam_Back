from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel, ConfigDict
from models.models import Estado


# schemas cliente
class ClienteBase(BaseModel):
    id: int
    nombre: str
    email: str
    clave: str
    telefono: str | None
    direccion: str | None
    fecha_creacion: datetime
    ultima_actividad: datetime | None


class CrearCliente(BaseModel):
    nombre: str
    email: str
    clave: str

    model_config = ConfigDict(from_attributes=True)


class ActualizarCliente(BaseModel):
    nombre: str | None = None
    email: str | None = None
    clave: str | None = None
    telefono: str | None = None
    direccion: str | None = None

    model_config = ConfigDict(from_attributes=True)


class GetCliente(BaseModel):
    id: int | None
    nombre: str | None
    email: str | None
    telefono: str | None
    direccion: str | None

    model_config = ConfigDict(from_attributes=True)


# schemas componentes
class ComponenteBase(BaseModel):
    id: int
    nombre: str
    descripcion: str | None
    precio: Decimal
    stock: int
    categoria: str
    fecha_creacion: datetime
    fecha_actualizacion: datetime | None


class CrearComponente(BaseModel):
    nombre: str
    descripcion: str | None = None
    precio: Decimal
    stock: int
    categoria: str


class ActualizarComponente(BaseModel):
    nombre: str | None = None
    descripcion: str | None = None
    precio: Decimal | None = None
    stock: int | None = None
    categoria: str | None = None
    fecha_actualizacion: datetime | None = None


class GetComponente(BaseModel):
    id: int | None
    nombre: str | None
    categoria: str | None


# schemas carrito
class CarritoBase(BaseModel):
    id: int
    cliente_id: int
    fecha_creacion: datetime
    fecha_actualizacion: datetime
    estado: Estado
    cliente: str


class CrearCarrito(CarritoBase):
    id: int | None


class CarritoItemBase(BaseModel):
    id: int
    carrito_id: int
    componente_id: int
    cantidad: int
    fecha_agregado: datetime


class ActualizarCarritoItem(BaseModel):
    carrito_id: int | None
    componente_id: int | None
    cantidad: int | None
    fecha_agregado: int | None


class CrearCarritoItem(CarritoItemBase):
    id: int | None


class GetCarritoItem(BaseModel):
    id: int | None
    carrito_id: int | None
    componente_id: int | None
    cantidad: int | None
