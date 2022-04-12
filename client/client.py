import socket
import ssl
from common import sendMsg, recvMsg


class Client:

    def __init__(self):
        self.context = self.createContext()
        self.connection = self.createConnection()

    def createContext(self):
        context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
        context.verify_mode = ssl.CERT_REQUIRED
        context.load_verify_locations("../serverCRT/server.crt")
        context.load_cert_chain(
            certfile="../clientCRT/client.crt", keyfile="../clientCRT/client.key")
        return context

    def createConnection(self):
        s = socket.socket()  # socket.AF_INET, socket.SOCK_STREAM default
        connection = self.context.wrap_socket(s, server_side=False)
        return connection

    def startConnection(self, port, handler):
        try:
            self.connection.connect(('127.0.0.1', port))
            handler(self.connection)
            self.connection.close()
        except Exception as e:
            print('Problema na conexão: ', e)
            exit()

