from threading import Thread, ThreadError
from hashlib import md5
from socket import AF_INET, SOCK_STREAM, socket, error, SO_REUSEADDR
from gzip import decompress
from ssl import SSLEOFError, PROTOCOL_TLSv1_2, OP_NO_TLSv1, OP_NO_TLSv1_1, SSLContext, SOL_SOCKET
from sys import exit
from os import getcwd, listdir
import logging


class ServerSsl:

    def __init__(self):
        try:
            self.sock = socket(AF_INET, SOCK_STREAM, 0)
        except error:
            print("Сould not create socket")
            logging.error("Socket creation error")
            exit(1)
        self.context = None
        try:
            self.context = SSLContext(PROTOCOL_TLSv1_2)
        except SSLEOFError:
            print("SSL context loading failed")
            logging.error("Fake context")
            exit(1)
        path = getcwd() + "/credentials/"
        try:
            self.context.load_cert_chain(certfile=path +"crt.pem", keyfile=path + "key.pem")
            self.context.options |= PROTOCOL_TLSv1_2 | OP_NO_TLSv1 | OP_NO_TLSv1_1
            self.context.set_ciphers("TLS13+CDH+AESGCM:ECDH+CHACHA20")
        except SSLEOFError:
            print("Braking cert-chain")
            logging.error("Corrupted cert-chain")
            exit(1)
        self.ssl_sock = None
        try:
            self.ssl_sock = self.context.wrap_socket(self.sock, server_side=True, do_handshake_on_connect=True)
            #self.ssl_sock.ssl_version
        except SSLEOFError:
            print("Error of ssl-socket wrapping")
            logging.error("Error loading cert-chain")
            exit(1)
        try:
            #host = "127.0.0.1"
            host = "35.247.6.149"
            port = 4547
            self.ssl_sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
            self.ssl_sock.bind((host, port))
        except SSLEOFError:
            print("Error of binding")
            logging.error("Error of binding")
            exit(1)

    def con(self, direct):
        self.ssl_sock.listen(9)
        print("START SERVER LISTENING")
        while True:
            try:
                c, a = self.ssl_sock.accept()
            except error:
                print("Acception error")
                continue
            try:
                tsession = Thread(target=self.get_log(c, direct), args="")
                tsession.start()
            except ThreadError:
                logging.error("Session braked")
                print("Session braked")

    @staticmethod
    def get_log(conn, cur_direct):
        try:
            _buf = conn.recv(9216)
        except error:
            print("Warning: Recieving metrics error")
        else:
            conn.close()
            ind = str(md5(str(conn).encode()).hexdigest())
            del conn
            num = str(len(listdir(cur_direct)))
            ind += num
            try:
                with open(cur_direct + ind + ".log", "wb") as _f:
                    try:
                        data = decompress(_buf)
                    except EOFError:
                        print("Error: Unable to decompress packets")
                    else:
                        _f.write(data)
            except IOError:
                print("Warning: Unable to write log")
            finally:
                del ind
        #except BufferError:
         #   print("Buffer overflow")

    def disable(self):
        self.ssl_sock.close()
        self.sock.close()
