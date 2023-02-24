
import os

'''try:
    x = int(input('Entre com o valor da conta: '))
    desc = float(input('Entre com o valor do desconto: '))
    valor_desconto = x * desc
    print(f'A conta com desconto é {x-valor_desconto}')
    # mais código implementado....
    num_pessoas = int(input('Quantas pessoas? '))
    conta_final = (x-valor_desconto) / num_pessoas
    print(f'O valor da conta por pessoa é {conta_final}')
except ValueError:
    print('Oops... valor errado')
except ZeroDivisionError:
    print('Não posso dividir por zero')
else:
    print('O programa rodou')
finally:
    print('passei pelo finally')'''

## Exercício proposto:

while True:
    try:
        x = int(input('Entre com um valor: '))
        break
    except ValueError:
        print('Oops... Entre com um valor numérico')

print(f'O valor do dobro eh {2*x}')
