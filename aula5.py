try:
    #nome_arq = input('Entre com o nome do arquivo: ')
    nome_arq = 'sinopse_mochileiros.txt'
    with open(nome_arq, "r", encoding="utf-8") as arq:    
        palavras_texto = []
        sentencas_texto = []
        for i,linha in enumerate(arq,1):
            #print(linha)
            #print(f'Linha {i} contem a string\n{linha}')                
            palavras_linha = linha.split(' ')
            sentencas_linha = linha.split('.')
            
            for palavra in palavras_linha:
                palavras_texto.append(palavra.replace('\n', ''))
            
            for sentenca in sentencas_linha:
                sentencas_texto.append(sentenca)
    
    palavras_texto.remove('')
    sentencas_texto.remove('\n')
    print(palavras_texto)
    print(sentencas_texto)
    print('O numero total de palavras do texto eh:', len(palavras_texto))
    print('O numero de sentenças do texto eh:', len(sentencas_texto))

    ## Vamos gerar o arquivo invertido aqui

except FileNotFoundError:
    print('Arquivo nao existe')