import threading, time, random

def soma_1(lista, inicio, fim):
    for i in range(inicio,fim):
        lista[i] += 1
    

def eleva_quadrado(lista, inicio, fim):
    arq = open('thread'+str(inicio)+'.txt','w')
    
    arq.write('thread que imprime de ' + str(inicio) + ' ' + str(fim) + '\n')
    for i in range(inicio,fim):
        arq.write('Quadrado de ' + str(lista[i])  + ' eh:' + str(lista[i]*lista[i]) + '\n')
    arq.close()
    
lista = []
lista_threads = []

for i in range(100):
    lista.append(random.randint(1,100))

#print(lista)
tamanho = len(lista)

tini = time.time()

t1 = threading.Thread(target=soma_1, args=(lista,0, int(tamanho/2)))
t2 = threading.Thread(target=soma_1, args=(lista,int(tamanho/2),tamanho))

#t1 = threading.Thread(target=eleva_quadrado, args=(lista,0, int(tamanho/2)))
#t2 = threading.Thread(target=eleva_quadrado, args=(lista,int(tamanho/2),tamanho))

t1.start()
t2.start()

t1.join()
t2.join()

#soma_1(lista, 0, tamanho)

tfim = time.time()

#print(lista)
print(tfim-tini)