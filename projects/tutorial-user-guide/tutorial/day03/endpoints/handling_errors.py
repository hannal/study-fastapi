from fastapi import HTTPException, status

from tutorial.exceptions import BaseHttpTeapotError
from ..app import app
from ..handlers.error import Day03CustomError

items = {"foo": "The foo wrestlers"}


@app.get("/items/{item_id}", name="read_item_for_404_error")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )
    return {"item": items[item_id]}


@app.get("/teapot-error", name="day03_teapot_error")
async def day03_teapot_error():
    raise Day03CustomError()


@app.get("/base-teapot-error", name="base_teapot_error")
async def base_teapot_error():
    raise BaseHttpTeapotError()
