from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.config.db import Base


class Cliente(Base):
    __tablename__ = 'cliente'

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    cuentas = relationship("Cuenta", back_populates="Cliente")
    categoria_cliente = relationship("CategoriaCliente", uselist=False, back_populates="Cliente")

    def __repr__(self):
        return f"Cliente nombre: {self.nombre} con id: {self.id}"

    def __str__(self):
        return self.nombre
