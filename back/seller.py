from log import register_log


file_path = "logs/sellers.txt"


def register_seller(name: str, email: str, telephone: str) -> None:
    file = open(file_path, 'a')
    file.write(f'{name};{email};{telephone}\n')
    file.close()
    register_log('register', 'seller') 


def list_sellers() -> list:
    products_rows = []
    file = open(file_path, 'r')

    for line in file:
        treated_line = line.strip().split(';')
        products_rows.append({'name': treated_line[0], 'email': treated_line[1], 'telephone': treated_line[2]})
    file.close()
    register_log('list', 'seller') 

    return products_rows
