from fastapi import APIRouter

from src.security import sign_jwt
from src.views.auth import LoginOut
from src.schemas.auth import LoginIn

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login", response_model=LoginOut)
async def login(data: LoginIn):
    token_data = sign_jwt(user_id=data.user_id)
    return LoginOut(access_token=token_data["access_token"])
