from historico import salvar_historico


file_path = "logs/sellers.txt"


def register_seller(name: str, email: str, telephone: str) -> None:
    file = open(file_path, 'a')
    file.write(f'{name};{email};{telephone}\n')
    file.close()
    salvar_historico('Cadastrar Seller') 


def list_sellers() -> list:
    products_rows = []
    file = open(file_path, 'r')

    for line in file:
        treated_line = line.strip().split(';')
        products_rows.append(treated_line)
    file.close()
    salvar_historico('Listar Seller') 

    return products_rows
