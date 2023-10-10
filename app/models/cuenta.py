from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.config.db import Base


class Cuenta(Base):
    __tablename__ = 'cuenta'

    id = Column(Integer, primary_key=True)
    id_cliente = Column(Integer, ForeignKey('cliente.id'), nullable=False)
    cliente = relationship("Cliente", back_populates="cuenta")
    movimientos = relationship("Movimiento", back_populates="cuenta")

    def __repr__(self):
        return f"Cuenta nro: {self.id} de cliente: {self.id_cliente}"

    def __str__(self):
        return self.id
