import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

print(socket.gethostbyaddr("35.247.6.149"))
