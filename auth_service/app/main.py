from fastapi import FastAPI
from app.routes.auth_routes import router as auth_router

app = FastAPI()

# Mount auth routes
app.include_router(auth_router, prefix="/auth", tags=["Auth"])
