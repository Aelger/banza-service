from sqlalchemy import Column, Integer, Enum, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.config.db import Base


class Movimiento(Base):
    __tablename__ = 'movimiento'

    id = Column(Integer, primary_key=True)
    id_cuenta = Column(Integer, ForeignKey('cuenta.id'), nullable=False)
    tipo = Column(Enum('Ingreso', 'Egreso', name='tipos de movimientos'), nullable=False)
    importe = Column(Integer, nullable=False)
    fecha = Column(Date, nullable=False)
    cuenta = relationship("Cuenta", back_populates="movimientos")

    def __repr__(self):
        return f"Movimiento del tipo: {self.tipo} con la cuenta id: {self.id_cuenta}"

    def __str__(self):
        return self.tipo
