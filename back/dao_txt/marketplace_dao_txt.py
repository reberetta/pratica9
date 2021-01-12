from back.controllers.log_controller import create_log
mkp_file = "back/data/marketplace.txt"


def salvar_arquivo(caminho:str,linha:str) -> None:
    arquivo = open(caminho, 'a', encoding='utf-8')
    arquivo.write(f'{linha}\n')
    arquivo.close()


def save_marketplace(name:str, description:str)->None:  
    if isinstance(name, str) and isinstance(description, str): 
        linha = f'{name};{description}'
        salvar_arquivo(mkp_file,linha)
    create_log('register', 'Marketplace') 


def read_marketplaces() -> list:
    marketplaces = []

    with open(mkp_file, 'r', encoding='utf-8') as marketplaces_file:
        for line in marketplaces_file:
            result = line.strip().split(';')
            marketplaces.append({'name': result[0], 'description': result[1]})

    create_log('list', 'marketplaces')   
    return marketplaces

