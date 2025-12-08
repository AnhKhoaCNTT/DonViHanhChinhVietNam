import importlib
from app.data.models import CommuneOrWard, ProvinceOrCity
from app.data.service.provincial import responses

class ProvincialService:
    @staticmethod
    def read_all() -> list[ProvinceOrCity]:
        return responses
    
class CommunalService:
    @staticmethod
    def read_all(parent_id: int) -> list[CommuneOrWard]:
        return importlib.import_module("app.data.service.communal."+str(parent_id)).responses