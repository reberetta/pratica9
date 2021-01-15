import sys
sys.path.append('')
from back.controllers.base_controller import BaseController
from back.dao.product_dao import ProductDao


class ProductController(BaseController):
    def __init__(self):
        self.__dao = ProductDao()
        super().__init__(self.__dao)