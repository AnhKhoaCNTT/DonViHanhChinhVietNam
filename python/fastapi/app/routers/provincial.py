from fastapi import APIRouter
from app.data.models import ProvinceOrCity
from app.data.service.providers import ProvincialService

router=APIRouter()

@router.get("/provincialUnits/", tags=["provinces_and_cities"])
async def read_all():
    responses=[ProvinceOrCity(id=-1, unitCode=None, name="-- Chọn Tỉnh / Thành phố --", type=1)]
    responses.append(ProvincialService.read_all())
    return responses