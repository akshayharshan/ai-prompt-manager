from fastapi import HTTPException,Request
from app.core.redis import redis_client


RATE_LIMIT =5
WINDOW = 60

async def rate_limit(request: Request):
    ip = request.client.host

    key = f"rate_limit:{ip}"
    current = redis_client.get(key)

    if current and int(current) >= RATE_LIMIT:
        raise HTTPException(
            status_code=429,
            detail="Too many request"
        )

    redis_client.incr(key)

    redis_client.expire(key,WINDOW)