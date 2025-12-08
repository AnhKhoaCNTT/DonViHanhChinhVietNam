from fastapi import FastAPI
from app.routers import communal, provincial

app=FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(provincial.router)
app.include_router(communal.router)