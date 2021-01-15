import sys
sys.path.append('')

#from back.controllers.base_controller import BaseController
from back.dao.log_dao import LogDao

    
class LogController:
    def __init__(self):
        self.__dao = LogDao()
        