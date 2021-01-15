import sys
sys.path.append('')

from back.models.marketplace import Marketplace
from .base_dao import BaseDao

class MarketplaceDao(BaseDao):
    def get_type(self):
        return 'marketplace'
    
    def create_marketplaces_table(self):
        query = """
                    CREATE TABLE if not exists marketplaces(
                    id serial NOT NULL,
                    nome varchar(100) NOT NULL,
                    descricao varchar(200) NULL,
                    CONSTRAINT marketplaces_pk PRIMARY KEY (id));"""
        super().execute(query)

    def create(self, marketplace:Marketplace) -> None:
        self.create_marketplaces_table()
        query = f"INSERT INTO public.marketplaces (nome, descricao) \
                        VALUES('{marketplace.nome}', '{marketplace.descricao}');"
        super().execute(query)

    def read_all(self) -> list:
        query = 'SELECT id, nome, descricao FROM marketplaces'
        results =  super().read(query)
        
        marketplaces = []
        for result in results:
            marketplaces.append(Marketplace(id_=result[0], nome=result[1], descricao=result[2]))
        return marketplaces
                

    def read_by_id(sefl, id_:int)-> Marketplace:
        query = f'SELECT id, nome, descricao from marketplaces where id = {id_}'
        result =  super().read(query)[0]
        return Marketplace(id_=result[0], nome=result[1], descricao=result[2])

    def update(self, marketplace:object)->None:
        query = f"""UPDATE CATEGORY 
                            SET 
                                nome = '{marketplace.nome}',
                                descricao = '{marketplace.descricao}' 
                            WHERE id = {marketplace.id_};
                            """
        super().execute(query)


    def delete(self, id_:int) -> list:
        query = f'DELETE FROM marketplaces where id = {id_}'
        super().execute(query)
