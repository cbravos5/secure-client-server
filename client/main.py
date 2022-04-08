#!/usr/bin/env python3

import sys
from command_parser import CommandParser
from commands import Commands
from create_service import CreateService
from client import Client
from common import sendMsg, recvMsg

def dataHandler(connection):
        sendMsg(connection)
        data = recvMsg(connection)
        print(data)


client = Client()
client.startConnection(3000,dataHandler)

parser = CommandParser()
create_service = CreateService(client)
while True:
    try:
        raw_cmd = input('> ')
        cmd = parser.parse_command(raw_cmd)
        if cmd == Commands.EXIT:
            sys.exit()
        elif cmd == Commands.CREATE:
            create_service.call()
    except EOFError:
        print('end')
        break
