import sys
sys.path.append('')

#from back.dao_txt.seller_dao_txt import save_seller, read_sellers
from back.dao.seller_dao import create_sellers_db, list_sellers_db
from back.controllers.log_controller import create_log


def create_seller(name: str, email: str, telephone: str) -> None:
    create_sellers_db(name, email, telephone)
    create_log('register', 'seller')

def list_sellers() -> list:
    sellers = list_sellers_db()
    create_log('list', 'seller')
    return sellers
    
    