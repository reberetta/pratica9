import sys
sys.path.append('')

import psycopg2
from back.dao.config import _connection_string


def create_marketplaces_table():
    conn = psycopg2.connect(_connection_string)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE if not exists marketplaces(
    id serial NOT NULL,
	nome varchar(100) NOT NULL,
	descricao varchar(200) NULL,
	CONSTRAINT marketplaces_pk PRIMARY KEY (id));""")
    conn.commit()
    cursor.close()
    conn.close()

def create_marketplace_db(name: str, description: str) -> None:
    create_marketplaces_table()  
    conn = psycopg2.connect(_connection_string)
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO public.marketplaces (nome, descricao) VALUES('{name}', '{description}');")
    conn.commit()
    cursor.close()
    conn.close() 


def list_marketplaces_db() -> list:
    marketplaces = []

    conn = psycopg2.connect(_connection_string)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM marketplaces')
    result = cursor.fetchall()
    for item in result:
        marketplaces.append({'name': item[1], 'description': item[2]})
    cursor.close()
    conn.close()
    return marketplaces