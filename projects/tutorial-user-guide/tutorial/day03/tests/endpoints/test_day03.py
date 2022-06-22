from pathlib import Path

import pytest
from fastapi import UploadFile, HTTPException, status

from tutorial.day03.endpoints import path_op_conf
from tutorial.day03.endpoints import handling_errors


@pytest.fixture
def upload_file():
    _path = Path(__file__).resolve().parent / "uploadfile.txt"
    with _path.open("rb") as fp:
        yield fp


@pytest.mark.anyio
async def test_create_item(upload_file):
    item = path_op_conf.Item(
        name="hello",
        price=100_000.0,
    )
    file = UploadFile("hello.txt", upload_file)
    res = await path_op_conf.create_item(item, file)
    assert res.description == file.filename


@pytest.mark.anyio
async def test_404_error():
    with pytest.raises(HTTPException) as exc:
        await handling_errors.read_item("invalid")

    assert exc.value.status_code == status.HTTP_404_NOT_FOUND
