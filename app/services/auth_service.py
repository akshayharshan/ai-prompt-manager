from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import HTTPException
from fastapi import Depends
from app.core.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import SECRET_KEY, ALGORITHM,create_access_token, hash_password, verify_password,oauth2_scheme
from jose import JWTError,jwt



async def register_user(user_data:UserCreate, db:AsyncSession):
    result = await db.execute(
        select(User).where(User.email == user_data.email)
    )
    existing_user = result.scalar_one_or_none()

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    new_user = User(
        email = user_data.email,
        hash_password = hash_password(user_data.password)
    )
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    return new_user
async def login_user(db:AsyncSession,email:str,password:str):

    result = await db.execute(
        select(User).where(User.email == email)
    )
    user = result.scalar_one_or_none()

    if not user or not verify_password(password,user.hash_password):
        raise HTTPException(status_code=401,detail="Invalid credentials")
    
    access_token = create_access_token({"sub":str(user.id)})
    return {"access_token": access_token} 

async def get_current_user(token: str = Depends(oauth2_scheme),db: AsyncSession = Depends(get_db)):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        user_id : str = payload.get("sub")

        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token")
    except JWTError:
        raise HTTPException(status_code=401,detail = "Invalid token")
    result = await db.execute(select(User).where(User.id == int(user_id)))
    user = result.scalar_one_or_none()

    if user is None:
        raise HTTPException(status_code=401,detail="User not found")
    return user