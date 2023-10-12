from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.config.db import Base


class Categoria(Base):
    __tablename__ = 'categoria'

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    categorias_cliente = relationship("CategoriaCliente", back_populates="categoria")

    def __repr__(self):
        return f"Categoria del tipo: {self.nombre}"

    def __str__(self):
        return self.nombre
