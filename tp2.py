import os

## Questão 1
def q1():
    while True:
        try:
            x = int(input('Entre com um numero inteiro: '))
            break
        except ValueError:
            print('Oops... Programa abortado')

def eleva_quadrado(n):
    return n*n

def q2():
    while True:
        try:
            x = int(input('Entre com um numero inteiro: '))
            return eleva_quadrado(x)
        except ValueError:
            print('Oops... Programa abortado')


for item in os.listdir():    
    if (os.path.isfile(item)) and (item == 'xxxx'):
        print('Achei')
        break
    
print('Não achei')
