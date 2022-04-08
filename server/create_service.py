#!/usr/bin/env python3

from distutils.command.build import build
from utils import *
from serializer import Serializer


class CreateService:

    def __init__(self, client):
        self.client_connection = client

    def call(self):
        # read input
        # serialize data
        # send data
        print('===Criação de aluno===')
        try:
            m_data = self.build_data()
            serializer = Serializer()
            serialized_data = serializer.serialize('create', m_data)
            # Send to remote
        # TODO: fix de ctrl + d para voltar ao menu.
        except KeyboardInterrupt as e:
            return

    def build_data(self):
        student = {}
        while True:
            student['name'] = input('> Nome do aluno: ')
            if is_string(student['name']):
                break
        while True:
            student['age'] = input('> Idade do aluno: ')
            if is_number(student['age']):
                break
        while True:
            student['br_document'] = input('> CPF do aluno: ')
            if is_string(student['br_document']):
                break
        while True:
            student['email'] = input('> e-mail do aluno: ')
            if is_string(student['email']):
                break
