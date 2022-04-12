#!/usr/bin/env python3

from models import Student
from playhouse.shortcuts import model_to_dict

class StudentDao:

    def create(self, data):
        Student.create(**data)

    def update(self, data):
        student = Student.get(Student.br_document == data['br_document'])
        student.name = data['name']
        student.age = data['age']
        student.br_document = data['br_document']
        student.email = data['email']
        student.save()

    def list(self, data):
        query = Student.select().limit(data['limit'])
        return [model_to_dict(student) for student in query]

    def delete(self, data):
        s = Student.get(Student.br_document == data['br_document'])
        s.delete_instance()
        # Student.delete().where(data['br_document']).execute()
