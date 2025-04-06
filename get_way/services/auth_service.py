from fastapi import APIRouter, Request
import httpx

router = APIRouter()
AUTH_SERVICE_URL = "http://localhost:8001"  # auth_service

@router.post("/signup")
async def signup(request: Request):
    async with httpx.AsyncClient() as client:
        data = await request.json()
        response = await client.post(f"{AUTH_SERVICE_URL}/signup", json=data)
        return response.json()

@router.post("/login")
async def login(request: Request):
    async with httpx.AsyncClient() as client:
        data = await request.json()
        response = await client.post(f"{AUTH_SERVICE_URL}/login", json=data)
        return response.json()
