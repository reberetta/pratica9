import sys
sys.path.append('')

#from back.dao_txt.marketplace_dao_txt import save_marketplace, read_marketplaces
from back.dao.marketplace_dao import create_marketplace_db, list_marketplaces_db
from back.controllers.log_controller import create_log


def create_marketplace(name: str, description: str) -> None:  
    create_marketplace_db(name, description)
    create_log('register', 'marketplace')

def list_marketplaces() -> list:
    marketplaces = list_marketplaces_db()
    create_log('list', 'marketplace')  
    return marketplaces
    
    