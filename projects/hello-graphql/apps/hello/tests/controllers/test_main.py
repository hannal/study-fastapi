import pytest
import asyncio
import httpx
import json


URL_A = "https://23123adtest.com/api/trains"  # 예시용 URL
URL_B = "https://10912803test.com/api/buses"  # 예시용 URL


async def request(client, url, params):
    response = await client.get(url, params=params)
    return {"url": response.request.url, "json": json.loads(response.text)}


async def main():
    async with httpx.AsyncClient() as client:
        tasks = []
        params = {"default": "default_value"}

        for i in range(0, 17, 2):  # 0부터 16까지 2씩 증가
            d = params.copy()
            d.update({"offset": i})
            tasks.append(
                asyncio.create_task(request(client=client, url=URL_A, params=d))
            )

        for i in range(0, -12, -3):  # 0부터 -12까지 3씩 감소
            d = params.copy()
            d.update({"offset": i})
            tasks.append(
                asyncio.create_task(request(client=client, url=URL_B, params=d))
            )

        results = await asyncio.gather(*tasks)

    return results


@pytest.mark.asyncio
async def test_main():
    result = await main()
    print("/" * 80)
    print(result)
    assert 1 == 2
