__author__ = 'bruno'


def validate_input(n):
    if type(n) == type(int()) and n >= 0:
        return True
    else:
        return False


def recursive(n):
    if validate_input(n):
        if n == 0:
            return 1
        elif n == 1:
            return 1
        else:
            return n * recursive(n-1)
    else:
        return None


def incremental(n):
    if validate_input(n):
        fat = 1
        i = 1
        while i <= n:
            fat = fat * i
            i += 1
        return fat
    else:
        return None