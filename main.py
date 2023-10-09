from fastapi import FastAPI
from app.config.db import Base, engine
from app.models import cliente, categoria, categoria_cliente, cuenta, movimiento

app = FastAPI()
Base.metadata.create_all(engine)


@app.get("/healthCheck")
def health_check():
    return {"Hello": "World"}
