import socket, gzip, ssl, os, logging, subprocess

class Client:
    def __init__(self):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error:
            logging.error("Socket creation error")
            del self.sock
            exit(1)
        self.port = 443
        self.addr = "localhost"
        self.peername = ""

    def _conn(self):
        try:
            self.addr = socket.gethostname()
        except socket.gaierror:
            logging.error("Server unreached")
            exit(1)

    def __del__(self):
        del self.sock
        del self.port
        del self.addr
        del self.peername


class SockSsl(Client):

    def __init__(self):
        super().__init__()
        try:
            self.ssl_sock = ssl.wrap_socket(self.sock, ssl_version=ssl.PROTOCOL_SSLv23, ciphers="RSA-AES256-SHA512", server_side=True, do_handshake_on_connect=True)
        except ssl.CertificateError:
            logging.error("Certificate error")
            subprocess.Popen(['notify-send', "Connection refused, because .X509 certificate not valid"])
            del self.ssl_sock
            exit(1)
        self.context=ssl.create_default_context(capath="/home/max/PycharmProjects/DFos_optimizations/credentials/", cafile="crt.pem")

    def set(self):
        self.ssl_sock.bind(self.addr)
        self.sock.listen(1)
        _con = self.sock.accept()
        _peer = self.sock.getpeername()

    def send(self, data):
        _buf = gzip.compress(str(data), compresslevel=9)
        try:
            self.ssl_sock.send(_buf)
        except socket.error:
            subprocess.Popen(['notify-send', "Warning: sending metrics error"])
        exit(1)

    def __del__(self):
        self.ssl_sock.close()
        del self.ssl_sock


path="/home/max/PycharmProjects/DFos_optimizations/credentials/"
context= ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_cert_chain(path+"crt.pem", path+"key.pem")
context.options=ssl.PROTOCOL_TLSv1
hostname="127.0.0.1"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        #context.options
        ssock.connect(("127.0.0.1", 4547))
        #ssock.
        ssock.do_handshake()
        print(ssock.version())