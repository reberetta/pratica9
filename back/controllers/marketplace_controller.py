import sys
sys.path.append('')

#from back.dao_txt.marketplace_dao_txt import save_marketplace, read_marketplaces
# from back.dao.marketplace_dao import create_marketplace_db, list_marketplaces_db
# from back.controllers.log_controller import create_log
# from back.models.marketplace import Marketplace
# from back.models.log import Log
from back.controllers.base_controller import BaseController
from back.dao.marketplace_dao import MarketplaceDao

# def create_marketplace(marketplace:Marketplace) -> None:  
#     create_marketplace_db(marketplace)
#     log = Log(acao='register', elemento='marketplace')
#     create_log(log)

# def list_marketplaces() -> list:
#     marketplaces = list_marketplaces_db()
#     log = Log(acao='list', elemento='marketplace')
#     create_log(log)
#     return marketplaces
    
class MarketplaceController(BaseController):
    def __init__(self):
        self.__dao = MarketplaceDao()
        super().__init__(self.__dao)