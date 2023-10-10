from pydantic import BaseModel
from app.schemas.cuenta import Cuenta


class ClienteBase(BaseModel):
    nombre: str


class CrearCliente(ClienteBase):
    pass


class Cliente(ClienteBase):
    categoria_cliente: int
    cuenta: Cuenta

    class Config:
        orm_mode = True
