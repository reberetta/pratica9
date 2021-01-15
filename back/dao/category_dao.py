import sys
sys.path.append('')

from back.dao.base_dao import BaseDao 
from back.models.category import Category
from .connection import Connection 

class CategoryDao(BaseDao):
    def get_type(self):
        return 'product'

    def create_category_table() -> None:
        query = """
                CREATE TABLE if not exists categorias(
                id serial NOT NULL,
                nome varchar(100) NOT NULL,
                descricao varchar(200) NULL,
                CONSTRAINT categorias_pk PRIMARY KEY (id));"""
        super().execute(query)
        


    def create(self, model: Category) -> list:
        query = (f"""INSERT INTO categorias
                        (nome, descricao) 
                        VALUES
                        ('{model.nome}', '{model.descricao}');""")
        super().execute(query)


    def read_by_id(self, id_:int)-> Category:
        query = f"SELECT ID, nome, descricao FROM categorias WHERE ID = {id_};"
        result = super().read(query)[0]
        return Category(nome=result[1], descricao=result[2], id_=result[0])


    def read_all(self)->list:
        query = f"SELECT ID, nome, descricao FROM categorias;"
        results = super().read(query)
        categories = []
        for result in results:
            categories.append(Category(nome=result[1], descricao=result[2], id_=result[0]))
        return categories


    def update(self, model:Category)->None:
        query = f"""UPDATE CATEGOrias
                            SET nome = '{model.nome}', descricao = '{model.descricao}' 
                            WHERE ID = {model.id_};
                            """
        super().execute(query)


    def delete(self, id_:int)->None:
        print(id_)
        query = f"DELETE FROM CATEGORias WHERE ID = {id_};"
        super().execute(query)
