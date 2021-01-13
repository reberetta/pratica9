import sys
sys.path.append('')

import psycopg2
from back.dao.config import _connection_string




def create_category_table():
    conn = psycopg2.connect(_connection_string)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE if not exists categorias(
    id serial NOT NULL,
	nome varchar(100) NOT NULL,
	descricao varchar(200) NULL,
	CONSTRAINT categorias_pk PRIMARY KEY (id));""")
    conn.commit()
    cursor.close()
    conn.close()

def create_category_db(name: str, description: str) -> None:
    create_category_table()  
    conn = psycopg2.connect(_connection_string)
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO categorias(nome, descricao) VALUES('{name}', '{description}');")
    conn.commit()
    cursor.close()
    conn.close() 


def list_categories_db() -> list:
    categories = []

    conn = psycopg2.connect(_connection_string)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM categorias')
    result = cursor.fetchall()
    for item in result:
        categories.append({'name': item[1], 'description': item[2]})
    cursor.close()
    conn.close()
    return categories

