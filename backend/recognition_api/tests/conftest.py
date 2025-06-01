import pytest_asyncio
from httpx import ASGITransport, AsyncClient

from core.config import Settings, get_settings
from main import recognition_api

settings: Settings = get_settings()


@pytest_asyncio.fixture
async def async_client():
    async with AsyncClient(
        transport=ASGITransport(app=recognition_api),
        base_url=f"http://0.0.0.0:8000/{settings.CURRENT_API_URL}",
    ) as client:
        yield client
