from pathlib import Path

import pytest
from fastapi import UploadFile

from tutorial.day03.endpoints import path_op_conf as endpoints


@pytest.fixture
def upload_file():
    _path = Path(__file__).resolve().parent / "uploadfile.txt"
    with _path.open("rb") as fp:
        yield fp


async def test_create_item(upload_file):
    item = endpoints.Item(
        name="hello",
        price=100_000.0,
    )
    file = UploadFile("hello.txt", upload_file)
    res = await endpoints.create_item(item, file)
    assert res.description == file.filename
