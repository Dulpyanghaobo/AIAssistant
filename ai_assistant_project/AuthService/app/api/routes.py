from fastapi import APIRouter
from AuthService.app.api.views import auth_login

router = APIRouter()

router.include_router(auth_login.router, tags=["auth"], prefix="/api/v1/login")
