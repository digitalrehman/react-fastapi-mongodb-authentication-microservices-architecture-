from fastapi import APIRouter
import httpx
from models.user_model import User

router = APIRouter()
USER_SERVICE_URL = "http://localhost:8002"


@router.post("/")
async def create_user(user: User):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{USER_SERVICE_URL}/users/", json=user.dict())
        return response.json()


@router.get("/{user_id}")
async def get_user(user_id: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{USER_SERVICE_URL}/users/{user_id}")
        return response.json()


@router.put("/{user_id}")
async def update_user(user_id: str, user: User):
    async with httpx.AsyncClient() as client:
        response = await client.put(f"{USER_SERVICE_URL}/users/{user_id}", json=user.dict())
        return response.json()


@router.delete("/{user_id}")
async def delete_user(user_id: str):
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"{USER_SERVICE_URL}/users/{user_id}")
        return response.json()
