class SockSsl(Sock443):

    def __init__(Sock443):
        super().__init__()
        Sock443.ssl_sock = ssl.wrap_socket(Sock443.sock, ssl_version=ssl.PROTOCOL_SSLv23, ciphers="", do_handshake_on_connect=True)

    def __del__(Sock443):
        del Sock443.ssl_sock

    def set(Sock443):
        Sock443.ssl_sock.connect((Sock443.addr, Sock443.port))

    def _send(Sock443, data):

        try:
            Sock443.ssl_sock.send(data)
            Sock443.ssl_sock.close()
        except:
            Sock443.__del__()
