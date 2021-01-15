import sys
sys.path.append('')

from back.controllers.base_controller import BaseController
from back.dao.seller_dao import SellerDao


    
class SellerController(BaseController):
    def __init__(self):
        self.__dao = SellerDao()
        super().__init__(self.__dao)
