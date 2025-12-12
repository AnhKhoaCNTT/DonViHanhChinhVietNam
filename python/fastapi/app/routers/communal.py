from fastapi import APIRouter
from app.data.service.providers import CommunalService
from app.data.models import CommuneOrWard

router=APIRouter()

@router.get("/communalUnits/{parent_id}", tags=["Communal units"])
async def read_communes(parent_id: int):
    responses=[CommuneOrWard(id=-1, unitCode=None, name="-- Chọn Xã / Phường --", parentId=None, type=2)]
    responses.append(CommunalService.read_all(parent_id=parent_id))
    return responses