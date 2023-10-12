from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint
from app.config.db import Base
from sqlalchemy.orm import relationship


class CategoriaCliente(Base):
    __tablename__ = 'categoria_cliente'

    id = Column(Integer, primary_key=True)
    id_categoria = Column(Integer, ForeignKey('categoria.id'), nullable=False)
    id_cliente = Column(Integer, ForeignKey('cliente.id'), nullable=False)
    categorias = relationship("Categoria", back_populates="categoria_cliente")
    clientes = relationship("Cliente", back_populates="categoria_cliente")

    __table_args__ = (UniqueConstraint("id_cliente", "id_categoria"),)
