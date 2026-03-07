from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncScalarResult
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.sql.functions import current_user
from app.core.redis import redis_client
from app.core.database import get_db
from app.models.prompt import Prompt
from app.models.user import User
from app.schemas.prompt import PromptCreate
from app.services.auth_service import get_current_user
import json
from sqlalchemy import select 


router = APIRouter(prefix="/prompts" ,tags=["Prompts"])

@router.get("/")
async def get_prompts(db: AsyncSession = Depends(get_db)):
    cache = redis_client.get("prompts:all")

    if cache:
        return json.loads(cache)
    result = await db.execute(select(Prompt))
    prompts = result.scalars().all()
    data = [p.to_dict() for p in prompts]

    redis_client.setex(
        "prompts.all",
        60,
        json.dumps(data)
    )
    return data
    

@router.get("/user/{user_id}")
async def get_user_prompts(user_id:int,db:AsyncSession = Depends(get_db)):
    cache_key = f"prompts:user:{user_id}"

    cache = redis_client.get(cache_key)

    if cache:
        return json.loads(cache)
    result = await db.execute(select(Prompt).where(Prompt.user_id == user_id))
    prompts = result.scalars().all()

    data = [p.to_dict() for p in prompts]
    redis_client.setex(cache_key,60,json.dumps(data))

    return data


@router.post("/")
async def create_prompt(
    promt: PromptCreate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)

):

    prompt = Prompt(
        user_id = current_user.id,
        text=promt.text
    )

    db.add(prompt)
    await db.commit()

    redis_client.delete(f"prompts:user:{current_user.id}")
    redis_client.delete("prompts:all")

    return {"message": "prompt created"}