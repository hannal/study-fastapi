from contrib.testing.decorators import pytest_async

from apps.hello import controllers


@pytest_async
async def test_hello_controller():
    res = await controllers.hello()
    assert isinstance(res, dict)
