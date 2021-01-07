import sys
sys.path.append('back')
from log import register_log


def cadastrar_produto(nome:str, descricao:str, preco:float ):
    arq = open('back/produto/produtos.txt', 'a')
    arq.write(f'{nome};{descricao};{preco}\n')
    arq.close()
    register_log('register', 'product')


def list_products():
    products_rows = []
    file = open('back/produto/produtos.txt', 'r')

    for line in file:
        treated_line = line.strip().split(';')
        products_rows.append(treated_line)
    file.close()
    register_log('list', 'product')

    return products_rows
