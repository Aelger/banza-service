from fastapi import FastAPI
from app.models import models
from app.routes.cliente import cliente_router
from app.routes.cuenta import cuentas_router

app = FastAPI()
app.include_router(cliente_router)
app.include_router(cuentas_router)
models.Base.metadata.create_all(models.engine)


@app.get("/healthcheck")
def health_check():
    return {"Im": "alive"}



