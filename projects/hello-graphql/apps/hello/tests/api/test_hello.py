from fastapi import FastAPI
from httpx import AsyncClient
from starlette import status

from contrib.testing.decorators import pytest_async, pytest_parametrize


graphql_path = "/graphql"


@pytest_parametrize(
    "url_name, expected_status",
    [
        ["hello:index", status.HTTP_200_OK],
    ],
)
@pytest_async
async def test_hello(app: FastAPI, client: AsyncClient, url_name, expected_status):
    res = await client.get(app.url_path_for(url_name))
    assert res.status_code == expected_status


@pytest_parametrize(
    "url_name, expected_status",
    [
        ["hello:index", status.HTTP_200_OK],
    ],
)
@pytest_async
async def test_hello_graphql(
    app: FastAPI, client: AsyncClient, url_name, expected_status
):
    _query = """query user($username: String!) {
        user(username: $username) {
            username
            name
        }
    }"""

    payload = {
        "query": _query,
        "variables": {
            "username": "hannal",
        },
    }
    res = await client.post(graphql_path, json=payload)
    assert res.status_code == expected_status
    data = res.json()
    assert isinstance(data.get("data"), dict)
    assert data["data"]["user"]["username"] == payload["variables"]["username"]


@pytest_async
async def test_create_user_graphql(app: FastAPI, client: AsyncClient):
    _query = """mutation createUser($username: String!, $name: String!){
        createUser(username: $username, name: $name) {
            username
        }
    }"""
    payload = {
        "query": _query,
        "variables": {
            "username": "hannal",
            "name": "Kay Cha",
        },
    }
    res = await client.post(graphql_path, json=payload)
    assert res.status_code == 200
    data = res.json()
    assert data["data"]["createUser"]["username"] == payload["variables"]["username"]
