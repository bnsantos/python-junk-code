__author__ = 'bruno'
import helper.validateInput as ValidateInput


def recursive(n):
    """
        O(2^n) time complexity
    """
    if ValidateInput.validate_integer_positive_input(n):
        if n == 0:
            return 1
        elif n == 1:
            return 1
        else:
            return n * recursive(n-1)
    else:
        return None


def incremental(n):
    if ValidateInput.validate_integer_positive_input(n):
        fat = 1
        i = 1
        while i <= n:
            fat = fat * i
            i += 1
        return fat
    else:
        return None