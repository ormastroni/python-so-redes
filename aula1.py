# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 19:39:56 2022

@author: andre
"""

## Módulo os
import os, time

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

## Retorna uma lista com o conteúdo do diretório
print(os.listdir())

## Distinção emtre arquivos e diretórios: isfile() e isdir()
p = 'projeto'
if os.path.isdir(p):
    print(p, 'é um diretorio!')
else:
    print(p, 'não é um diretorio!')


f = 'aula1.py'
if os.path.isfile(f):
    print(f, 'é um arquivo!')
else:
    print(f, 'não é um arquivo!')


## Pegar o nome de um arquivo num caminho completo
print(os.path.basename("C:\\Users\\Teste\\Desktop\\Exemplos\\arq_texto.txt"))

## Pegar o nome do diretório num caminho completo
print(os.path.dirname("C:\\Users\\Teste\\Desktop\\Exemplos\\arq_texto.txt"))

## Pegar o nome completo do caminho de um arquivo
print(os.path.abspath('arq_texto.txt'))

## Pegar uma tupla que separa o nome do caminho do nome do arquivo
print(os.path.split("C:\\Users\\Teste\\Desktop\\Exemplos\\arq_texto.txt"))

## Juntando os pedaços de um caminho
print(os.path.join("C:", "Users", "Teste", "arq_texto.txt"))

## Pegando o status de um arquivo
print(os.stat('aula1.py'))

status = os.stat('README.md')
## Formatando a data
print(status.st_mtime)
print(time.ctime(status.st_mtime))