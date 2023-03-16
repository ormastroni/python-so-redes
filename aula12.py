import threading, time

class CalculoNumerico(threading.Thread):
    def __init__(self, nome, base, potencia):
        threading.Thread.__init__(self)
        self._base = base
        self._potencia = potencia
        self._nome = nome

    def faz_alguma_coisa():
        pass

    def eleva_quadrado():
        pass

    def potencia():
        pass
    
    def run(self):
        print(self._nome)
        resultado = self._base
        for i in range(self._potencia-1):
            resultado *= self._base
        print(resultado)
    
lista = [2,3,4,5]

t1 = CalculoNumerico('quadrado', 4,2)
t2 = CalculoNumerico('cubo', 2,3)

tini = time.time()

t1.start()
t2.start()

t1.join()
t2.join()

tfim = time.time()

print('realizado em ', tfim-tini)