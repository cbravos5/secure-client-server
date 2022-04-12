#!/usr/bin/env python3

from distutils.command.build import build
from utils import *
from serializer import Serializer


class DeleteService:
    def call(self):
        print('===remoção de aluno===')
        try:
            m_data = self.build_data()
            serializer = Serializer()
            serialized_data = serializer.serialize('delete', m_data)
            return serialized_data
        # TODO: fix de ctrl + d para voltar ao menu.
        except KeyboardInterrupt as e:
            return

    def build_data(self):
        params = {}
        while True:
            params['br_document'] = input('> CPF do aluno: ')
            if is_string(params['br_document']):
                break
        return params
