__author__ = 'bruno'


def gcd_euclidean(a, b):
    while a != b:
        if a > b:
            a = a-b
        else:
            b = b-a
    return a
