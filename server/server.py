import socket, ssl
from common import sendMsg, recvMsg

class Server:

    def __init__(self, port):
        self.context = self.createContext()
        self.socket = self.createSocket(port)
        self.connection = None

    def createContext(self):
        context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
        context.verify_mode = ssl.CERT_REQUIRED
        context.load_verify_locations("../clientCRT/client.crt")
        context.load_cert_chain(certfile="../serverCRT/server.crt", keyfile="../serverCRT/server.key")
        # context.keylog_filename = "keylog.log" # DEBUG PURPOSES
        return context

    def createSocket(self, port):
        bindsocket = socket.socket()
        bindsocket.bind(('127.0.0.1', port))
        bindsocket.listen(5)
        return bindsocket

    def startListening(self, dataHandler):
        while True:
            try:
                newsocket, fromaddr = self.socket.accept()
                self.connection = self.context.wrap_socket(newsocket, server_side=True)
                try:
                    dataHandler(self.connection) # uses connection.recv() and connection.send()
                finally:
                    self.connection.shutdown(socket.SHUT_RDWR)
                    self.connection.close()
            except Exception as e:
                print('Erro na conexão: ', e)
                exit()

if __name__ == "__main__":
    server = Server(3000)

    def dataHandler(connection):
        data = recvMsg(connection)
        while data:
            print(data)
            sendMsg(connection, "Hello From Server")
            data = recvMsg(connection)

    server.startListening(dataHandler)
