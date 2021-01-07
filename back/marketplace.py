from log import register_log
mkp_file = "logs/marketplace.txt"


def salvar_arquivo(caminho:str,linha:str) -> None:
    arquivo = open(caminho, 'a', encoding='utf-8')
    arquivo.write(f'{linha}\n')
    arquivo.close()


def add_new_marketplace(name:str, desc:str)->None:  
    if isinstance(name, str) and isinstance(desc, str): 
        linha = f'{name};{desc}'
        salvar_arquivo(mkp_file,linha)
    register_log('register', 'Marketplace') 


def list_marketplaces() -> list:
    marketplaces = []

    with open(mkp_file, 'r', encoding='utf-8') as marketplaces_file:
        for line in marketplaces_file:
            result = line.strip().split(';')
            marketplaces.append({'name': result[0], 'description': result[1]})

    register_log('list', 'marketplaces')   
    return marketplaces
