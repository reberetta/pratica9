import sys
sys.path.append('')

#from back.dao_txt.product_dao_txt import save_product, read_products
# from back.dao.product_dao import create_product_db, list_products_db
# from back.controllers.log_controller import create_log
# from back.models.product import Product
# from back.models.log import Log
from back.controllers.base_controller import BaseController
from back.dao.product_dao import ProductDao

# def create_product(product:Product)->None:
#     create_product_db(product)
    
#     log = Log(acao='register', elemento='produtct')
#     create_log(log)

# def list_products()->list:
#     products = list_products_db()

#     log = Log(acao='list', elemento='product')
#     create_log(log)
#     return products
    
class ProductController(BaseController):
    def __init__(self):
        self.__dao = ProductDao()
        super().__init__(self.__dao)