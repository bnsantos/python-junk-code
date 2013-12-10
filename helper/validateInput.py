__author__ = 'bruno'


def validate_integer_positive_input(n):
    if type(n) == type(int()) and n >= 0:
        return True
    else:
        return False
