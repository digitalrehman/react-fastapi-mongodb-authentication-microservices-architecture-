from fastapi import APIRouter, Request
import httpx

router = APIRouter()
USER_SERVICE_URL = "http://localhost:8002"  # user_service

@router.post("/")
async def create_user(request: Request):
    async with httpx.AsyncClient() as client:
        data = await request.json()
        response = await client.post(f"{USER_SERVICE_URL}/users/", json=data)
        return response.json()

@router.get("/{user_id}")
async def get_user(user_id: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{USER_SERVICE_URL}/users/{user_id}")
        return response.json()

@router.put("/{user_id}")
async def update_user(user_id: str, request: Request):
    async with httpx.AsyncClient() as client:
        data = await request.json()
        response = await client.put(f"{USER_SERVICE_URL}/users/{user_id}", json=data)
        return response.json()

@router.delete("/{user_id}")
async def delete_user(user_id: str):
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"{USER_SERVICE_URL}/users/{user_id}")
        return response.json()
