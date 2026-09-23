import httpx
import pytest

from app.integrations.jsonplaceholder import JsonPlaceholderClient


@pytest.mark.asyncio
async def test_fetch_users_normalizes_payload(monkeypatch) -> None:
    payload = [
        {
            "id": 1,
            "name": "Jane Doe",
            "username": "jane",
            "email": "jane@example.com",
            "phone": "123",
            "website": "example.com",
            "company": {"name": "Example Inc"},
            "address": {"city": "Medellin"},
        }
    ]

    async def fake_get(self, url):
        request = httpx.Request("GET", url)
        return httpx.Response(200, json=payload, request=request)

    monkeypatch.setattr(httpx.AsyncClient, "get", fake_get)

    users = await JsonPlaceholderClient().fetch_users()

    assert len(users) == 1
    assert users[0].company == "Example Inc"
    assert users[0].city == "Medellin"
