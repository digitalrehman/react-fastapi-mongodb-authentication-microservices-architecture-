from fastapi import FastAPI
from app.routes.user_routes import router as user_router

app = FastAPI()

# Include user routes
app.include_router(user_router, prefix="/users", tags=["Users"])
