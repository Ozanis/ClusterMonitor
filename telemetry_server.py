import socket, gzip, ssl, os, logging, subprocess, hashlib


def firewall_ban(con):
    try:
        subprocess.check_call(["ufw", "deny", "incoming", "from", str(con)])
    except subprocess.CalledProcessError:
        logging.warning("Firewall role is not added!")
        exit(1)
    logging.warning("Firewall role succefully added: %s (incoming traffic has blocked)" % str(con))


class Sock4547:

    def __init__(self):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        except socket.error:
            subprocess.Popen(['notify-send', "Сould not create socket"])
            logging.error("Socket creation error")
            exit(1)
        logging.info(str(os.getlogin()))
        self.port = 4547
        self.host = "127.0.0.1"
        self.peer = "localhost"
        self.peername = ""
        self.sock.bind((self.host, self.port))
        self.sock.listen(1)
        con = self.sock.accept()
        peer = self.sock.getpeername()
        if peer != self.peername or con != self.host:
            notifi = "WRONG CONNECTOR: %s" % (con + str(peer))
            logging.warning(notifi)
            subprocess.Popen(['notify-send', notifi])
            firewall_ban(con)
            exit(1)
        else:
            del con, peer
            self.path = "/home/max/PycharmProjects/DFos_optimizations/credentials/Server/peer_cert.pem"
            H = open(self.path, "rb")
            #del path
            _h = H.read()
            self.hash = hashlib.md5(_h).hexdigest()
            del _h

    def __del__(self):
        self.sock.close()
        del self.sock, self.port, self.host, self.peer, self.hash


class SockSsl(Sock4547):

    def __init__(self):
        super().__init__()
        try:
            self.context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        except ssl.SSLEOFError:
            subprocess.Popen(['notify-send', "SSL context loading failed"])
            logging.error("Fake context")
        try:
            path = "/home/max/PycharmProjects/DFos_optimizations/credentials/Server/"
            self.context.check_hostname = True
            self.context.verify_mode = ssl.CERT_REQUIRED
            self.context.load_cert_chain(certfile=path + "crt.pem", keyfile=path + "key.pem")
            self.context.load_verify_locations(capath=path+"csr.pem")
            self.context.options |= (ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1)
            self.context.options = ssl.PROTOCOL_TLSv1_2
        except ssl.SSLEOFError:
            subprocess.Popen(['notify-send', "Braking cert-chain"])
            logging.error("Corrupted cert-chain")
        try:
            self.ssl_sock = self.context.wrap_socket(self.sock, server_side=True, do_handshake_on_connect=True)
            self.ssl_sock.server_hostname = "localhost"
        except ssl.SSLEOFError:
            subprocess.Popen(['notify-send', "Error of ssl-socket wrapping"])
            logging.error("Error loading cert-chain")
        finally:
            exit(1)

    def verifi(self):
        c = b"%s" % self.ssl_sock.getpeercert()
        if self.hash != hashlib.md5(c).hexdigest():
            false_cert = open(self.path + "false_cert.pem", "wb")
            false_cert.write(c)
            del c
            false_cert.close()
            subprocess.Popen(['notify-send', "Warning wrong connector"])
            logging.warning("Wrong connector: certs is not match")
            return False
        else:
            logging.info("Connection estabilised")
            return True

    def send(self, data):
        _buf = gzip.compress(str(data), compresslevel=9)
        try:
            self.ssl_sock.send(_buf)
        except socket.error:
            subprocess.Popen(['notify-send', "Warning: sending metrics error"])
            exit(1)

    def __del__(self):
        self.ssl_sock.close()
        del self.ssl_sock, self.context
