from fastapi import APIRouter
from app.data.models import ProvinceOrCity
from app.data.service.provinces_and_cities import ProvinceAndCityService

router=APIRouter()

@router.get("/provincesAndCities/", tags=["provinces_and_cities"])
async def read_all():
    responses=[ProvinceOrCity(id=-1, unitCode=None, name="-- Chọn Tỉnh / Thành phố --", type=1)]
    responses.append(ProvinceAndCityService.read_all())
    return responses