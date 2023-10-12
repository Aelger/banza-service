from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.config.db import obtener_conexion
from app.services import cuenta

cuentas_router = APIRouter()


@cuentas_router.get("/crear-cuenta/{id_cliente}")
async def crear_cuenta(id_cliente, db: Session = Depends(obtener_conexion)):
    cuenta_db = cuenta.crear(db, id_cliente)
    db.refresh(cuenta_db)
    return cuenta_db
