import json
from pathlib import Path

import pytest
from fastapi import FastAPI, status
from fastapi.testclient import TestClient
from httpx import AsyncClient

from contrib.testing.decorators import pytest_async, pytest_parametrize

from tutorial.exceptions import BaseHttpTeapotError
from tutorial.day03.handlers.error import Day03CustomError


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
    assert res.status_code == expected_status


@pytest_parametrize(
    "url_name, expected_status",
    [
        ["create_item_with_file", status.HTTP_201_CREATED],
        ["create_item_with_file2", status.HTTP_200_OK],
    ],
)
def test_create_item_with_file(
    app: FastAPI,
    client: TestClient,
    upload_file,
    url_name,
    expected_status,
):
    payload = {
        "item": {
            "name": "Hannal",
            "description": "Lorem Ipsum",
            "price": 100_000.0,
            "tax": 10.0,
            "tags": ["Tag1", "Tag2"],
        },
    }
    files = {
        "file": upload_file,
        "item": (
            None,
            json.dumps(payload["item"]),
        ),
    }
    res = client.post(app.url_path_for(url_name), files=files)
    data = res.json()
    assert res.status_code == expected_status
    assert data["description"] in upload_file.name


@pytest_parametrize(
    "item_id, expected_status",
    [
        ["foo", status.HTTP_200_OK],
        ["-invalid-", status.HTTP_404_NOT_FOUND],
    ],
)
def test_404_error(
    app: FastAPI,
    client: TestClient,
    item_id,
    expected_status,
):
    url_name = "read_item_for_404_error"
    res = client.get(app.url_path_for(url_name, item_id=item_id))
    assert res.status_code == expected_status
    if expected_status == status.HTTP_404_NOT_FOUND:
        data = res.json()
        assert data["custom_field"] == "not-found"


@pytest_parametrize(
    "url_name, expected_status, expected_detail",
    [
        ["day03_teapot_error", Day03CustomError.status_code, Day03CustomError.detail],
        [
            "base_teapot_error",
            BaseHttpTeapotError.status_code,
            BaseHttpTeapotError.detail,
        ],
    ],
)
def test_teapot_error(
    app: FastAPI,
    client: TestClient,
    url_name,
    expected_status,
    expected_detail,
):
    res = client.get(app.url_path_for(url_name))
    assert res.status_code == expected_status
    data = res.json()
    assert data["message"] == expected_detail
