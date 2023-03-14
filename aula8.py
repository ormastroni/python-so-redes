import socket, sys, struct, time

hostname = 'pool.ntp.org' # Servidor NTP
port = 123
TIME1970 = 2208988800 # 1970-01-01 00:00:00
NTP_QUERY = '\x1b' + 47 * '\0' # Código para requisição NTP

host = socket.gethostbyname(hostname) # Obtém IP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.settimeout(1)
s.sendto(NTP_QUERY.encode('ascii'), (host, port))

try:
    (buf,addr) = s.recvfrom(1024)

    if len(buf) != 48: # São 12 inteiros: 12 * 4 bytes recebidos
        print ("Tamanho errado ", (len(buf), buf))
        sys.exit(1)

    tuple_secs = struct.unpack("!12I", buf)
    print(tuple_secs)
    secs = tuple_secs[10]
    
    if (secs <= 0):
        print ("Segundos errados ", secs)
        sys.exit(1)

    secs -=  TIME1970
    print (time.ctime(int(secs)))
except socket.timeout as e:
    print('Tempo excedido de espera')
    print(e)