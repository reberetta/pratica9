from datetime import datetime


file_path = 'back/data/log.txt'

current_time = datetime.now()
datetime_brazil_format = current_time.strftime('%H:%M:%S - %d/%m/%Y')

def save_log(action: str, element: str) -> None:
    file = open(file_path,'a')
    file.write(f'{datetime_brazil_format};{action};{element}\n')
    file.close()

def read_log() -> list:
    file_rows = []
    file = open(file_path, 'r')

    for line in file:
        treated_line = line.strip().split(';')
        file_rows.append({'date': treated_line[0], 'action': treated_line[1], 'element': treated_line[2]})
    file.close()

    return file_rows