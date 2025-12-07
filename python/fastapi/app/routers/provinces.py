from fastapi import APIRouter
from app.datafiles.models import Province
from app.datafiles import provinces

router=APIRouter()

@router.get("/provinces/", tags=["provinces"])
async def read_all():
    response_list=[Province(id=-1, unitCode=None, name="-- Chọn Tỉnh / Thành phố --", type=1)]
    response_list.append(provinces.response_list)
    return response_list