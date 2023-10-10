from pydantic import BaseModel


class Cuenta(BaseModel):
    id: int
    id_cliente: int

    class Config:
        orm_mode = True


class CrearCuenta(Cuenta):
    pass
