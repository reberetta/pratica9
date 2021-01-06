import sys
sys.path.append('back')
from historico import salvar_historico


def cadastrar_produto(nome:str, descricao:str, preco:float ):
    arq = open('back/produto/produtos.txt', 'a')
    arq.write(f'{nome};{descricao};{preco}\n')
    arq.close()
    salvar_historico('Cadastrar Produto') 


def list_products():
    products_rows = []
    file = open('back/produto/produtos.txt', 'r')

    for line in file:
        treated_line = line.strip().split(';')
        products_rows.append(treated_line)
    file.close()
    salvar_historico('Listar Produto') 

    return products_rows
