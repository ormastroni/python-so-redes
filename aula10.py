import threading, time

resultado_quadrado = []
resultado_cubo = []

def eleva_quadrado(lista):
    global resultado_quadrado
    for n in lista:
        time.sleep(1)
        resultado_quadrado.append(n*n)
    
def eleva_cubo(lista):
    #global resultado_cubo
    for n in lista:
        time.sleep(1)
        resultado_cubo.append(n*n*n)        
    
lista = [2,3,4,5,6]

t1 = threading.Thread(target=eleva_quadrado, args=(lista,))
t2 = threading.Thread(target=eleva_cubo, args=(lista,))

tini = time.time()

#eleva_quadrado(lista)
#eleva_cubo(lista)

t1.start()
t2.start()

t1.join()
t2.join()

tfim = time.time()

print('realizado em ', tfim-tini)
print(resultado_quadrado)
print(resultado_cubo)