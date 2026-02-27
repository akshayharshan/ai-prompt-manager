from fastapi import FastAPI

app = FastAPI(title="AI Prompt Manager API")

@app.get("/")
async def root():
    return {"message": "AI Prompt Manager Running"}