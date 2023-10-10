from sqlalchemy.orm import Session
from app.models.cuenta import Cuenta


def crear(db: Session, id_cliente: int):
    cuenta_db = Cuenta(id_cliente=id_cliente)
    db.add(cuenta_db)
    db.commit()
    return cuenta_db
