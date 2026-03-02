from app.schemas.user import UserCreate
from fastapi import APIRouter, Depends, HTTPException
from app.core.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from app.services import auth_service





router = APIRouter(prefix="/auth" ,tags=["Auth"])
@router.post("/register")
async def register(user_data:UserCreate, db: AsyncSession = Depends(get_db)):
    return await auth_service.register_user(user_data,db)
