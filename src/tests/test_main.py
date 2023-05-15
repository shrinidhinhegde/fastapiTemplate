import pytest
from httpx import AsyncClient

from .test_database_config import server

test_client = AsyncClient(app=server, base_url="http://localhost:8000")


@pytest.mark.asyncio
async def test_root():
    response = await test_client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to App Backend"}


@pytest.mark.asyncio
async def test_app_health():
    response = await test_client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"message": "OK"}
