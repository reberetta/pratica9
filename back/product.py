from log import register_log


file_path = "logs/products.txt"


def register_product(name: str, description: str, price: float ):
    file = open(file_path, 'a')
    file.write(f'{name};{description};{price}\n')
    file.close()
    register_log('register', 'product')

def list_products():
    products_rows = []
    file = open(file_path, 'r')

    for line in file:
        treated_line = line.strip().split(';')
        products_rows.append(treated_line)
    file.close()
    register_log(file_path, 'product')

    return products_rows
