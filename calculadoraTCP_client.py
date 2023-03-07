import socket

# Cria o socket UDP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

try:
    # Tenta se conectar ao servidor
    s.connect(('localhost', 9999))

    while True:
        msg = input('Entre com a expressão: ')
        
        # Envia mensagem codificada em bytes ao servidor
        s.send(msg.encode('ascii'))
        if (msg == '@'):
            break
    
        resp = s.recv(1024)
        print(resp.decode('ascii'))
    
    # Fecha conexão com o servidor
    s.close()
except Exception as erro:
    print(erro)