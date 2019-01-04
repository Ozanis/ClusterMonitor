import socket, gzip, gzip, hashlib, os

class DF_user:

    def __init__(self):
        self.user = os.getlogin()

    def credentials(self):
        return str(self.user)

    def __del__(self):
        del self.user


class LocalServ:

    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.port = 443
        self.addr = socket.gethostname()
        self.buffer = ""
        self.filename = ""

    def beacon_set(self):
        self.sock.bind((self.addr, self.port))
        self.sock.listen(1)

    def beacon_recv(self):
        self.sock.accept()

        with open(self.filename, "wb") as _file:
            try:
                while len(self.buffer)<=1024:
                    self.buffer = self.sock.recv(1024)
                    _file.write(self.buffer)
            except:
                if len(self.buffer) >= 1024:
                    self.buffer =""
                else:
                    self.sock.send("Error of file transfer".encode())
                    self.sock.close()
                    self.buffer=""

