import sys
sys.path.append('')


from back.controllers.base_controller import BaseController
from back.dao.marketplace_dao import MarketplaceDao


class MarketplaceController(BaseController):
    def __init__(self):
        self.__dao = MarketplaceDao()
        super().__init__(self.__dao)
