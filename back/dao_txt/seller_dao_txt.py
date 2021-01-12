from back.controllers.log_controller import create_log


file_path = 'back/data/sellers.txt'

def save_seller(name: str, email: str, telephone: str) -> None:
    file = open(file_path, 'a')
    file.write(f'{name};{email};{telephone}\n')
    file.close()
    create_log('register', 'seller') 


def read_sellers() -> list:
    sellers_rows = []
    file = open(file_path, 'r')

    for line in file:
        treated_line = line.strip().split(';')
        sellers_rows.append(({'name': treated_line[0], 'email': treated_line[1], 'telephone': treated_line[2]}))
    file.close()
    create_log('list', 'seller') 

    return sellers_rows

