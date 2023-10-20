from pydantic import BaseModel


class Categoria(BaseModel):
    nombre: str

    class ConfigDict:
        orm_mode = True
