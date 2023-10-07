from typing import Union

from fastapi import FastAPI

from app.config.db import init_db

app = FastAPI()
init_db()


@app.get("/")
def read_root():
    return {"Hello": "World"}
