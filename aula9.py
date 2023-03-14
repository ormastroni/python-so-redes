import threading, time

def minhaFunc(i):
    print('ola mundo da thread ', i)
    ## Processa o valor i
    time.sleep(1)
    
a = 1
b = 2
c = 3
d = 4

'''t1 = time.time()
minhaFunc(a)
minhaFunc(b)
minhaFunc(c)
minhaFunc(d)
t2 = time.time()'''

#print(f'Tempo de execução {t2-t1} segundos')

tempo1 = time.time()

t1 = threading.Thread(target=minhaFunc, args=(a,))
t2 = threading.Thread(target=minhaFunc, args=(b,))
t3 = threading.Thread(target=minhaFunc, args=(c,))
t4 = threading.Thread(target=minhaFunc, args=(d,))

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()

tempo2 = time.time()
print(f'Tempo de execução {tempo2-tempo1} segundos')