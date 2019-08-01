import logging
from socket import socket, error, AF_INET, SOCK_STREAM
from ssl import SSLContext, PROTOCOL_TLSv1_2, PROTOCOL_TLS, SSLEOFError, CERT_REQUIRED, wrap_socket
from os import getcwd
from subprocess import Popen


class SockSsl:

    def __init__(self):
        self.sock = None
        try:
            self.sock = socket(AF_INET, SOCK_STREAM, 0)
        except error:
            Popen(['notify-send', "Сould not create socket"])
            logging.error("Socket creation error")
            exit(1)
        self.context = None
        try:
            self.context = SSLContext(PROTOCOL_TLS)
        except SSLEOFError:
            Popen(['notify-send', "SSL context loading failed"])
            logging.error("Fake context")
            exit(1)
        path = str(getcwd()) + "/Credentials/"
        try:
            self.context.verify_mode = CERT_REQUIRED
            #self.context.load_cert_chain(certfile=path + "crt.pem", keyfile=path + "key.pem")
            self.context.load_verify_locations(path + "crt.pem")
            #self.context.options |= ssl.PROTOCOL_TLSv1_2 | ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1
            self.context.options = PROTOCOL_TLSv1_2
            #self.context.check_hostname = True
            #self.context.set_ciphers("TLS13+CDH+AESGCM:ECDH+CHACHA20")
        except SSLEOFError:
            Popen(['notify-send', "Braking cert-chain"])
            logging.error("Corrupted cert-chain")
            exit(1)
        try:
            self.ssl_sock = wrap_socket(self.sock, certfile=path+"crt.pem", keyfile=path+"key.pem", ciphers="TLS13+CDH+AESGCM:ECDH+CHACHA20", do_handshake_on_connect=True)
        except SSLEOFError:
            Popen(['notify-send', "Error of ssl-socket wrapping"])
            logging.error("Error loading cert-chain")
            exit(1)
        del path

    def con(self, host):
        try:
            port = 4547
            self.ssl_sock.connect((host, port))
        except error:
            self.ssl_sock.close()
            Popen(['notify-send', "Error of connection"])
            logging.error("Error of connection")
            exit(1)

    def send(self, data):
        try:
            self.ssl_sock.send(data)
        except error:
            Popen(['notify-send', "Warning: sending metrics error"])
            exit(1)
