import socket

# Cria o socket
#socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_servidor = socket.socket()

# Obtém o nome da máquina
host = 'localhost'
porta = 9999

servidor = ('localhost', 9999)

# Associa a porta
socket_servidor.bind(servidor)

# Escutando...
socket_servidor.listen()
print("Servidor de nome", host, "esperando conexão na porta", porta)

# Aceita alguma conexão
(socket_cliente,addr) = socket_servidor.accept()
print("Conectado a:", str(addr))

while True:    
    msg = socket_cliente.recv(1024)
    # Decodifica mensagem em ASCII
    msg_rec = msg.decode('ascii')
    print(msg_rec)
    if (msg_rec == 'fim'):
        break
    
socket_cliente.close()