from pydantic import BaseModel


class ClienteBase(BaseModel):
    nombre: str


class Cliente(ClienteBase):
    categoria_cliente: int

    class Config:
        orm_mode = True
