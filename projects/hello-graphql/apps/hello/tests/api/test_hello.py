import pytest
from fastapi import FastAPI
from httpx import AsyncClient
from starlette import status

from contrib.testing.decorators import pytest_async


@pytest.mark.parametrize(
    "url_name, expected_status",
    [
        ["hello:index", status.HTTP_200_OK],
    ],
)
@pytest_async
async def test_hello(app: FastAPI, client: AsyncClient, url_name, expected_status):
    res = await client.get(app.url_path_for(url_name))
    assert res.status_code == expected_status
