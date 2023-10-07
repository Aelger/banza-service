from typing import Union

from fastapi import FastAPI

from app.config.db import Base

app = FastAPI()


@app.get("/")
def read_root():
    base = Base
    return {"Hello": "World"}
