import os
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_sessionmaker
)
from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv
load_dotenv()

DatabaseURL = os.getenv("DATABASE_URL")
if not DatabaseURL:
    raise ValueError("DATABASE_URL is not set")

engine = create_async_engine(DatabaseURL, echo=True,future=True)
AsyncSessionLocal = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()

Base = declarative_base()