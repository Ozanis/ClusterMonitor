import socket, gzip, ssl, os, logging, subprocess

"""Open simple socket"""


class Sock4547:

    def __init__(self):
        try:
            subprocess.check_call(["ping", "-c 1", "www.google.ru"])
        except subprocess.CalledProcessError:
            logging.warning("No internet. Extra stopping")
            subprocess.Popen(['notify-send', "Warning: check your internet connection or possibly google host ureachable :)"])
            exit(1)

        logging.basicConfig(filename= str(os.getcwd()) + "/logs/server_log.log", level=logging.INFO)
        logging.info("---Telemetry log open session---")
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error:
            logging.error("Socket creation error")
            del self.sock
            exit(1)
        logging.info(str(os.getlogin()))
        self.port = 443
        self.addr = ""
        self.peername = ""

    def _conn(self):
        try:
            self.addr = socket.gethostname()
        except socket.gaierror:
            logging.error("Server unreached")
            self.__del__()
            exit(1)

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
            pass

    def __del__(self):
        self.ssl_sock.close()
        del self.ssl_sock

    @staticmethod
    def firewall_ban(danger_traffic_source):
        try:
            subprocess.check_call(["ufw", "deny", "incoming", "from", danger_traffic_source])
            logging.warning("Firewall role succefully added: %s (incoming traffic has blocked)" % danger_traffic_source)
            subprocess.Popen(['notify-send', "Warning: incoming possible dangerous traffic blocked from: ", danger_traffic_source])
        except subprocess.CalledProcessError:
            logging.warning("Firewall role is not added!")
            subprocess.Popen(['notify-send', "Warning: Firewall role is not added!", "Be carefull sock blocked"])
            exit(1)

    def _set(self):
        self.ssl_sock.bind(self.addr)
        self.sock.listen(1)
        _con = self.sock.accept()
        _peer = self.sock.getpeername()
        if _peer != self.peername or _con != self.addr:
            _con = str(_con)
            notifi = "WRONG CONNECTOR: %s" % (_con+str(_peer))
            logging.warning(notifi)
            subprocess.Popen(['notify-send', notifi])
            self.firewall_ban(_con)
            self.ssl_sock.close()
            return False
        else:
            logging.log("Connection estabilised with %s:" % str(_con))
            return True

    def _send(self, data):
        _buf = gzip.compress(str(data), compresslevel=9).encode("utf-8")
        try:
            self.ssl_sock.send(_buf)
        except socket.error:
            logging.error("Sending error")
            subprocess.Popen(['notify-send', "Warning: sending metrics error"])
        self.ssl_sock.close()
        self.__del__()
        logging.info("---Telemetry log SUCCESSFULLY CLOSE session---")

#def connect(self, data):
 #   self._set()
  #  self._send(data)
