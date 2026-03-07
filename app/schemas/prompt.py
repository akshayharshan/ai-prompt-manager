from pydantic import BaseModel


class PromptCreate(BaseModel):
    text:str