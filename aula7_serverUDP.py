import socket

# Cria o socket
socket_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = 'localhost'
porta = 9999

orig = (host, porta)

# Associa a porta
socket_udp.bind(orig)

print('Comunicação UDP...')
while True:    
    (msg, cliente) = socket_udp.recvfrom(1024)
    # Decodifica mensagem em ASCII
    msg_rec = msg.decode('ascii')
    print(msg_rec, cliente)
    if (msg_rec == 'fim'):
        break
    
socket_udp.close()