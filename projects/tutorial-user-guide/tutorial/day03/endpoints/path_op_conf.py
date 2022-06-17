import enum
import json
import pydantic
from fastapi import File, UploadFile, Request, Depends, status

from ..app import app


@enum.unique
class Tag(enum.Enum):
    ITEMS = "items"


class Item(pydantic.BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()


async def _unserialize_item(request: Request):
    form = await request.form()
    return Item(**json.loads(form["item"]))


@app.post(
    "/items/",
    response_model=Item,
    name="create_item_with_file",
    status_code=status.HTTP_201_CREATED,
    tags=[Tag.ITEMS],
)
async def create_item(
    item: Item = Depends(_unserialize_item),
    file: UploadFile = File(...),
):
    item.description = file.filename
    return item
