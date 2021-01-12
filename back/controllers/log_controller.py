#from back.dao_txt.log_dao_txt import save_log, read_log
from back.dao.log_dao import create_log_db, list_logs_db

def create_log(action: str, element: str) -> None:
    create_log_db(action, element)

def list_log() -> list:
    logs = list_logs_db()
    return logs
    
