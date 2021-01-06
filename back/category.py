from historico import salvar_historico
category_txt = "logs/categories.txt"


def salvar_arquivo(caminho: str, linha: str) -> None:
    with open(caminho, 'a', encoding='utf-8'):
        arquivo.write(f'{linha}\n')


def create_category(name: str, description: str) -> None:  
    if isinstance(name, str) and isinstance(desc, str): 
        category = f'{name};{desc}'
        salvar_arquivo(category_txt, category)
    salvar_historico('Cadastrar Categoria') 


def list_categories() -> list:
    categories = []

    with open(category_txt, 'r', encoding='utf-8') as categories_file:
        for line in categories_file:
            result = line.strip().split(';')
            categories.append({'name': result[0], 'description': result[1]})

    salvar_historico('Listar Categorias')   
    return categories