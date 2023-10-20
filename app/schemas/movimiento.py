from pydantic import BaseModel
from datetime import date


class Movimiento(BaseModel):
    id: int
    id_cuenta: int
    tipo: str
    importe: int
    fecha: date

    class ConfigDict:
        orm_mode = True


class CrearMovimiento(Movimiento):
    pass
