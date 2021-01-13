#from back.dao_txt.product_dao_txt import save_product, read_products
from back.dao.product_dao import create_product_db, list_products_db
from back.controllers.log_controller import create_log


def create_product(name: str, description: str, price: float ):
    create_product_db(name, description, price)
    create_log('register', 'product')

def list_products():
    products = list_products_db()
    create_log('list', 'product')
    return products
    
