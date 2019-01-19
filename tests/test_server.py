import socket, gzip, ssl, logging, subprocess, os


class SockSsl:

    def __init__(self):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        except socket.error:
            subprocess.Popen(['notify-send', "Сould not create socket"])
            logging.error("Socket creation error")
            exit(1)
        self.context = None
        try:
            self.context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
        except ssl.SSLEOFError:
            subprocess.Popen(['notify-send', "SSL context loading failed"])
            logging.error("Fake context")
            exit(1)
        path = str(os.getcwd()) + "/credentials/Server/"
        try:
            self.context.load_cert_chain(certfile=path +"crt.pem", keyfile=path + "key.pem")
            self.context.options |= ssl.PROTOCOL_TLSv1_2 | ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1
            self.context.set_ciphers("TLS13+CDH+AESGCM:ECDH+CHACHA20")
        except ssl.SSLEOFError:
            subprocess.Popen(['notify-send', "Braking cert-chain"])
            logging.error("Corrupted cert-chain")
            exit(1)
        self.ssl_sock = None
        try:
            self.ssl_sock = self.context.wrap_socket(self.sock, server_side=True, do_handshake_on_connect=True)
            #self.ssl_sock.ssl_version
        except ssl.SSLEOFError:
            subprocess.Popen(['notify-send', "Error of ssl-socket wrapping"])
            logging.error("Error loading cert-chain")
            exit(1)
        try:
            host = "127.0.0.1"
            port = 4547
            self.ssl_sock.bind((host, port))
            #self.ssl_sock.ssl_version
        except ssl.SSLEOFError:
            subprocess.Popen(['notify-send', "Error of binding"])
            logging.error("Error of binding")
            exit(1)

    def con(self):
        self.ssl_sock.listen(1)
        a, c = self.ssl_sock.accept()
        print(c)
        print(a)
        #if c != self.host:
            #try:
            #   subprocess.check_call(["ufw", "deny", "incoming", "from", str(c)])
            #  logging.warning("Firewall role succefully added: %s (incoming traffic has blocked)" % str(c))
            #except subprocess.CalledProcessError:
            #   logging.warning("Firewall role is not added!")
            #  exit(1)
        _buf = None
        try:
            _buf = a.recv(3072)
        except socket.error:
            subprocess.Popen(['notify-send', "Warning: Recieving metrics error"])
            exit(1)
        data = None
        try:
            data = gzip.decompress(_buf)
            del _buf
        except EOFError:
            subprocess.Popen(['notify-send', "Error: Unable to decompress packets"])
            exit(1)
        try:
            with open(str(os.getcwd()) + "/log/test.log", "wb") as _f:
                _f.write(data)
                del data
        except IOError:
            subprocess.Popen(['notify-send', "Warning: Unable to write log"])
            exit(1)


c = SockSsl()
c.con()
