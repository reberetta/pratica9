import sys
sys.path.append('')

#from back.dao_txt.log_dao_txt import save_log, read_log
from back.controllers.base_controller import BaseController
from back.dao.log_dao import LogDao

# def create_log(log:Log) -> None:
#     create_log_db(log)

# def list_log() -> list:
#     logs = list_logs_db()
#     return logs
    
class LogController(BaseController):
    def __init__(self):
        self.__dao = LogDao()
        super().__init__(self.__dao)