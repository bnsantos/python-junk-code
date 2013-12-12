__author__ = 'bruno'


def russian(a, b):
    x = a
    y = b
    z = 0
    while x > 0:
        if x % 2 == 1:
            z = z + y
        y <<= 1
        x >>= 1
    return z