from sqlalchemy import delete
from app.core.redis import redis_client
from app.core.security import ALGORITHM, SECRET_KEY, create_access_token, create_refresh_token
from app.schemas.user import UserCreate
from app.schemas.auth import TokenResponse,LoginRequest
from fastapi import APIRouter, Depends, HTTPException
from app.core.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from app.services.auth_service import register_user,login_user, require_admin
from app.services.auth_service import get_current_user
from app.models import User
from fastapi.security import OAuth2PasswordRequestForm
from jose import JWTError,jwt
from app.core.rate_limiter import rate_limit
from fastapi import Request




router = APIRouter(prefix="/auth" ,tags=["Auth"])
@router.post("/register")
async def register(user_data:UserCreate, db: AsyncSession = Depends(get_db)):
    return await register_user(user_data,db)

@router.post("/login",response_model=TokenResponse)
async def login(request: Request,form_data: OAuth2PasswordRequestForm = Depends(),db:AsyncSession = Depends(get_db)):
    await rate_limit(request)
    return await login_user(db,form_data.username,form_data.password)

@router.get("/me")
async def get_me(current_user: User = Depends(get_current_user)):
    return{
        "id": current_user.id,
        "email" : current_user.email
    }

@router.post("/refresh", response_model=TokenResponse)
async def refresh_token(token:str):
    payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
    user_id = payload.get("sub")
    #rotate token
    redis_client = delete(f"refresh:{token}")
    new_access_token = create_access_token({"sub": user_id})
    new_refresh_token = create_refresh_token({"sub":user_id})

    redis_client.setex(
        f"refresh:{new_refresh_token}",
        7 * 24 * 60 * 60
    )
    return{
        "access_token" : new_access_token,
        "refresh_token" : new_refresh_token,
        "token_type": "bearer"
    }

@router.get("/admin")
async def admin_route(user: User = Depends(require_admin)):
    return {"message": "welcome admin"}

