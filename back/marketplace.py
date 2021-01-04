from historico import salvar_historico
mkp_file = "logs/marketplace.txt"


def salvar_arquivo(caminho:str,linha:str) -> None:
    arquivo = open(caminho,'a')
    arquivo.write(f'{linha}\n')
    arquivo.close()


def add_new_marketplace(name:str, desc:str)->None:  
    if isinstance(name, str) and isinstance(desc, str): 
        linha = f'{name};{desc}'
        salvar_arquivo(mkp_file,linha)
    salvar_historico('Cadastrar Marketplace')    