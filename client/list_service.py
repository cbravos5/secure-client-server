#!/usr/bin/env python3

from utils import *
from serializer import Serializer


class ListService:
    def call(self):
        print('===listagem de aluno===')
        try:
            m_data = self.build_data()
            serializer = Serializer()
            serialized_data = serializer.serialize('list', m_data)
            return serialized_data
        # TODO: fix de ctrl + d para voltar ao menu.
        except KeyboardInterrupt as e:
            return

    def build_data(self):
        params = {}
        while True:
            params['limit'] = input('> Quantidade de alunos (max: 10): ')
            if is_number(params['limit']) and int(params['limit']) <= 10:
                break
        return params
