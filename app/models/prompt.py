from sqlalchemy import Integer,String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base

class Prompt(Base):

    __tablename__ = "prompts"

    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    user_id:Mapped[int] = mapped_column(ForeignKey("users.id"))
    text:Mapped[str] = mapped_column(String)


    def to_dict(self):
        return {
            "id":self.id,
            "user_id":self.user_id,
            "text": self.text
        }