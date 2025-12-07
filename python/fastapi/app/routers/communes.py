from fastapi import APIRouter
import importlib
from app.datafiles.models import Commune

router=APIRouter()

@router.get("/communes/{province_id}", tags=["communes"])
async def read_communes(province_id: int):
    commune_module=importlib.import_module("app.datafiles.communes."+str(province_id),"app.datafiles")
    response_list=[Commune(id=-1, unitCode=None, name="-- Chọn Xã / Phường --", parentId=None, type=2)]
    response_list.append(commune_module.response_list)
    return response_list