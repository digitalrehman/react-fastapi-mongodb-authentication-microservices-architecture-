from fastapi import APIRouter, HTTPException
from app.models.auth_model import UserCreate, UserLogin
from app.db.database import user_collection
from app.utils.hashing import hash_password, verify_password
from app.utils.jwt_handler import create_access_token

router = APIRouter()


@router.post("/signup")
async def signup(user: UserCreate):
    existing_user = await user_collection.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed = hash_password(user.password)
    user_dict = {"name": user.name, "email": user.email, "password": hashed}
    result = await user_collection.insert_one(user_dict)
    return {"msg": "User registered", "user_id": str(result.inserted_id)}


@router.post("/login")
async def login(user: UserLogin):
    db_user = await user_collection.find_one({"email": user.email})
    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": str(db_user["_id"])})
    return {"access_token": token, "token_type": "bearer"}
