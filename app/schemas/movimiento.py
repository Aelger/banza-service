from pydantic import BaseModel
from datetime import date
from app.schemas.cuenta import Cuenta


class Movimiento(BaseModel):
    id: int
    id_cuenta: int
    tipo: str
    importe: int
    fecha: date
    cuenta: Cuenta

    class Config:
        orm_mode = True


class CrearMovimiento(Movimiento):
    pass
