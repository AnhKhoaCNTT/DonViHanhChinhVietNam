from fastapi import APIRouter
import importlib
from app.data.models import CommuneOrWard

router=APIRouter()

@router.get("/communesAndWards/{province_or_city_id}", tags=["communes_and_wards"])
async def read_communes(province_or_city_id: int):
    CommunesAndWardsService=importlib.import_module("app.data.service.communes_and_wards."+str(province_or_city_id),"app.data.service.communes_and_wards").CommunesAndWardsService
    responses=[CommuneOrWard(id=-1, unitCode=None, name="-- Chọn Xã / Phường --", parentId=None, type=2)]
    responses.append(CommunesAndWardsService.read_all())
    return responses