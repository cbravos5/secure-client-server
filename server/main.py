#!/usr/bin/env python3

import sys
from command_parser import CommandParser
from commands import Commands
from create_service import CreateService
from common import sendMsg, recvMsg
from server import Server
from serializer import Serializer
from student_dao import StudentDao
import peewee

def dataHandler(connection):
        sendMsg(connection)
        data = recvMsg(connection)
        print(data)


# server = Server(3000)

# def dataHandler(connection):
#     data = recvMsg(connection)
#     while data:
#         print(data)
#         sendMsg(connection, "Hello From Server")
#         data = recvMsg(connection)

# server.startListening(dataHandler)

parser = CommandParser()

serializer = Serializer()
dao = StudentDao()
while True:
    try:
        # receive message
        command = serializer.deserialize('{"action": "create", "data": {"name": "a", "age": "32", "br_document": "a", "email": "b"}}')
        # defina a action
        try:
            if command['action'] == 'create':
                dao.create(command['data'])
            # retorna ok
        except peewee.PeeweeException as e:
            print(e)
            # retorna falha
        exit()
    except (EOFError, KeyboardInterrupt):
        print('\nEnd of program')
        break
