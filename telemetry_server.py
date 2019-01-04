import socket, gzip, ssl, os, syslog

class DF_user:

    def __init__(self):
        self.user = os.getlogin()

    def credentials(self):
        return str(self.user)

    def __del__(self):
        del self.user


class Sock443:

    def __init__(self):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error:
            print("socket creation error")
            pass
        self.port = 443
        self.addr = ""

    def _conn(self):
        try:
            self.addr = socket.gethostname()
        except socket.gaierror:
            self.__del__()

    def __del__(self):
        del self.sock
        del self.port
        del self.addr


class SockSsl(Sock443):

    def __init__(self):
        super().__init__()
        try:
            self.ssl_sock = ssl.wrap_socket(self.sock, ssl_version=ssl.PROTOCOL_SSLv23, ciphers="", server_side=True, do_handshake_on_connect=True)
        except ssl.CertificateError:
            print("CertificateError")
            pass

    def __del__(self):
        del self.ssl_sock

    def set(self):
        self.ssl_sock.bind(self.addr)
        self.sock.listen(1)
        if self.sock.getpeername()!="correct name":
            print("wrong connector!")
            self.ssl_sock.close()
            return False
        else:
            print("start connect")
            return True

    def _send(self, data):
        try:
            self.ssl_sock.send(data)
        except "sending error":
            self.ssl_sock.close()
            self.__del__()




