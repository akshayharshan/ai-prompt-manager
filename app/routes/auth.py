from app.schemas.user import UserCreate
from app.schemas.auth import TokenResponse,LoginRequest
from fastapi import APIRouter, Depends, HTTPException
from app.core.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from app.services.auth_service import register_user,login_user
from app.services.auth_service import get_current_user
from app.models import User
from fastapi.security import OAuth2PasswordRequestForm





router = APIRouter(prefix="/auth" ,tags=["Auth"])
@router.post("/register")
async def register(user_data:UserCreate, db: AsyncSession = Depends(get_db)):
    return await register_user(user_data,db)

@router.post("/login",response_model=TokenResponse)
async def login(form_data: OAuth2PasswordRequestForm = Depends(),db:AsyncSession = Depends(get_db)):
    return await login_user(db,form_data.username,form_data.password)

@router.get("/me")
async def get_me(current_user: User = Depends(get_current_user)):
    return{
        "id": current_user.id,
        "email" : current_user.email
    }

