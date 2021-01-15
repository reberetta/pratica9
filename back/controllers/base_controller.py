class BaseController:
    def __init__(self, dao):
        self.__dao = dao

    def create(self, model: object)->None:
        return self.__dao.create(model)

    def read_by_id(self,id_:int)-> object:
        return self.__dao.read_by_id(id_)

    def read_all(self)->list:
        return self.__dao.read_all()

    def delete(self, id_:int)->None:
        self.__dao.delete(id_)

    def update(self, model: object)->None:
        self.__dao.update(model)