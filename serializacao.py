import pickle

class Pessoa:

    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    def getNome(self):
        return self._nome
    
    def getIdade(self):
        return self._idade
    
    def __str__(self) -> str:
        return self._nome + '{' + str(self._idade) + '}'
    

andre = Pessoa('andre', 49)
joao = Pessoa('joao', 21)
gus = Pessoa('gustavo', 19)

print(andre)
print(joao)
print(gus)

andre_bytes = pickle.dumps(andre)
print(andre_bytes)

objeto = pickle.loads(andre_bytes)
print(objeto)

