#!/usr/bin/env python3

from common import sendMsg, recvMsg
from server import Server
from serializer import Serializer
from student_dao import StudentDao
import peewee

def dataHandler(connection):
    serializer = Serializer()
    dao = StudentDao()
    while True:
        try:
            # receive message
            data = recvMsg(connection)
            command = serializer.deserialize(data)
            try:
                msg = { 'status': 'OK', 'message': 'ok'}
            # defina a action
                if command['action'] == 'create':
                    print('Ação criar executada.')
                    dao.create(command['data'])
                elif command['action'] == 'update':
                    print('Ação atualizar executada.')
                    dao.update(command['data'])
                elif command['action'] == 'list':
                    print('Ação listar executada')
                    msg['data'] = dao.list(command['data'])
                elif command['action'] == 'delete':
                    print('Ação deletar executada')
                    dao.delete(command['data'])
                # retorna ok
                msg = serializer.serialize(msg)
            except peewee.PeeweeException as e:
                print(e)
                # retorna falha
                msg = { 'status': 'NOK', 'message': str(e)}
                msg = serializer.serialize(msg)
            sendMsg(connection, msg)
        except (EOFError, KeyboardInterrupt):
            print('\nEnd of program')
            break
    exit()


print('Starting server...')
server = Server(3002)
print('Server started...')
server.startListening(dataHandler)
