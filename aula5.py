try:
    arq = open("sinopse.txt", "r", encoding="utf-8")
    saida = open('sinopse_invertida.txt', "w", encoding="utf-8")

    palavras_texto = []
    for i, linha in enumerate(arq,1):
        #print(linha)
        #print(f'Linha {i} contem a string\n{linha}')
        palavras_linha = linha.split(' ')
        for palavra in palavras_linha:
            palavras_texto.append(palavra.replace('\n', ''))
    
    arq.close()
    palavras_texto.remove('')
    print(palavras_texto)

    ## Vamos gerar o arquivo invertido aqui
    
except FileNotFoundError:
    print('Arquivo nao existe')