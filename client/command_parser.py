#!/usr/bin/env python3

from commands import Commands


class CommandParser:
    def parse_command(self, command):
        command = command.lower().strip()
        result_cmd = self.__string_to_code(command)
        return result_cmd

    def __string_to_code(self, argument):
        switcher = {
            "exit": Commands.EXIT,
            "sair": Commands.EXIT,
            "criar": Commands.CREATE,
            "atualizar": Commands.UPDATE,
            "listar": Commands.LIST,
            "deletar": Commands.DELETE
        }
        return switcher.get(argument, None)
