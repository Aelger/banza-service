from app.config.db import Base
from sqlalchemy import Column, Integer, String


class Cliente(Base):
    __tablename__ = 'cliente'

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)

    def __init__(self, nombre):
        self.nombre = nombre

    def __repr__(self):
        return f"Cliente nombre: {self.nombre} con id: {self.id}"

    def __str__(self):
        return self.nombre
