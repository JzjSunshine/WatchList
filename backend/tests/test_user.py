import asyncio
from typing import Generator

import pytest
from fastapi.testclient import TestClient

from backend.api import app
from backend.models import User

from tortoise.contrib.test import finalizer, initializer


@pytest.fixture(scope="module")
def client() -> Generator:
    initializer(["models"])
    with TestClient(app) as c:
        yield c
    finalizer()


@pytest.fixture(scope="module")
def event_loop(client: TestClient) -> Generator:
    yield client.task.get_loop()  # type: ignore

def test_create_user(client:TestClient,event_loop:asyncio.AbstractEventLoop):
    response = client.post("/api/v1/user",json={"username":"test","password":"test123"})
    assert response.status_code == 200
    assert "test" in response.text
    user_id = response.json()["data"]["id"]

    async def get_user_by_db():
        user = await User.get(id=user_id)
        return user
    user_obj = event_loop.run_until_complete(get_user_by_db())
    assert user_obj.id == user_id


if __name__ == '__main__':
    test_create_user(client,event_loop)