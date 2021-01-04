from datetime import datetime

caminho = 'logs/historico.txt'

def salvar_historico(linha:str) -> None:
    arquivo = open(caminho,'a')
    data_e_hora_atuais = datetime.now()
    data_e_hora_em_texto = data_e_hora_atuais.strftime('%H:%M:%S - %d/%m/%Y')
    arquivo.write(f'{data_e_hora_em_texto} - {linha}\n')
    arquivo.close()

def ler_historico() -> list:
    lista_linhas_arquivo = []
    arquivo = open(caminho, 'r')
    for linha in arquivo:
        lista_linhas_arquivo.append(linha)
    arquivo.close()
    return lista_linhas_arquivo