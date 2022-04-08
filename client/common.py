def sendMsg(connection, data):
    encoded = data.encode("utf-8")
    connection.send(encoded)

def recvMsg(connection):
    data = connection.recv(1024)
    decoded = data.decode("utf-8")
    return decoded