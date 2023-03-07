import socket

# Cria o socket
socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#socket_servidor = socket.socket()

# Obtém o nome da máquina
host = 'localhost'
porta = 9999

# Associa a porta
socket_servidor.bind((host, porta))

# Escutando...
socket_servidor.listen()
print("Servidor de calculadora", host, "esperando conexão na porta", porta)

# Aceita alguma conexão
(socket_cliente,addr) = socket_servidor.accept()
print("Conectado a:", str(addr))

def soma(a,b):
    return a+b

def diferenca(a,b):
    return a-b

def multiplicacao(a,b):
    return a*b

def divisao(a,b):
    return a/b

while True:
    
    msg = socket_cliente.recv(1024)
    # Decodifica mensagem em ASCII
    msg_rec = msg.decode('ascii')
    
    lista = msg_rec.split()    
    resposta = 0
    
    try:
        if (lista[0] == '+'):
            resposta = soma(int(lista[1]), int(lista[2]))
        
        if (lista[0] == '-'):
            resposta = diferenca(int(lista[1]), int(lista[2]))
        
        if (lista[0] == '*'):
            resposta = multiplicacao(int(lista[1]), int(lista[2]))
        
        if (lista[0] == '/'):
            resposta = divisao(int(lista[1]), int(lista[2]))
    
        if (lista[0] == '@'):
            break
        
        print(msg_rec)
        print('Enviando resposta para o cliente...')
                
        # send resposta para o cliente
        msg_resposta = str(resposta)
        print(msg_resposta)
        socket_cliente.send(msg_resposta.encode('ascii'))
        
    except:
        msg_erro = 'Argumento invalido'
        print(msg_erro)
        socket_cliente.send(msg_erro.encode('ascii'))

socket_cliente.close()