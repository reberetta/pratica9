import sys
sys.path.append('')

#from back.dao_txt.category_dao_txt import save_category, read_categories
from back.dao.category_dao import create_category_db, list_categories_db
from back.controllers.log_controller import create_log


def create_category(name: str, description: str) -> None:  
    create_category_db(name, description)
    create_log('register', 'category') 

def list_categories() -> list:
    categories = list_categories_db()
    create_log('list', 'category') 
    return categories

