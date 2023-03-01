import socket

# Cria o socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

try:
    
    DEST = ('localhost', 9999)
    s.connect(DEST)

    while True:
        msg = input('Envie uma mensagem para o servidor: ')
        # Envia mensagem codificada em bytes ao servidor
        s.send(msg.encode('ascii'))
        if (msg == 'fim'):
            break
    # Fecha conexão com o servidor
    s.close()
except Exception as erro:
    print(erro)