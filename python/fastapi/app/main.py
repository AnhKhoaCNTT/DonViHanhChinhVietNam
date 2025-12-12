from fastapi import FastAPI
from app.routers import communal, provincial

app=FastAPI()

@app.get("/", tags=["Default"])
async def root():
    return {
        "project_name": "Đơn vị hành chính Việt Nam",
        "examples":
        [
            {"http://127.0.0.1:8000/provincialUnits":"Liệt kê tất cả các tên Tỉnh và Thành phố của Việt Nam"},
            {"http://127.0.0.1:8000/communalUnits/12370":"Liệt kê tất cả các Phường và Xã tại Thành phố Hà Nội. Trong đó, 12370 là Id của Thành phố Hà Nội"},
            {"http://127.0.0.1:8000/communalUnits/12401":"Liệt kê tất cả các Phường, Xã và Đặc khu tại Tỉnh An Giang. Trong đó, 12401 là Id của Tỉnh An Giang"}
        ],
        "open_api_documentation":
        [
            {"http://127.0.0.1:8000/docs":"swagger"},
            {"http://127.0.0.1:8000/redoc":"redoc"}
        ]
    }

app.include_router(provincial.router)
app.include_router(communal.router)