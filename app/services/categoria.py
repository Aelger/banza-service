from sqlalchemy.orm import Session
from app.models.categoria import Categoria as model_categoria
from app.schemas.categoria import Categoria as schema_categoria


def obtener(db: Session, id_categoria: int):
    return db.query(model_categoria).filter(model_categoria.id == id_categoria).first()


def crear(db: Session, categoria: schema_categoria):
    categoria_db = model_categoria(nombre=categoria.nombre)
    db.add(categoria_db)
    db.commit()
    db.refresh(categoria_db)
    return categoria_db
