#!/usr/bin/env python3

def is_string(input):
    try:
        # Convert it into integer
        int(input)
        print('O valor deve ser uma string')
        return False
    except ValueError:
        try:
            # Convert it into float
            float(input)
            print('O valor deve ser uma string')
            return False
        except ValueError:
            return True


def is_number(input):
    try:
        # Convert it into integer
        int(input)
        return True
    except ValueError:
        print('O valor deve ser um número inteiro')
        return False


def is_float(input):
    try:
        # Convert it into integer
        int(input)
        print('O valor deve ser um número real')
        return False
    except ValueError:
        try:
            # Convert it into float
            float(input)
            return True
        except ValueError:
            print('O valor deve ser um número real')
            return False
