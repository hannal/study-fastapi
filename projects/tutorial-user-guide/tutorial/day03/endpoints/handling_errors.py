from fastapi import HTTPException, status

from ..app import app


items = {"foo": "The foo wrestlers"}


@app.get("/items/{item_id}", name='read_item_for_404_error')
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return {"item": items[item_id]}
