from sqlalchemy.orm import Session
from app.models.cliente import Cliente
from app.models.cuenta import Cuenta
from app.schemas.cliente import ClienteBase


def obtener(db: Session, id_cliente: int):
    return db.query(Cliente).filter(Cliente.id == id_cliente).first()


def crear(db: Session, cliente: ClienteBase):
    cliente_db = Cliente(nombre=cliente.nombre)
    db.add(cliente_db)
    db.commit()
    return cliente_db


def obtener_todos(db: Session):
    return db.query(Cliente).all()


def editar(db: Session, cliente: ClienteBase):
    pass


def borrar(db: Session, id_cliente: int):
    cliente = obtener(db, id_cliente)
    db.delete(cliente)
    db.commit()
