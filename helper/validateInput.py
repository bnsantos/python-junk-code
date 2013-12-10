__author__ = 'bruno'


def validate_integer_positive_input(n):
    if type(n) == type(int()) and n >= 0:
        return True
    else:
        return False


def validate_string_input(n):
    if type(n) == type(str()) and len(n) > 0:
        return True
    else:
        return False
