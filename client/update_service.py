#!/usr/bin/env python3

from utils import *
from serializer import Serializer


class UpdateService:
    def call(self):
        print('===Atualização de aluno===')
        try:
            m_data = self.build_data()
            serializer = Serializer()
            serialized_data = serializer.serialize('update', m_data)
            return serialized_data
        # TODO: fix de ctrl + d para voltar ao menu.
        except KeyboardInterrupt as e:
            return

    def build_data(self):
        student = {}
        while True:
            student['br_document'] = input('> CPF do aluno: ')
            if is_string(student['br_document']):
                break
        while True:
            student['name'] = input('> Nome do aluno: ')
            if is_string(student['name']):
                break
        while True:
            student['age'] = input('> Idade do aluno: ')
            if is_number(student['age']):
                break
        while True:
            student['email'] = input('> e-mail do aluno: ')
            if is_string(student['email']):
                break
        return student
