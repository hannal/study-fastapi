from pathlib import Path

import pytest
from fastapi import FastAPI, status
from httpx import AsyncClient

from contrib.testing.decorators import pytest_async, pytest_parametrize


@pytest.fixture
async def client_for_uploading(initialized_app: FastAPI) -> AsyncClient:
    async with AsyncClient(
        app=initialized_app,
        base_url="http://day03.testserver",
        # headers={
        #     "Content-Type": "multipart/form-data; boundary=80ae023a1d0500c1554eb26d4cf9f66d",
        #     "Content-Type": "multipart/form-data",
        # },
        headers=None,
    ) as client:
        yield client


@pytest.fixture
def upload_file():
    _path = Path(__file__).resolve().parent / "uploadfile.txt"
    with _path.open("rb") as fp:
        yield fp


@pytest_parametrize(
    "url_name, expected_status",
    [
        ["create_file", status.HTTP_201_CREATED],
        ["create_upload_file", status.HTTP_201_CREATED],
    ],
)
# @pytest.mark.anyio
@pytest_async
async def test_create_file(
    app: FastAPI,
    client_for_uploading: AsyncClient,
    upload_file,
    url_name,
    expected_status,
):
    client = client_for_uploading
    files = {
        "file": upload_file,
    }
    res = await client.post(app.url_path_for(url_name), files=files)
    res.request.read()
    assert res.status_code == expected_status
