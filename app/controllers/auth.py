from fastapi import APIRouter
from app.schemas.auth import LoginIn
from app.security import sign_jwt
from app.security import create_access_token, verify_token  # Ajuste conforme necessário

router = APIRouter()

@router.post("/login")
async def login(data: LoginIn):
    return sign_jwt(user_id=data.user_id)
