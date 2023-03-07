import socket

# Cria o socket UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

try:
    
    DEST = ('localhost', 9999)

    while True:
        msg = input('Envie uma mensagem para o servidor: ')
        # Envia mensagem codificada em bytes ao servidor
        s.sendto(msg.encode('ascii'), DEST)
        if (msg == 'fim'):
            break
    # Fecha conexão com o servidor
    s.close()
except Exception as erro:
    print(str(erro))