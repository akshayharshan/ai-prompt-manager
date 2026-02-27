from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base

class User(Base):
    __tablename__ = "users"
    id:Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    email:Mapped[str] = mapped_column(String(255), unique=True, index=True)
    hash_password:Mapped[str] = mapped_column(String(255))