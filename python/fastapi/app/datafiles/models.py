class Province:
    def __init__(self, id: int, unitCode: str, name: str, type: int=1):
        self.id=id
        self.unitCode=unitCode
        self.name=name
        #self.parentId=None
        self.type=type
        #self.isUsed=True

class Commune:
    def __init__(self, id: int, unitCode: str, name: str, parentId: int, type: int=2):
        self.id=id
        self.unitCode=unitCode
        self.name=name
        self.parentId=parentId
        self.type=type
        #self.isUsed=True