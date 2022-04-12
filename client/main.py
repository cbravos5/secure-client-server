#!/usr/bin/env python3

import sys
from command_parser import CommandParser
from commands import Commands
from create_service import CreateService
from update_service import UpdateService
from list_service import ListService
from delete_service import DeleteService
from client import Client
from common import sendMsg, recvMsg
from serializer import Serializer

def handle_response(response):
    serializer = Serializer()
    response_data = serializer.deserialize(response)
    print('server_response: ', response_data)

def dataHandler(connection):
    parser = CommandParser()
    create_service = CreateService()
    update_service = UpdateService()
    list_service = ListService()
    delete_service = DeleteService()
    while True:
        try:
            raw_cmd = input('> ')
            cmd = parser.parse_command(raw_cmd)
            serialized_data = None
            if cmd == Commands.EXIT:
                sys.exit()
            elif cmd == Commands.CREATE:
                serialized_data = create_service.call()
            elif cmd == Commands.UPDATE:
                serialized_data = update_service.call()
            elif cmd == Commands.LIST:
                serialized_data = list_service.call()
            elif cmd == Commands.DELETE:
                serialized_data = delete_service.call()
            if serialized_data != None:
                print('mensagem enviada: ', serialized_data)
                sendMsg(connection, serialized_data)
                response = recvMsg(connection)
                handle_response(response)
        except EOFError:
            break

client = Client()
client.startConnection(3000, dataHandler)
