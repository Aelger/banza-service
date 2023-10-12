from fastapi import FastAPI
from app.models import models
from app.routes.cliente import cliente_router
from app.routes.cuenta import cuentas_router
from app.routes.categoria import categoria_router

app = FastAPI(title="Banza challenge", description="Soy una API", summary="Soy una api en python con fastapi y slqalchemy", debug=True, openapi_url="/challenge.json")
app.include_router(cliente_router, prefix="/api/V1")
app.include_router(cuentas_router, prefix="/api/V1")
app.include_router(categoria_router, prefix="/api/V1")
models.Base.metadata.create_all(models.engine)


@app.get("/healthcheck")
def health_check():
    return {"Im": "alive"}



