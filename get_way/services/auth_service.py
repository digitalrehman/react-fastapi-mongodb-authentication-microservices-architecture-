from fastapi import APIRouter
import httpx
from models.auth_model import UserCreate, UserLogin

router = APIRouter()
AUTH_SERVICE_URL = "http://localhost:8001"

@router.post("/signup")
async def signup(request: UserCreate):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{AUTH_SERVICE_URL}/auth/signup", json=request.dict())
        return response.json()


@router.post("/login")
async def login(request: UserLogin):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{AUTH_SERVICE_URL}/auth/login", json=request.dict())
        return response.json()
