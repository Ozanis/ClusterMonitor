import socket, gzip, ssl, os, logging, subprocess
from dataclasses import dataclass, field

"""Get individual machine name"""


class DFuserAuthorize:

    def __init__(self):
        self.user = os.getlogin()

    def __repr__(self):
        return str(self.user)

    def __del__(self):
        del self.user


"""Data compresser"""


@dataclass
class Cmprs:

    data: str = field(repr=True)

    def __repr__(self):
        return gzip.compress(self.data, compresslevel=9).encode()


"""Open simple socket"""


class Sock4547:

    def __init__(self):
        try:
            subprocess.check_call(["ping", "-c 1", "www.google.ru"])
        except subprocess.CalledProcessError:
            logging.warning("No internet")
            exit(1)
        logging.basicConfig(filename= str(os.getcwd()) + "/logs/server_log.log", level=logging.INFO)
        logging.info("---Telemetry log---")
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error:
            logging.error("Socket creation error")
            del self.sock
            exit(1)
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
            del self.ssl_sock
            pass

    def __del__(self):
        del self.ssl_sock

    @staticmethod
    def firewall_ban(_con):
        try:
            subprocess.check_call(["ufw", "deny", "incoming", "from", str(_con)])
        except subprocess.CalledProcessError:
            logging.warning("Firewall role is not added!")
            exit(1)
        logging.warning("Firewall role succefully added: %s (incoming traffic has blocked)" % str(_con))

    def set(self):
        self.ssl_sock.bind(self.addr)
        self.sock.listen(1)
        _con = self.sock.accept()
        _peer = self.sock.getpeername()
        if _peer != self.peername or _con != self.addr:
            logging.warning("WRONG CONNECTOR: %s" % (str(_con)+str(_peer)) )
            self.firewall_ban(_con)

            self.ssl_sock.close()
            return False
        else:
            logging.log("Connection estabilised with %s:" % str(_con))
            return True

    def _send(self, data):
        try:
            self.ssl_sock.send(data)
        except socket.error:
            logging.error("Sending error")
            self.ssl_sock.close()
            self.__del__()
