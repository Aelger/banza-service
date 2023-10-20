from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services import cliente, cuenta, categoria_cliente
from app.config.db import obtener_conexion
from app.schemas.cliente import ClienteBase, ActualizarCliente

cliente_router = APIRouter(prefix="/cliente", tags=["cliente"], deprecated=False)


@cliente_router.get("/{id_cliente}")
async def obtener_cliente(id_cliente: int, db: Session = Depends(obtener_conexion)):
    db_cliente = cliente.obtener(db, id_cliente)
    return db_cliente


@cliente_router.get("/", description="")
async def obtener_clientes(db: Session = Depends(obtener_conexion)):
    return cliente.obtener_todos(db)


@cliente_router.post("/crear")
async def crear_cliente(cliente_body: ClienteBase, db: Session = Depends(obtener_conexion)):
    nuevo_cliente = cliente.crear(db, cliente_body)
    nueva_cuenta = cuenta.crear(db, nuevo_cliente.id)
    db.refresh(nuevo_cliente)
    db.refresh(nueva_cuenta)
    return {"nuevo_cliente": nuevo_cliente, "nueva_cuenta": nueva_cuenta}


@cliente_router.delete("/borrar/{id_cliente}")
async def borrar_cliente(id_cliente: int, db: Session = Depends(obtener_conexion)):
    cliente.borrar(db, id_cliente)


@cliente_router.put("/editar/{id_cliente}")
async def editar_cliente(id_cliente: int, cliente_update: ActualizarCliente, db: Session = Depends(obtener_conexion)):
    cliente.editar(db, cliente_update, id_cliente)


@cliente_router.get("/cuentas/{id_cliente}")
async def cuentas_por_cliente(id_cliente: int, db: Session = Depends(obtener_conexion)):
    cuentas = cliente.obtener(db, id_cliente).cuenta
    return cuentas


@cliente_router.post("/agregar-categoria")
async def agregar_categoria(id_cliente: int, id_categoria: int, db: Session = Depends(obtener_conexion)):
    categoria_cliente_db = categoria_cliente.añadir_categoria_cliente(db, id_cliente, id_categoria)
    return categoria_cliente_db