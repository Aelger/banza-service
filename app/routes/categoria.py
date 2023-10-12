from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.config.db import obtener_conexion
from app.services import categoria
from app.schemas.categoria import Categoria


categoria_router = APIRouter(prefix="/categoria", tags=["categoria"], deprecated=False)


@categoria_router.get("/{id_categoria}")
async def obtener_categoria(id_categoria: int, db: Session = Depends(obtener_conexion)):
    db_categoria = categoria.obtener(db, id_categoria)
    return db_categoria


@categoria_router.post("/crear")
async def crear_categoria(categoria_body: Categoria, db: Session = Depends(obtener_conexion)):
    db_categoria = categoria.crear(db, categoria_body)
    return db_categoria


@categoria_router.get("/aber/{id_categoria}")
async def aber_categoria(id_categoria: int, db: Session = Depends(obtener_conexion)):
    categorias = categoria.obtener(db, id_categoria).categoria_cliente
    return categorias