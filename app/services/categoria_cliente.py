from sqlalchemy.orm import Session
from app.models.categoria_cliente import CategoriaCliente


def añadir_categoria_cliente(db: Session, id_cliente: int, id_categoria: int):
    categoria_cliente = CategoriaCliente(id_cliente=id_cliente, id_categoria=id_categoria)
    db.add(categoria_cliente)
    db.commit()
    db.refresh(categoria_cliente)
    return categoria_cliente

