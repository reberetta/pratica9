import sys
sys.path.append('')

import psycopg2
from back.models.product import Product
from .base_dao import BaseDao

class ProductDao(BaseDao):

    def create_product_table(self):
        query = """
                    CREATE TABLE if not exists sellers(
                    id serial NOT NULL,
                    nome varchar(100) NOT NULL,
                    descricao varchar(200) NULL,
                    preco money NOT NULL,
                    CONSTRAINT produtos_pk PRIMARY KEY (id));"""
        super().execute(query)

    def create(self, product:Product) -> None:
        self.create_product_table()  
        query = f"""INSERT INTO produtos 
                        (nome, descricao, preco) 
                    VALUES
                        ('{product.nome}', '{product.descricao}', '{product.preco}');"""
        super().execute(query)

    def read_all(self) -> list:
        query = 'SELECT nome, descricao, preco, id FROM produtos'
        results =  super().read(query)
        produtos = []
        for result in results:
            produtos.append(Product(id_=result[3], nome=result[0], descricao=result[1], preco=result[2]))
        return produtos
    
    def read_by_id(self, id_:int)->object:
        query = f"SELECT nome, descricao, preco, id FROM produtos WHERE id = {id_};"
        
        result =  super().read(query)[0]
        
        return Product(id_=result[3], nome=result[0], descricao=result[1], preco=result[2])
        
    def update(self, product:object)->None:
        query = f"UPDATE produtos SET nome = '{model.nome}', descricao = '{model.descricao}', preco = '{model.preco}';"
        super.execute(query)
    
    def delete(self, id_:int) -> None:
        query = f"DELETE FROM produtos WHERE id = {id_};"
        super().execute(query)