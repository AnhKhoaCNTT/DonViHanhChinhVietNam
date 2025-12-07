from fastapi import FastAPI, APIRouter
from app.routers import provinces, communes

app=FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(provinces.router)
app.include_router(communes.router)