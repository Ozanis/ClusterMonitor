import socket, gzip, ssl, os, logging, subprocess

import socket, gzip, ssl, os, logging, subprocess

path = os.getcwd()+"/credentials/client/"
host, port="127.0.0.1", 4547
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

context = ssl.SSLContext(ssl.PROTOCOL_TLS)
context.verify_mode = ssl.CERT_REQUIRED
context.load_verify_locations(path+"crt.pem")
context.options = ssl.PROTOCOL_TLSv1_2

ssock = ssl.wrap_socket(sock, certfile=path+"crt.pem", keyfile=path+"key.pem", ciphers="TLS13+CDH+AESGCM:ECDH+CHACHA20", do_handshake_on_connect=True)
ssock.connect((host, port))

a = ssock.recv(1024)
print(a.decode())

print(ssock.version())
print(ssock.cipher())
ssock.close()
sock.close()