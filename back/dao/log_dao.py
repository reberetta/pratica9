import sys
sys.path.append('')

# import psycopg2
from datetime import datetime
from back.models.log import Log
from .base_dao import BaseDao


class LogDao(BaseDao):

    def get_type(self):
        return 'log'

    def create_log_table(self)->None:
        query = """
            CREATE TABLE if not exists logs(
            id serial NOT NULL,
            data_do_registro timestamp NOT NULL,
            acao varchar(100) NOT NULL,
            elemento varchar(100) NOT NULL,
            CONSTRAINT logs_pk PRIMARY KEY (id));"""
        super().execute(query)

    def create(self, log:Log) -> None:
        self.create_log_table() 
        query = f"INSERT INTO logs (data_do_registro, acao, elemento) \
                  VALUES('{log.data_do_registro}', '{log.acao}', '{log.elemento}');"
        super().execute(query)
        

    def read_all(self) -> list:
        query = 'SELECT data_do_registro, acao, elemento, id FROM logs'
        results = super().read(query)
        logs = []
        for log in results:
            logs.append(Log(data_do_registro=log[0], acao=log[1],
                        elemento=log[2], id_=log[3]))
               
        return logs

    def read_by_id(self, id_:int) -> list:
        query = 'SELECT data_do_registro, acao, elemento, id FROM logs WHERE id = {id_}'
        result = super().read(query)[0]
        return Log(data_do_registro=result[0], acao=result[1],
                        elemento=result[2], id_=result[3])
               
    
    def update(self, log:Log)->None:
        query = f"""UPDATE logs 
                            SET 
                                acao = '{log.acao}',
                                elemento = '{log.elemento}' 
                            WHERE id = {log.id_};
                            """
        super().execute(query)

        
    def delete(self, id_:int)->None: 
        query = f"DELETE FROM logs where ID = {id_};"
        super().execute(query)
        