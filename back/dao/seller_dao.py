import sys
sys.path.append('')

import psycopg2
from back.dao.config import _connection_string


def create_sellers_table():
    conn = psycopg2.connect(_connection_string)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE if not exists sellers(
    id serial NOT NULL,
	nome varchar(100) NOT NULL,
	email varchar(50) NOT NULL,
	telefone varchar(20) NOT NULL,
	CONSTRAINT sellers_pk PRIMARY KEY (id));""")
    conn.commit()
    cursor.close()
    conn.close()

def create_sellers_db(name: str, email: str, telephone: str) -> None:
    create_sellers_table()  
    conn = psycopg2.connect(_connection_string)
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO sellers(nome, email, telefone) VALUES('{name}', '{email}', '{telephone}');")
    conn.commit()
    cursor.close()
    conn.close()

def list_sellers_db() -> list:
    sellers = []

    conn = psycopg2.connect(_connection_string)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM sellers')
    result = cursor.fetchall()
    for item in result:
        sellers.append({'name': item[1], 'email': item[2], 'telephone':item[3]})
    cursor.close()
    conn.close()
    return sellers