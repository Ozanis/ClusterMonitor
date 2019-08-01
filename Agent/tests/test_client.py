import socket, gzip, ssl, os, logging, subprocess


class SockSsl:

    def __init__(self):
        self.sock = None
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        except socket.error:
            subprocess.Popen(['notify-send', "Сould not create socket"])
            logging.error("Socket creation error")
            exit(1)
        self.context = None
        try:
            self.context = ssl.SSLContext(ssl.PROTOCOL_TLS)
        except ssl.SSLEOFError:
            subprocess.Popen(['notify-send', "SSL context loading failed"])
            logging.error("Fake context")
            exit(1)
        path = str(os.getcwd()) + "/credentials/client/"
        try:
            self.context.verify_mode = ssl.CERT_REQUIRED
            #self.context.load_cert_chain(certfile=path + "crt.pem", keyfile=path + "key.pem")
            self.context.load_verify_locations(capath=path + "crt.pem")
            #self.context.options |= ssl.PROTOCOL_TLSv1_2 | ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1
            self.context.options = ssl.PROTOCOL_TLSv1_2
            self.context.check_hostname = True
            #self.context.set_ciphers("TLS13+CDH+AESGCM:ECDH+CHACHA20")
        except ssl.SSLEOFError:
            subprocess.Popen(['notify-send', "Braking cert-chain"])
            logging.error("Corrupted cert-chain")
            exit(1)
        try:
            self.ssl_sock = ssl.wrap_socket(self.sock, certfile=path+"crt.pem", keyfile=path+"key.pem", ciphers="TLS13+CDH+AESGCM:ECDH+CHACHA20")
        except ssl.SSLEOFError:
            subprocess.Popen(['notify-send', "Error of ssl-socket wrapping"])
            logging.error("Error loading cert-chain")
            exit(1)
        del path

    def con(self, val):
        try:
            port = 4547
            host = "127.0.0.1"
            self.ssl_sock.connect((host, port))
        except socket.error:
            subprocess.Popen(['notify-send', "Error of connection"])
            logging.error("Error of binding")
            exit(1)
        buf = gzip.compress(val, compresslevel=9)
        try:
            self.ssl_sock.send(buf)
        except socket.error:
            subprocess.Popen(['notify-send', "Warning: sending metrics error"])
            exit(1)

    def __del__(self):
        if self.ssl_sock is not None:
            del self.context
            self.ssl_sock.unwrap()
            self.ssl_sock.close()
            del self.ssl_sock
            self.sock.close()
            del self.sock
        else:
            if self.sock is not None:
                del self.sock
                if self.context is not None:
                    del self.context
                    if self.ssl_sock is not None:
                        del self.ssl_sock

c = SockSsl()
with open("file.txt", "wb") as _f:
    _f.write(b"dffffffffffff")
with open("file.txt", "rb") as _f:
    _buf = _f.read()
    c.con(_buf)
os.remove("file.txt")