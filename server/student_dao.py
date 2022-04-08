#!/usr/bin/env python3

from models import Student

class StudentDao:

    def create(self, data):
        Student.create(**data)