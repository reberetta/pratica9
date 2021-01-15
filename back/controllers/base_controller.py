from back.models.log import Log
from back.controllers.log_controller import LogController
from back.dao.log_dao import LogDao

class BaseController:
    dao:object
    def __init__(self, dao):
        self.dao = dao

    @property
    def dao(self)->object:
        return self.__dao
    
    @dao.setter
    def dao(self, dao)->None:
        self.__dao = dao

    def create(self, model: object)->None:
        if not self.dao.get_type() == "log":
            log = Log(acao="create", elemento=self.dao.get_type())
            LogDao().create(log)
        return self.__dao.create(model)

    def read_by_id(self,id_:int)-> object:
        if not self.dao.get_type() == "log":
            log = Log(acao="read_by_id", elemento=self.dao.get_type())
            LogDao().create(log)
        return self.__dao.read_by_id(id_)

    def read_all(self)->list:
        if not self.dao.get_type() == "log":
            log = Log(acao="read_all", elemento=self.dao.get_type())
            LogDao().create(log)
        return self.__dao.read_all()

    def delete(self, id_:int)->None:
        if not self.dao.get_type() == "log":
            log = Log(acao="delete", elemento=self.dao.get_type())
            LogDao().create(log)
        
        self.__dao.delete(id_)

    def update(self, model: object)->None:
        if not self.dao.get_type() == "log":
            log = Log(acao="update", elemento=self.dao.get_type())
            LogDao().create(log)
        
        self.__dao.update(model)
