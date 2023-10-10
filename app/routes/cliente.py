from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services import cliente
from app.services import cuenta
from app.config.db import obtener_conexion
from app.schemas.cliente import CrearCliente

router = APIRouter()


@router.get("/cliente/{id_cliente}")
async def obtener_cliente(id_cliente: int, db: Session = Depends(obtener_conexion)):
    db_cliente = cliente.obtener(db, id_cliente)
    return db_cliente


@router.get("/cliente")
async def obtener_clientes(db: Session = Depends(obtener_conexion)):
    return cliente.obtener_todos(db)


@router.post("/cliente")
async def crear_cliente(cliente_body: CrearCliente, db: Session = Depends(obtener_conexion)):
    nuevo_cliente = cliente.crear(db, cliente_body)
    nueva_cuenta = cuenta.crear(db, nuevo_cliente.id)
    db.refresh(nuevo_cliente)
    db.refresh(nueva_cuenta)
    return {"nuevo_cliente": nuevo_cliente, "nueva_cuenta": nueva_cuenta}


@router.delete("/borrar-cliente/{id_cliente}")
async def borrar_cliente(id_cliente: int, db: Session = Depends(obtener_conexion)):
    cliente.borrar(db, id_cliente)
