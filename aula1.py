# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 19:39:56 2022

@author: andre
"""

## Módulo os
import os

## Nomes do sistema operacional e do usuário logado
print(os.name)
print(os.getlogin())


## Variáveis de ambiente da máquina: Propriedade environ é um dicionário, 
# onde cada chave é uma variável de ambiente, e o valor é o valor correspondente da variável
print(os.environ)
print(os.environ['HOMEDRIVE'])
print(os.environ['HOMEPATH'])
print(os.environ['OS'])
print(os.environ['JAVA_HOME'])
print(os.getcwd())
print(os.getpid())

## Manipulação do sistema de arquivos
os.mkdir('novo_dir')
print('diretorio criado')
os.rename('novo_dir', 'nova_pasta')
os.rmdir('nova_pasta')

print(os.listdir(r'C:\users\andre'))

p = 'arq_texto.txt'
if os.path.isdir(p):
    print(p, 'é um diretorio!')
else:
    print(p, 'não é um diretorio!')