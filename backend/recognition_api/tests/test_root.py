import pytest


@pytest.mark.asyncio
async def test_api_works(async_client):
    response = await async_client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "API works!"
