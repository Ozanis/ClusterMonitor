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
        path = str(os.getcwd()) + "/credentials/Server"
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
        self.host = None
        try:
            port = 4547
            self.host = "127.0.0.1"
            self.ssl_sock.bind((self.host, port))
        except OSError:
            subprocess.Popen(['notify-send', "Error of binding"])
            logging.error("Error of binding")
            exit(1)

    def con(self):
        self.ssl_sock.listen(1)
        c, p = self.ssl_sock.accept()
        #if c != self.host:
            #try:
             #   subprocess.check_call(["ufw", "deny", "incoming", "from", str(c)])
              #  logging.warning("Firewall role succefully added: %s (incoming traffic has blocked)" % str(c))
            #except subprocess.CalledProcessError:
             #   logging.warning("Firewall role is not added!")
              #  exit(1)
        try:
            _buf = self.ssl_sock.recv(3072)
            data = gzip.decompress(_buf)
            del _buf
            with open("log/test.log", "wb") as _f:
                _f.write(data)
        except socket.error:
            subprocess.Popen(['notify-send', "Warning: sending metrics error"])
            exit(1)

    def __del__(self):
        if self.host is not None:
            self.ssl_sock.close()
            self.sock.close()
            del self.ssl_sock, self.sock, self.host, self.context
        else:
            if self.sock is not None:
                try:
                    self.sock.close()
                finally:
                    del self.sock
                if self.context is not None:
                    del self.context
                    if self.ssl_sock is not None:
                        try:
                            self.ssl_sock.close()
                        finally:
                            del self.ssl_sock
                            if self.host is not None:
                                del self.host

c = SockSsl()
c.con()
