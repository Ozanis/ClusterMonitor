import socket

sock = socket.socket(socket.AF_INET, socket.AF_SECURITY, 0)

sock.bind(("111.111.111.111", 9090))

while True:
    sock.listen(1)



print(socket.gethostbyaddr("111.111.111.111"))