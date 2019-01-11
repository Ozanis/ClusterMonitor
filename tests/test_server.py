import socket, gzip, ssl, os, logging, subprocess

"""Open simple socket"""


class Sock4547:

    def __init__(self):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error:
            logging.error("Socket creation error")
            del self.sock
            exit(1)
        logging.info(str(os.getlogin()))
        self.port = 443
        self.addr = "localhost"
        self.peername = "localhost"

    def __del__(self):
        del self.sock
        del self.port
        del self.addr
        del self.peername


"""Open SSL layer"""


class SockSsl(Sock4547):

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
print(path)
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(path+"crt.pem", path+"key.pem")
context.options=ssl.PROTOCOL_TLSv1
hostname="localhost"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
    sock.bind((hostname, 4547))
    sock.listen(5)
    with context.wrap_socket(sock, server_side=True) as ssock:
        conn, addr = ssock.accept()
        ssock.getpeercert()
        ssock.do_handshake()

