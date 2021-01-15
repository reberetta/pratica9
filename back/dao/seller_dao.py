import sys
sys.path.append('')

#import psycopg2
#from back.dao.config import _connection_string
from back.dao.base_dao import BaseDao
from back.dao.base_dao import Connection
from back.models.seller import Seller


class SellerDao(BaseDao):

    def create_sellers_table() -> None:
        query = """
        CREATE TABLE if not exists sellers(
        id serial NOT NULL,
        nome varchar(100) NOT NULL,
        email varchar(50) NOT NULL,
        telefone varchar(20) NOT NULL,
        CONSTRAINT sellers_pk PRIMARY KEY (id));"""
        super().execute(query)


    def create(self, model: Seller) -> None:
        query = (f"""INSERT INTO sellers
                    (nome, email, telefone) 
                    VALUES
                    ('{model.nome}', '{model.email}', '{model.telefone}');""")
        super().execute(query)

    
    def read_by_id(self, id_:int)-> Seller:
        query = f"""SELECT nome, email, telefone, ID FROM sellers WHERE ID={id_};"""
        result = super().read(query)[0]
        return Seller(id_=result[3], nome=result[0], email=result[1], telefone=result[2])


    def read_all(self)-> list:
        sellers = []
        query = f"""SELECT id, nome, email, telefone FROM sellers;"""
        list_result = super().read(query)
        for result in list_result:
            sellers.append(Seller(id_=result[0], nome=result[1], email=result[2], telefone=result[3]))
        return sellers


    def update(self, model:Seller)-> None:
        query = f"""UPDATE sellers 
                    SET
                        nome = '{model.nome}', 
                        telefone = '{model.telefone}', 
                        email = '{model.email}'
                    WHERE ID = {model.id_};"""
        super().execute(query)


    def delete(self, id_:int)-> None:
        query = f"DELETE FROM sellers WHERE ID={id_};"
        super().execute(query)


