from fastapi import status
from httpx import AsyncClient


async def test_create_post_success(client: AsyncClient, access_token: str):
    headers = {"Authorization": f"Bearer {access_token}"}
    data = {
        "title": "post 1",
        "content": "some content",
        "published_at": "2024-04-12T04:33:14.403Z",
        "published": True,
    }

    response = await client.post("/posts/", json=data, headers=headers)

    content = response.json()

    assert response.status_code == status.HTTP_201_CREATED
    assert content["id"] is not None


async def test_create_post_invalid_payload_fail(client: AsyncClient, access_token: str):
    headers = {"Authorization": f"Bearer {access_token}"}
    data = {
        "content": "some content",
        "published_at": "2024-04-12T04:33:14.403z",
        "published": True,
    }

    response = await client.post("/posts/", json=data, headers=headers)

    content = response.json()

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert content["detail"][0]["loc"] == ["body", "title"]


async def test_create_post_not_authenticated_fail(client: AsyncClient):
    data = {
        "title": "post 1",
        "content": "some content",
        "published_at": "2024-04-12T04:33:14.403z",
        "published": True,
    }

    response = await client.post("/posts/", json=data, headers={})

    content = response.json()

    assert response.status_code == status.HTTP_401_UNAUTHORIZED
