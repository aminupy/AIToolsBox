import pytest
import pytest_asyncio
from httpx import AsyncClient
from fastapi import status

from app.core.config import get_settings
from app.main import app

settings = get_settings()


async def get_mock_email():
    from uuid import uuid4

    return f"{uuid4()}@example.com"


@pytest_asyncio.fixture(autouse=True)
async def client():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac


@pytest.mark.asyncio
async def test_initialize_register(client):
    email = await get_mock_email()
    response = await client.post("/users/register/", json={"email": email})
    assert response.status_code == status.HTTP_201_CREATED
    assert "user_id" in response.json()

    response = await client.post("/users/register/", json={"email": email})
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.asyncio
async def test_request_otp(client):
    email = await get_mock_email()
    response = await client.post("/users/register/", json={"email": email})
    assert response.status_code == status.HTTP_201_CREATED

    response = await client.post("/auth/otp/request", json={"email": email})
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()["email"] == email


@pytest.mark.asyncio
async def test_verify_otp(client):
    email = await get_mock_email()
    response = await client.post("/users/register/", json={"email": email})
    assert response.status_code == status.HTTP_201_CREATED

    response = await client.post("/auth/otp/request", json={"email": email})
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()["email"] == email

    otp = input("Enter OTP: ")

    # Assuming OTP is sent and is '123456'
    response = await client.post("/auth/otp/verify", json={"email": email, "otp": otp})
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["status"] == "verified"


@pytest.mark.asyncio
async def test_finalize_register(client):
    # Create fake email
    email = await get_mock_email()

    response = await client.post("/users/register/", json={"email": email})
    user_id = response.json()["user_id"]

    response = await client.put(
        f"/users/register/{user_id}/",
        json={"email": email, "password": "strongpassword", "fullname": "Test User"},
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    response = await client.post("/auth/otp/request", json={"email": email})
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()["email"] == email

    otp = input("Enter OTP: ")

    # Assuming OTP is sent and is '123456'
    response = await client.post("/auth/otp/verify", json={"email": email, "otp": otp})
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["status"] == "verified"

    response = await client.put(
        f"/users/register/{user_id}/",
        json={"email": email, "password": "strongpassword", "fullname": "123456"},
    )
    assert response.status_code == status.HTTP_200_OK

    response = await client.put(
        f"/users/register/{user_id}/",
        json={"email": email, "password": "strongpassword", "fullname": "123456"},
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.asyncio
async def test_signin(client):
    # Create fake email
    email = await get_mock_email()

    response = await client.post("/users/register/", json={"email": email})
    user_id = response.json()["user_id"]

    response = await client.post("/auth/otp/request", json={"email": email})
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()["email"] == email

    otp = input("Enter OTP: ")

    # Assuming OTP is sent and is '123456'
    response = await client.post("/auth/otp/verify", json={"email": email, "otp": otp})
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["status"] == "verified"

    response = await client.put(
        f"/users/register/{user_id}/",
        json={"email": email, "password": "strongpassword", "fullname": "123456"},
    )
    assert response.status_code == status.HTTP_200_OK

    response = await client.post(
        "/auth/login",
        data={
            "grant_type": "password",
            "username": email,
            "password": "strongpassword",
        },
    )
    assert response.status_code == status.HTTP_200_OK
    assert "access_token" in response.cookies
    assert "refresh_token" in response.cookies


@pytest.mark.asyncio
async def test_refresh_token(client):
    # Create fake email
    email = await get_mock_email()

    response = await client.post("/users/register/", json={"email": email})
    user_id = response.json()["user_id"]

    response = await client.post("/auth/otp/request", json={"email": email})
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()["email"] == email

    otp = input("Enter OTP: ")

    # Assuming OTP is sent and is '123456'
    response = await client.post("/auth/otp/verify", json={"email": email, "otp": otp})
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["status"] == "verified"

    response = await client.put(
        f"/users/register/{user_id}/",
        json={"email": email, "password": "strongpassword", "fullname": "123456"},
    )
    assert response.status_code == status.HTTP_200_OK

    response = await client.post(
        "/auth/login",
        data={
            "grant_type": "password",
            "username": email,
            "password": "strongpassword",
        },
    )
    assert response.status_code == status.HTTP_200_OK
    assert "access_token" in response.cookies
    assert "refresh_token" in response.cookies

    client.cookies.set("refresh_token", response.cookies["refresh_token"])
    # sending request to refresh token with refresh token in cookies
    new_response = await client.post("/auth/token/refresh")
    assert response.status_code == status.HTTP_200_OK
    assert "access_token" in new_response.cookies
    assert "refresh_token" in new_response.cookies


@pytest.mark.asyncio
async def test_me(client):
    # Create fake email
    email = await get_mock_email()

    response = await client.post("/users/register/", json={"email": email})
    user_id = response.json()["user_id"]

    response = await client.post("/auth/otp/request", json={"email": email})
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()["email"] == email

    otp = input("Enter OTP: ")

    # Assuming OTP is sent and is '123456'
    response = await client.post("/auth/otp/verify", json={"email": email, "otp": otp})
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["status"] == "verified"

    response = await client.put(
        f"/users/register/{user_id}/",
        json={"email": email, "password": "strongpassword", "fullname": "123456"},
    )
    assert response.status_code == status.HTTP_200_OK

    response = await client.post(
        "/auth/login",
        data={
            "grant_type": "password",
            "username": email,
            "password": "strongpassword",
        },
    )
    assert response.status_code == status.HTTP_200_OK
    assert "access_token" in response.cookies
    assert "refresh_token" in response.cookies

    client.cookies.set("access_token", response.cookies["access_token"])
    response = await client.get("/users/me")

    assert response.status_code == status.HTTP_200_OK
    assert response.json()["email"] == email
    assert response.json()["fullname"] == "123456"
    assert response.json()["id"] == user_id
