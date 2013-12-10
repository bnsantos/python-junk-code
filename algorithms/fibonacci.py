__author__ = 'bruno'
import sys
sys.path.insert(0, '../helper')
import helper.validateInput as ValidateInput


def recursive(n):
    if ValidateInput.validate_integer_positive_input(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return recursive(n-1)+recursive(n-2)
    else:
        return None


def incremental(n):
    if ValidateInput.validate_integer_positive_input(n):
        if n == 0:
            return 0
        else:
            fib = 1
            ant = 0
            i = 1
            while i < n:
                i += 1
                aux = fib
                fib += ant
                ant = aux
            return fib
    else:
        return None