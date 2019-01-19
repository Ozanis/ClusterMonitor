import logging
from socket import AF_INET, SOCK_STREAM, socket, error
from gzip import decompress
from ssl import SSLEOFError, PROTOCOL_TLSv1_2, OP_NO_TLSv1, OP_NO_TLSv1_1, SSLContext
from os import getcwd
from sys import exit


class SockSsl:

    def __init__(self):
        try:
            self.sock = socket(AF_INET, SOCK_STREAM, 0)
        except error:
            print("Сould not create socket")
            logging.error("Socket creation error")
            exit(1)
        self.context = None
        try:
            self.context = SSLContext(PROTOCOL_TLSv1_2)
        except SSLEOFError:
            print("SSL context loading failed")
            logging.error("Fake context")
            exit(1)
        path = str(getcwd()) + "/credentials/Server/"
        try:
            self.context.load_cert_chain(certfile=path +"crt.pem", keyfile=path + "key.pem")
            self.context.options |= PROTOCOL_TLSv1_2 | OP_NO_TLSv1 | OP_NO_TLSv1_1
            self.context.set_ciphers("TLS13+CDH+AESGCM:ECDH+CHACHA20")
        except SSLEOFError:
            print("Braking cert-chain")
            logging.error("Corrupted cert-chain")
            exit(1)
        self.ssl_sock = None
        try:
            self.ssl_sock = self.context.wrap_socket(self.sock, server_side=True, do_handshake_on_connect=True)
            #self.ssl_sock.ssl_version
        except SSLEOFError:
            print( "Error of ssl-socket wrapping")
            logging.error("Error loading cert-chain")
            exit(1)
        try:
            host = ""
            port = 4547
            self.ssl_sock.bind((host, port))
            #self.ssl_sock.ssl_version
        except SSLEOFError:
            print( "Error of binding")
            logging.error("Error of binding")
            exit(1)

    def con(self):
        self.ssl_sock.listen(1)
        a, c = self.ssl_sock.accept()
        #if c != self.host:
            #try:
            #   subprocess.check_call(["ufw", "deny", "incoming", "from", str(c)])
            #  logging.warning("Firewall role succefully added: %s (incoming traffic has blocked)" % str(c))
            #except subprocess.CalledProcessError:
            #   logging.warning("Firewall role is not added!")
            #  exit(1)
        _buf = None
        try:
            _buf = a.recv(92160)
        except error:
            print( "Warning: Recieving metrics error")
            exit(1)
        data = None
        try:
            data = decompress(_buf)
            del _buf
        except EOFError:
            print( "Error: Unable to decompress packets")
            exit(1)
        try:
            with open(str(getcwd()) + "/log/test.log", "wb") as _f:
                _f.write(data)
                del data
        except IOError:
            print("Warning: Unable to write log")
            exit(1)