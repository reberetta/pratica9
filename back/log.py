from datetime import datetime


file_path = 'logs/log.txt'

current_time = datetime.now()
datetime_brazil_format = current_time.strftime('%H:%M:%S - %d/%m/%Y')

def register_log(action: str, element: str) -> None:
    file = open(file_path,'a')
    file.write(f'{datetime_brazil_format};{action};{element}\n')
    file.close()

def read_log() -> list:
    file_rows = []
    file = open(file_path, 'r')

    for line in file:
        file_rows.append(line)
    file.close()

    return file_rows
