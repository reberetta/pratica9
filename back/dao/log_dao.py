import sys
sys.path.append('')

import psycopg2
from back.dao.config import _connection_string
from datetime import datetime

def current_date() -> str:
    data_atual = datetime.now()
    data_completa = data_atual.strftime("%d/%m/%Y %H:%M:%S")
    return data_completa


def create_log_table():
    conn = psycopg2.connect(_connection_string)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE if not exists logs(
    id serial NOT NULL,
	data_do_registro timestamp NOT NULL,
	acao varchar(100) NOT NULL,
	elemento varchar(100) NOT NULL,
	CONSTRAINT logs_pk PRIMARY KEY (id));""")
    conn.commit()
    cursor.close()
    conn.close()

def create_log_db(action: str, element: str) -> None:
    create_log_table()  
    conn = psycopg2.connect(_connection_string)
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO logs (data_do_registro, acao, elemento) VALUES('{current_date()}', '{action}', '{element}');")
    conn.commit()
    cursor.close()
    conn.close() 


def list_logs_db() -> list:
    logs = []

    conn = psycopg2.connect(_connection_string)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM logs')
    result = cursor.fetchall()
    for item in result:
        logs.append({'datetime_brazil_format': item[1], 'action': item[2], 'element': item[3]})
    cursor.close()
    conn.close()
    return logs