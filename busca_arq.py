import os

def busca_arquivo(nome, dir):
    try:
        l = os.listdir(dir)
        for i in l:
            if os.path.isfile(i) and i == nome:
                return True
        return False    
    except FileNotFoundError:
        print('Diretorio nao existe')
        return False
    

nome_arq = input("Entre com o nome do arquivo: ")
nome_dir = input("Entre com o nome do diretório: ")

if busca_arquivo(nome_arq, nome_dir):
    print(nome_arq, "foi encontrado em", nome_dir)
else:
    print(nome_arq, "não foi encontrado em", nome_dir)
