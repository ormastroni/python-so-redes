import multiprocessing, time
from random import randint

def eleva_quadrado(fila1, fila2, ini, fim):
    result = []
    lista = fila1.get()
    for n in lista:
        result.append(n*n)
    fila2.put([ini, fim, result])
        
if (__name__ == "__main__"):

    lista = []

    print('Geração de números aleatórios...')
    TAM_LISTA = 100
    for i in range(TAM_LISTA):
        lista.append(randint(1,50))
    
    fila_entrada = multiprocessing.Queue()
    fila_saida = multiprocessing.Queue()

    N_PROCESSOS = 4
    lista_processos = []
    tini = time.time()

    fila_entrada.put(lista[0:25])
    fila_entrada.put(lista[25:50])
    fila_entrada.put(lista[50:75])
    fila_entrada.put(lista[75:100])

    p1 = multiprocessing.Process(target=eleva_quadrado, args=(fila_entrada, fila_saida, 0, 25))
    p2 = multiprocessing.Process(target=eleva_quadrado, args=(fila_entrada, fila_saida, 25, 50))
    p3 = multiprocessing.Process(target=eleva_quadrado, args=(fila_entrada, fila_saida, 50, 75))
    p4 = multiprocessing.Process(target=eleva_quadrado, args=(fila_entrada, fila_saida, 75, 100))

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()

    
    '''for i in range(N_PROCESSOS):
        ini = i * (TAM_LISTA//N_PROCESSOS)
        fim = (i+1) * (TAM_LISTA//N_PROCESSOS)
        fila_entrada.put(lista[ini:fim])
        print(f'Criação dos processo {i}...')
        p = multiprocessing.Process(target=eleva_quadrado, args=(fila_entrada, fila_saida, ini, fim))
        p.start()
        lista_processos.append(p)'''
    
    #print('Esperando os processos terminarem...')
    '''for p in lista_processos:
        p.join()  '''  
    
    print('Lista original')
    print(lista[0:25])
    print(lista[25:50])
    print(lista[50:75])
    print(lista[75:100])

    print('Pegando os resultados da fila de saída...')
    for i in range(N_PROCESSOS):
        [ini, fim, lista_quadrado] = fila_saida.get()
        print(f'Processo ({ini}, {fim}) gerou a lista {lista_quadrado}')
    
    tfim = time.time()

    print('realizado em ', tfim-tini)