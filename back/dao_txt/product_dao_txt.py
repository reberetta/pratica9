from back.controllers.log_controller import create_log


file_path = "back/data/products.txt"


def save_product(name: str, description: str, price: float ):
    file = open(file_path, 'a')
    file.write(f'{name};{description};{price}\n')
    file.close()
    create_log('register', 'product')

def read_products() -> list:
    products_rows = []
    file = open(file_path, 'r')

    for line in file:
        treated_line = line.strip().split(';')
        products_rows.append(treated_line)
    file.close()
    create_log('list', 'product')

    return products_rows