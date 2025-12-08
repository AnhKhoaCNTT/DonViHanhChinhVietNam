from fastapi import FastAPI
from app.routers import communes_and_wards
from app.routers import provinces_and_cities

app=FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(provinces_and_cities.router)
app.include_router(communes_and_wards.router)