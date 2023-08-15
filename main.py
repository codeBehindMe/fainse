from typing import Union

from fastapi import FastAPI

app = FastAPI()

_NOT_IMPLEMENTED_RESPONSE = {"error": "not implemented"}


@app.get("/")
def read_root():
    return {"fainse": "root"}


@app.get("/client/list")
def read_clients():
    return _NOT_IMPLEMENTED_RESPONSE
