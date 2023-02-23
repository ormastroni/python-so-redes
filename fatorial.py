class FatorialException(Exception):
    pass

def fatorial(n):
    try:
        if (n < 0):
            raise FatorialException('Não existe fatorial de numeros negativos')
        if (n == 1):
            return 1
        return n*fatorial(n-1)
    except TypeError:
        print('Fatorial só para numeros e positivos')
        ## Retorna -1 para valores não numéricos
        return -1
    return 1

print(fatorial(-1))