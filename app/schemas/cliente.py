from pydantic import BaseModel


class ClienteBase(BaseModel):
    nombre: str


class Cliente(ClienteBase):
    categoria_cliente: int

    class ConfigDict:
        orm_mode = True


class ActualizarCliente(Cliente):
    nombre: str = None
    categoria_cliente: int = None

    