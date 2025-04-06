from fastapi import FastAPI
from services.auth_service import router as auth_router
from services.user_service import router as user_router

app = FastAPI(title="API Gateway")

# Include both services
app.include_router(auth_router, prefix="/auth", tags=["Auth Service"])
app.include_router(user_router, prefix="/users", tags=["User Service"])
