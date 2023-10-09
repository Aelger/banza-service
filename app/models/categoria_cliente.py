from sqlalchemy import Column, Integer, ForeignKey
from app.config.db import Base
from sqlalchemy.orm import relationship
from app.models import categoria


class CategoriaCliente(Base):
    __tablename__ = 'categoria_cliente'

    id_categoria = Column(Integer, ForeignKey('categoria.id'), primary_key=True)
    id_cliente = Column(Integer, ForeignKey('cliente.id'), nullable=False)

    categoria = relationship("Categoria", back_populates="CategoriaCliente")
    cliente = relationship("Cliente", back_populates="CategoriaCliente")
