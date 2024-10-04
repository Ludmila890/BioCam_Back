from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel, ConfigDict
from models.models import Estado


# schemas cliente
class ClienteBase(BaseModel):
    id: int
    nombre: str
    correo: str
    clave: str
    telefono: str | None
    direccion: str | None
    fecha_creacion: datetime
    ultima_actividad: datetime | None


class CrearCliente(ClienteBase):
    id: int | None


class ActualizarCliente(BaseModel):
    nombre: str | None
    correo: str | None
    clave: str | None
    telefono: str | None
    direccion: str | None
    ultima_actividad: datetime | None


class GetCliente(BaseModel):
    id: int | None
    nombre: str | None
    correo: str | None
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


class CrearComponente(ComponenteBase):
    id: int | None


class ActualizarComponente(BaseModel):
    nombre: str | None
    descripcion: str | None
    precio: Decimal | None
    stock: int | None
    categoria: str | None
    fecha_actualizacion: datetime


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
