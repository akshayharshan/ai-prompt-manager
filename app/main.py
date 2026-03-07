from fastapi import FastAPI

from app.routes.auth import router as auth_router
from app.routes.prompts import router as prompt_roter

app = FastAPI(title="AI Prompt Manager API")

@app.get("/")
async def root():
    return {"message": "AI Prompt Manager Running"}
app.include_router(auth_router)
app.include_router(prompt_roter)