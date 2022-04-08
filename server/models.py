#!/usr/bin/env python3

import peewee

# conectar no banco de dados
# Aqui criamos o banco de dados
db = peewee.SqliteDatabase('./base_alunos.db')
# criar base de dados se não existir


class BaseModel(peewee.Model):
    """Classe model base"""

    class Meta:
        # Indica em qual banco de dados a tabela
        # 'author' sera criada (obrigatorio). Neste caso,
        # utilizamos o banco 'codigo_avulso.db' criado anteriormente
        database = db

class Student(BaseModel):
    """
    Classe que representa a tabela Student
    """
    # A tabela possui apenas o campo 'name', que receberá o nome do autor sera unico
    name = peewee.CharField()
    age = peewee.IntegerField()
    br_document = peewee.CharField()
    email = peewee.CharField()

if __name__ == '__main__':
    try:
        Student.create_table()
        print("Tabela 'Student' criada com sucesso!")
    except peewee.OperationalError:
        print("Tabela 'Student' ja existe!")
