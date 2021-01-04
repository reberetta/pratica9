import sys
sys.path.append('back')
from historico import salvar_historico

class Produto:
    
    
    def cadastrar_produto(self, nome:str, descricao:str, preco:float ):
        arq = open('back/produto/produtos.txt', 'a')
        arq.write(f'{nome};{descricao};{preco}\n')
        arq.close()
        salvar_historico('Cadastrar Produto') 
