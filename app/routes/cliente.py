from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services import cliente, cuenta
from app.config.db import obtener_conexion
from app.schemas.cliente import ClienteBase

cliente_router = APIRouter()


@cliente_router.get("/cliente/{id_cliente}")
async def obtener_cliente(id_cliente: int, db: Session = Depends(obtener_conexion)):
    db_cliente = cliente.obtener(db, id_cliente)
    return db_cliente


@cliente_router.get("/cliente")
async def obtener_clientes(db: Session = Depends(obtener_conexion)):
    return cliente.obtener_todos(db)


@cliente_router.post("/crear-cliente")
async def crear_cliente(cliente_body: ClienteBase, db: Session = Depends(obtener_conexion)):
    nuevo_cliente = cliente.crear(db, cliente_body)
    nueva_cuenta = cuenta.crear(db, nuevo_cliente.id)
    db.refresh(nuevo_cliente)
    db.refresh(nueva_cuenta)
    return {"nuevo_cliente": nuevo_cliente, "nueva_cuenta": nueva_cuenta}


@cliente_router.delete("/borrar-cliente/{id_cliente}")
async def borrar_cliente(id_cliente: int, db: Session = Depends(obtener_conexion)):
    cliente.borrar(db, id_cliente)


@cliente_router.get("/cuentas-cliente/{id_cliente}")
async def cuentas_por_cliente(id_cliente: int, db: Session = Depends(obtener_conexion)):
    cuentas = cliente.obtener(db, id_cliente).cuenta
    return cuentas
