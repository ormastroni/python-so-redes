import threading, time

def potencia(a,b):
    resultado = 1
    for i in range(b):
        resultado = resultado * a
    print(f'potencia de {a} por {b} eh {resultado}')
    
def fatorial(n):
    if (n == 1):
        return 1
    return n*fatorial(n-1)
    

t1 = threading.Thread(target=potencia, args=(2,3))
t2 = threading.Thread(target=fatorial, args=(10,))

tini = time.time()

t1.start()
t2.start()

t1.join()
t2.join()

tfim = time.time()

print('realizado em ', tfim-tini)