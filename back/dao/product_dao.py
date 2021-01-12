import sys
sys.path.append('')

import psycopg2
from back.dao.config import _connection_string


def create_product_table():
    conn = psycopg2.connect(_connection_string)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE if not exists sellers(
    id serial NOT NULL,
	nome varchar(100) NOT NULL,
	descricao varchar(200) NULL,
	preco money NOT NULL,
	CONSTRAINT produtos_pk PRIMARY KEY (id));""")
    conn.commit()
    cursor.close()
    conn.close()

def create_product_db(name: str, description: str, price: float) -> None:
    create_product_table()  
    conn = psycopg2.connect(_connection_string)
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO produtos (nome, descricao, preco) VALUES('{name}', '{description}', '{price}');")
    conn.commit()
    cursor.close()
    conn.close()

def list_products_db() -> list:
    products = []

    conn = psycopg2.connect(_connection_string)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM produtos')
    result = cursor.fetchall()
    for item in result:
        products.append({'name': item[1], 'description': item[2], 'price':item[3]})
    cursor.close()
    conn.close()
    return products
    